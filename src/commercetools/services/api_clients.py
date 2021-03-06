# DO NOT EDIT! This file is automatically generated
import typing

from commercetools._schemas._api_client import (
    ApiClientDraftSchema,
    ApiClientPagedQueryResponseSchema,
    ApiClientSchema,
)
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.types._api_client import (
    ApiClient,
    ApiClientDraft,
    ApiClientPagedQueryResponse,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _ApiClientQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class ApiClientService(abstract.AbstractService):
    """Manage your API Clients via an API.

    Useful for Infrastructure-as-Code tooling, and regularly rotating API secrets.
    """

    def get_by_id(self, id) -> ApiClient:
        """Get ApiClient by ID"""
        params: typing.Dict[str, str] = {}
        return self._client._get(
            endpoint=f"api-clients/{id}", params=params, schema_cls=ApiClientSchema
        )

    def query(
        self,
        *,
        expand: OptionalListStr = None,
        sort: OptionalListStr = None,
        limit: int = None,
        offset: int = None,
        with_total: bool = None,
        where: OptionalListStr = None,
        predicate_var: typing.Dict[str, str] = None,
    ) -> ApiClientPagedQueryResponse:
        """Manage your API Clients via an API. Useful for Infrastructure-as-Code
        tooling, and regularly rotating API secrets.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "sort": sort,
                "limit": limit,
                "offset": offset,
                "with_total": with_total,
                "where": where,
                "predicate_var": predicate_var,
            },
            _ApiClientQuerySchema,
        )
        return self._client._get(
            endpoint="api-clients",
            params=params,
            schema_cls=ApiClientPagedQueryResponseSchema,
        )

    def create(
        self, draft: ApiClientDraft, *, expand: OptionalListStr = None
    ) -> ApiClient:
        """Manage your API Clients via an API. Useful for Infrastructure-as-Code
        tooling, and regularly rotating API secrets.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="api-clients",
            params=params,
            data_object=draft,
            request_schema_cls=ApiClientDraftSchema,
            response_schema_cls=ApiClientSchema,
        )

    def delete_by_id(self, id, *, force_delete: bool = False) -> ApiClient:
        """Delete ApiClient by ID"""
        params: typing.Dict[str, str] = {}
        return self._client._delete(
            endpoint=f"api-clients/{id}",
            params=params,
            response_schema_cls=ApiClientSchema,
            force_delete=force_delete,
        )
