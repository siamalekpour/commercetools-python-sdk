# DO NOT EDIT! This file is automatically generated
import typing

import marshmallow
from marshmallow import fields

from commercetools._schemas._product import (
    ProductDraftSchema,
    ProductPagedQueryResponseSchema,
    ProductSchema,
    ProductUpdateSchema,
)
from commercetools.helpers import OptionalList, RemoveEmptyValuesMixin
from commercetools.types._product import (
    Product,
    ProductDraft,
    ProductPagedQueryResponse,
    ProductUpdate,
    ProductUpdateAction,
)
from commercetools.typing import OptionalListStr

from . import abstract, traits


class _ProductGetSchema(traits.ExpandableSchema, traits.PriceSelectingSchema):
    pass


class _ProductQuerySchema(
    traits.ExpandableSchema,
    traits.SortableSchema,
    traits.PagingSchema,
    traits.QuerySchema,
    traits.PriceSelectingSchema,
):
    pass


class _ProductCreateSchema(traits.ExpandableSchema, traits.PriceSelectingSchema):
    pass


class _ProductUpdateSchema(
    traits.ExpandableSchema, traits.VersionedSchema, traits.PriceSelectingSchema
):
    pass


class _ProductDeleteSchema(
    traits.VersionedSchema, traits.ExpandableSchema, traits.PriceSelectingSchema
):
    pass


class _ProductImagesSchema(marshmallow.Schema, RemoveEmptyValuesMixin):
    filename = OptionalList(fields.String(), required=False)
    variant = fields.Int(required=False)
    sku = OptionalList(fields.String(), required=False)
    staged = fields.Bool(required=False, missing=False)


class ProductService(abstract.AbstractService):
    """Products are the sellable goods in an e-commerce project on CTP.

    This document explains some design concepts of products on CTP and describes the
    available HTTP APIs for working with them.
    """

    def get_by_id(
        self,
        id: str,
        *,
        expand: OptionalListStr = None,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListStr = None,
        price_channel: OptionalListStr = None,
        locale_projection: OptionalListStr = None,
        store_projection: OptionalListStr = None,
    ) -> Product:
        """Gets the full representation of a product by ID."""
        params = self._serialize_params(
            {
                "expand": expand,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "locale_projection": locale_projection,
                "store_projection": store_projection,
            },
            _ProductGetSchema,
        )
        return self._client._get(
            endpoint=f"products/{id}", params=params, schema_cls=ProductSchema
        )

    def get_by_key(
        self,
        key: str,
        *,
        expand: OptionalListStr = None,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListStr = None,
        price_channel: OptionalListStr = None,
        locale_projection: OptionalListStr = None,
        store_projection: OptionalListStr = None,
    ) -> Product:
        """Gets the full representation of a product by Key."""
        params = self._serialize_params(
            {
                "expand": expand,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "locale_projection": locale_projection,
                "store_projection": store_projection,
            },
            _ProductGetSchema,
        )
        return self._client._get(
            endpoint=f"products/key={key}", params=params, schema_cls=ProductSchema
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
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListStr = None,
        price_channel: OptionalListStr = None,
        locale_projection: OptionalListStr = None,
        store_projection: OptionalListStr = None,
    ) -> ProductPagedQueryResponse:
        """You can use the query endpoint to get the full representations of
        products.

        REMARK: We suggest to use the performance optimized search endpoint which
        has a bunch functionalities, the query API lacks like sorting on custom
        attributes, etc.   Products are the sellable goods in an e-commerce
        project on CTP. This document explains some design concepts of products
        on CTP and describes the available HTTP APIs for working with them.
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
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "locale_projection": locale_projection,
                "store_projection": store_projection,
            },
            _ProductQuerySchema,
        )
        return self._client._get(
            endpoint="products",
            params=params,
            schema_cls=ProductPagedQueryResponseSchema,
        )

    def create(
        self,
        draft: ProductDraft,
        *,
        expand: OptionalListStr = None,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListStr = None,
        price_channel: OptionalListStr = None,
        locale_projection: OptionalListStr = None,
        store_projection: OptionalListStr = None,
    ) -> Product:
        """To create a new product, send a representation that is going to become
        the initial staged representation

        of the new product in the master catalog. If price selection query
        parameters are provided, the selected prices will be added to the
        response.   Products are the sellable goods in an e-commerce project on
        CTP. This document explains some design concepts of products on CTP and
        describes the available HTTP APIs for working with them.
        """
        params = self._serialize_params(
            {
                "expand": expand,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "locale_projection": locale_projection,
                "store_projection": store_projection,
            },
            _ProductCreateSchema,
        )
        return self._client._post(
            endpoint="products",
            params=params,
            data_object=draft,
            request_schema_cls=ProductDraftSchema,
            response_schema_cls=ProductSchema,
        )

    def update_by_id(
        self,
        id: str,
        version: int,
        actions: typing.List[ProductUpdateAction],
        *,
        expand: OptionalListStr = None,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListStr = None,
        price_channel: OptionalListStr = None,
        locale_projection: OptionalListStr = None,
        store_projection: OptionalListStr = None,
        force_update: bool = False,
    ) -> Product:
        params = self._serialize_params(
            {
                "expand": expand,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "locale_projection": locale_projection,
                "store_projection": store_projection,
            },
            _ProductUpdateSchema,
        )
        update_action = ProductUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"products/{id}",
            params=params,
            data_object=update_action,
            request_schema_cls=ProductUpdateSchema,
            response_schema_cls=ProductSchema,
            force_update=force_update,
        )

    def update_by_key(
        self,
        key: str,
        version: int,
        actions: typing.List[ProductUpdateAction],
        *,
        expand: OptionalListStr = None,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListStr = None,
        price_channel: OptionalListStr = None,
        locale_projection: OptionalListStr = None,
        store_projection: OptionalListStr = None,
        force_update: bool = False,
    ) -> Product:
        params = self._serialize_params(
            {
                "expand": expand,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "locale_projection": locale_projection,
                "store_projection": store_projection,
            },
            _ProductUpdateSchema,
        )
        update_action = ProductUpdate(version=version, actions=actions)
        return self._client._post(
            endpoint=f"products/key={key}",
            params=params,
            data_object=update_action,
            request_schema_cls=ProductUpdateSchema,
            response_schema_cls=ProductSchema,
            force_update=force_update,
        )

    def delete_by_id(
        self,
        id: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListStr = None,
        price_channel: OptionalListStr = None,
        locale_projection: OptionalListStr = None,
        store_projection: OptionalListStr = None,
        force_delete: bool = False,
    ) -> Product:
        params = self._serialize_params(
            {
                "version": version,
                "expand": expand,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "locale_projection": locale_projection,
                "store_projection": store_projection,
            },
            _ProductDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"products/{id}",
            params=params,
            response_schema_cls=ProductSchema,
            force_delete=force_delete,
        )

    def delete_by_key(
        self,
        key: str,
        version: int,
        *,
        expand: OptionalListStr = None,
        price_currency: OptionalListStr = None,
        price_country: OptionalListStr = None,
        price_customer_group: OptionalListStr = None,
        price_channel: OptionalListStr = None,
        locale_projection: OptionalListStr = None,
        store_projection: OptionalListStr = None,
        force_delete: bool = False,
    ) -> Product:
        params = self._serialize_params(
            {
                "version": version,
                "expand": expand,
                "price_currency": price_currency,
                "price_country": price_country,
                "price_customer_group": price_customer_group,
                "price_channel": price_channel,
                "locale_projection": locale_projection,
                "store_projection": store_projection,
            },
            _ProductDeleteSchema,
        )
        return self._client._delete(
            endpoint=f"products/key={key}",
            params=params,
            response_schema_cls=ProductSchema,
            force_delete=force_delete,
        )

    def file_upload(
        self,
        id: str,
        fh: typing.BinaryIO,
        *,
        filename: str = None,
        variant: int = None,
        sku: str = None,
        staged: bool = None,
    ) -> Product:
        """Uploads a binary image file to a given product variant.

        The supported image formats are JPEG, PNG and GIF.
        """
        params = self._serialize_params(
            {"filename": filename, "variant": variant, "sku": sku, "staged": staged},
            _ProductImagesSchema,
        )
        return self._client._upload(
            endpoint=f"products/{id}/images",
            params=params,
            response_schema_cls=ProductSchema,
            file=fh,
        )

    def upload_image(
        self,
        id: str,
        fh: typing.BinaryIO,
        *,
        filename: str = None,
        variant: int = None,
        sku: str = None,
        staged: bool = None,
    ) -> Product:
        """Uploads a binary image file to a given product variant.

        The supported image formats are JPEG, PNG and GIF.
        """
        params = self._serialize_params(
            {"filename": filename, "variant": variant, "sku": sku, "staged": staged},
            _ProductImagesSchema,
        )
        return self._client._upload(
            endpoint=f"products/{id}/images",
            params=params,
            response_schema_cls=ProductSchema,
            file=fh,
        )
