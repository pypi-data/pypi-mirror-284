import uuid
from viggocore.common.subsystem.pagination import Pagination
from typing import Any, Type

from viggocore.common import exception
from sqlalchemy import func, or_
from sqlalchemy.orm import exc
from sqlalchemy.sql import text

from viggocore.common.subsystem.transaction_manager import TransactionManager


class Driver(object):

    def __init__(self, resource: Type[Any],
                 transaction_manager: TransactionManager) -> None:
        self.resource = resource
        self.transaction_manager = transaction_manager

    def removeId(self, entity_aux):
        new_id = uuid.uuid4().hex

        if entity_aux.get('id') is not None:
            new_id = entity_aux.pop('id')

        return new_id

    def instantiate(self, **kwargs):
        try:
            embedded = {}
            for attr in self.resource.embedded():
                if attr not in kwargs:
                    raise Exception(
                        f'O campo embedded {attr} é obrigatório em ' +
                        f'{self.resource.__name__}.')
                embedded.update({attr: kwargs.pop(attr)})

            instance = self.resource(**kwargs)

            for attr in embedded:
                value = embedded[attr]
                var = getattr(self.resource, attr)
                # TODO(samueldmq): is this good enough? should we discover it?
                mapped_attr = {self.resource.individual() + '_id': instance.id}
                if isinstance(value, list):
                    setattr(instance, attr, [var.property.mapper.class_(
                        id=self.removeId(ref), **dict(ref, **mapped_attr))
                        for ref in value])
                else:
                    # TODO(samueldmq): id is inserted here. it is in the
                    # manager for the entities. do it all in the resource
                    # contructor
                    setattr(instance, attr, var.property.mapper.class_(
                        id=uuid.uuid4().hex, **dict(value, **mapped_attr)))
        except Exception as exec:
            # TODO(samueldmq): replace with specific exception
            message = ''.join(exec.args)
            raise exception.BadRequest(message)

        return instance

    def create(self, entity, session):
        if not entity.is_stable():
            raise exception.PreconditionFailed()
        session.add(entity)
        session.flush()

    def update(self, entity, data, session):
        # try:
        #     entity = self.get(id, session)
        # except exc.NoResultFound:
        #     raise exception.NotFound()

        for attr in self.resource.embedded():
            if attr in data:
                value = data.pop(attr)
                var = getattr(self.resource, attr)
                # TODO(samueldmq): is this good enough? should we discover it?
                mapped_attr = {self.resource.individual() + '_id': id}
                if isinstance(value, list):
                    setattr(entity, attr, [var.property.mapper.class_(
                        id=self.removeId(ref), **dict(ref, **mapped_attr))
                        for ref in value])
                else:
                    # TODO(samueldmq): id is inserted here. it is in the
                    # manager for the entities. do it all in the resource
                    # contructor
                    setattr(entity, attr, var.property.mapper.class_(
                        id=uuid.uuid4().hex, **dict(value, **mapped_attr)))

        for key, value in data.items():
            if hasattr(entity, key):
                try:
                    setattr(entity, key, value)
                except AttributeError:
                    raise exception.BadRequest(
                        f'Error! The attribute {key} is read only')
            else:
                raise exception.BadRequest(
                    f'Error! The attribute {key} not exists')

        if not entity.is_stable():
            raise exception.PreconditionFailed()
        session.flush()
        return entity

    def delete(self, entity, session):
        session.delete(entity)
        session.flush()

    def get(self, id, session):
        try:
            query = session.query(self.resource).filter_by(id=id)
            result = query.one()
        except exc.NoResultFound:
            raise exception.NotFound()

        return result

    def list(self, session, **kwargs):
        if 'query' in kwargs.keys():
            query = kwargs.pop('query', None)
            pagination = Pagination.get_pagination(self.resource, **kwargs)

            query = self.apply_filters(query, self.resource, **kwargs)
            pagination.adjust_dinamic_order_by(self.resource)
            query = self.apply_pagination(query, pagination)

            result = query.all()
            result = list(map(lambda x: x[0], result))
            return result
        else:
            query = session.query(self.resource)

            pagination = Pagination.get_pagination(self.resource, **kwargs)

            query = self.apply_filters(query, self.resource, **kwargs)
            query = self.apply_pagination(query, pagination)

            result = query.all()
            return result

    def count(self, session, **kwargs):
        try:
            # TODO(JogeSilva): improve filtering so as not to ignore parameters
            # that are attributes of an entity to include
            query = session.query(self.resource.id)
            rows = self.apply_filters(query, self.resource, **kwargs).count()
            result = rows
        except exc.NoResultFound:
            raise exception.NotFound()

        return result

    def activate_or_deactivate_multiple_entities(self, session, **kwargs):
        active = kwargs.pop('active', None)

        entities = self.list_multiple_selection(session, **kwargs)
        key = 'active'

        for entity in entities:
            if hasattr(entity, key):
                setattr(entity, key, active)
            else:
                raise exception.BadRequest(
                    f'Error! The attribute {key} not exists.')

            if not entity.is_stable():
                raise exception.PreconditionFailed()
        session.flush()
        return entities

    def list_multiple_selection(self, session, **kwargs):
        query_in_kwargs = False
        multiple_selection = kwargs.get('multiple_selection', None)
        if multiple_selection is None:
            raise exception.BadRequest('multiple_selection is required.')

        resource_filtro = self.resource
        resource = kwargs.pop('resource', None)
        if resource is not None:
            resource_filtro = resource

        if 'query' in kwargs.keys():
            query = kwargs.pop('query', None)
            query_in_kwargs = True
        else:
            query = session.query(resource_filtro)

        query = self.apply_filters(query, resource_filtro, **kwargs)
        query = self.apply_filter_multiple_selection(
            query, resource_filtro, **kwargs)

        query = query.distinct()
        result = query.all()

        if query_in_kwargs is True:
            result = list(map(lambda x: x[0], result))

        return result

    def apply_filter_multiple_selection(self, query, resource, **kwargs):
        multiple_selection = kwargs.get('multiple_selection', {})
        for k, v in multiple_selection.items():
            if k == 'selected_list' and len(v) > 0:
                query = query.filter(resource.id.in_(v))
            elif k == 'unselected_list' and len(v) > 0:
                query = query.filter(resource.id.not_in(v))
        return query

    def apply_filters(self, query, resource, **kwargs):
        for k, v in kwargs.items():
            if hasattr(resource, k):
                if k == 'tag':
                    values = v
                    if len(v) > 0 and v[0] == '#':
                        values = v[1:]
                    values = values.split(',')
                    filter_tags = []
                    for value in values:
                        filter_tags.append(
                            getattr(resource, k)
                            .like('%#' + str(value) + ' %'))
                    query = query.filter(or_(*filter_tags))
                elif isinstance(v, str) and '%' in v:
                    normalize = func.viggocore_normalize
                    query = query.filter(normalize(getattr(resource, k))
                                         .ilike(normalize(v)))
                else:
                    query = query.filter(getattr(resource, k) == v)

        return query

    def apply_pagination(self, query, pagination: Pagination):
        if (pagination.order_by is not None):
            query = query.order_by(text(pagination.order_by))

        if pagination.page_size is not None:
            query = query.limit(pagination.page_size)
            if pagination.page is not None:
                query = query.offset(pagination.page * pagination.page_size)

        return query
