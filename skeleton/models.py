# -*- coding: utf-8 -*-

from django.core.exceptions import EmptyResultSet
from django.db import connection
from django.db.models import CharField, Manager, Model, QuerySet, PositiveIntegerField
import numpy
import pandas
import typing


class SampleMixin(object):
    def sample(
        self,
        size: int = 1,
        query_filter: typing.Dict = None
    ):
        query = self.all() if query_filter is None else self.filter(**query_filter)

        return self.filter(
            pk__in = numpy.random.choice(
                a = query.values_list('pk', flat = True),
                size = size,
                replace = False
            )
        )


class BaseQuerySet(QuerySet, SampleMixin):
    """
    Custom methods you want on your querysets go here.
    """

    def to_df(self):
        try:
            query, params = self.query.sql_with_params()

        except EmptyResultSet:
            return pandas.DataFrame()

        return pandas.io.sql.read_sql_query(query, connection, params = params)


class BaseManager(Manager, SampleMixin):
    """
    A generic manager class with extra helpers.

    .. _models_utils_BaseManager:
    """

    def get_queryset(self):
        """
        This just implements querysets for the model managed by this manager as BaseQuerySets which have our custom methods
        """

        q = BaseQuerySet(self.model)
        return q if self._db is None else q.using(self._db)


class BaseModel(Model):
    """
    A few helper functions for models.

    .. _models_utils_BaseModel:
    """

    class Meta:
        abstract = True

    def values(
        self,
        values: typing.Tuple[str] = None,
        include_relationships: bool = False,
        include_null: bool = False
    ) -> typing.Dict:
        """
        Returns the values of the fields specified for the current record.

        :param values: A list of field names. If no list is supplied, all values are returned.
        :param include_relationships: By default, values which are relationships to other models are excluded.
        :param include_null: By default, values which are None are excluded.
        """

        data = {
            field_name: getattr(self, field_name) \
                for field_name in (
                    (
                        field.name for field in (
                            self._meta.fields \
                                if include_relationships is False \
                                else self._meta.get_fields()
                        )
                    ) if values is None else values
                )
        }

        return data \
            if include_null is True \
            else dict(filter(
                lambda kv: kv[1] is not None,
                data.items()
            ))


class Bird(BaseModel):
    objects = BaseManager()
    scientific_name = CharField(max_length = 255, unique = True, db_index = True)
    common_name = CharField(max_length = 255, null = True)
    body_mass = PositiveIntegerField(null = True)
    wingspan = PositiveIntegerField(null = True)
    wingbeat_amplitude = PositiveIntegerField(null = True)
    wingbeat_frequency = PositiveIntegerField(null = True)

    def airspeed(self):
        """
        http://style.org/unladenswallow/
        """
        return 3.0 * self.wingbeat_amplitude * self.wingbeat_frequency / 100
