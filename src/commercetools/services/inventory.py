# DO NOT EDIT! This file is automatically generated
import typing

from commercetools._schemas._inventory import (
    InventoryEntryDraftSchema,
    InventoryEntrySchema,
    InventoryEntryUpdateSchema,
    InventoryPagedQueryResponseSchema,
)
from commercetools.helpers import RemoveEmptyValuesMixin
from commercetools.types._inventory import (
    InventoryEntry,
    InventoryEntryDraft,
    InventoryEntryUpdate,
    InventoryEntryUpdateAction,
    InventoryPagedQueryResponse,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _InventoryEntryQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
):
    pass


class _InventoryEntryUpdateSchema(traits.ExpandableSchema, traits.VersionedSchema):
    pass


class _InventoryEntryDeleteSchema(traits.VersionedSchema, traits.ExpandableSchema):
    pass


class InventoryEntryService(abstract.AbstractService):
    """Inventory allows you to track stock quantities."""

    def get_by_id(self, id: str, *, expand: OptionalListStr = None) -> InventoryEntry:
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._get(
            endpoint=f"inventory/{id}", params=params, schema_cls=InventoryEntrySchema
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
    ) -> InventoryPagedQueryResponse:
        """Inventory allows you to track stock quantities.
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
            _InventoryEntryQuerySchema,
        )
        return self._client._get(
            endpoint="inventory",
            params=params,
            schema_cls=InventoryPagedQueryResponseSchema,
        )

    def create(
        self, draft: InventoryEntryDraft, *, expand: OptionalListStr = None
    ) -> InventoryEntry:
        """Inventory allows you to track stock quantities.
        """
        params = self._serialize_params({"expand": expand}, traits.ExpandableSchema)
        return self._client._post(
            endpoint="inventory",
            params=params,
            data_object=draft,
            request_schema_cls=InventoryEntryDraftSchema,
            response_schema_cls=InventoryEntrySchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[InventoryEntryUpdateAction],
        *,
        expand: OptionalListStr = None,
        force_update: bool = False,
    ) -> InventoryEntry:
        params = self._serialize_params({"expand": expand}, _InventoryEntryUpdateSchema)
        update_action = InventoryEntryUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"inventory/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=InventoryEntryUpdateSchema,
            response_schema_cls=InventoryEntrySchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        force_delete: bool = False,
    ) -> InventoryEntry:
        params = self._serialize_params(
            {"version": version, "expand": expand}, _InventoryEntryDeleteSchema
        )
        return self._client._delete(
            endpoint=f"inventory/{id}",
            params=params,
            response_schema_cls=InventoryEntrySchema,
            force_delete=force_delete,
        )
