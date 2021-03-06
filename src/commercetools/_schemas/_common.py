# DO NOT EDIT! This file is automatically generated
import marshmallow
import marshmallow_enum

from commercetools import helpers, types

__all__ = [
    "AddressSchema",
    "AssetDimensionsSchema",
    "AssetDraftSchema",
    "AssetSchema",
    "AssetSourceSchema",
    "BaseResourceSchema",
    "CentPrecisionMoneyDraftSchema",
    "CentPrecisionMoneySchema",
    "ClientLoggingSchema",
    "CreatedBySchema",
    "DiscountedPriceSchema",
    "GeoJsonPointSchema",
    "GeoJsonSchema",
    "HighPrecisionMoneyDraftSchema",
    "HighPrecisionMoneySchema",
    "ImageDimensionsSchema",
    "ImageSchema",
    "KeyReferenceSchema",
    "LastModifiedBySchema",
    "MoneySchema",
    "PagedQueryResponseSchema",
    "PriceDraftSchema",
    "PriceSchema",
    "PriceTierDraftSchema",
    "PriceTierSchema",
    "QueryPriceSchema",
    "ReferenceSchema",
    "ResourceIdentifierSchema",
    "ScopedPriceSchema",
    "TypedMoneyDraftSchema",
    "TypedMoneySchema",
    "UpdateActionSchema",
    "UpdateSchema",
]


class LocalizedStringField(marshmallow.fields.Dict):
    def _deserialize(self, value, attr, data, **kwargs):
        result = super()._deserialize(value, attr, data)
        return types.LocalizedString(**result)


class AddressSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.Address`."""

    id = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    title = marshmallow.fields.String(allow_none=True, missing=None)
    salutation = marshmallow.fields.String(allow_none=True, missing=None)
    first_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="firstName"
    )
    last_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="lastName"
    )
    street_name = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="streetName"
    )
    street_number = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="streetNumber"
    )
    additional_street_info = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="additionalStreetInfo"
    )
    postal_code = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="postalCode"
    )
    city = marshmallow.fields.String(allow_none=True, missing=None)
    region = marshmallow.fields.String(allow_none=True, missing=None)
    state = marshmallow.fields.String(allow_none=True, missing=None)
    country = marshmallow.fields.String()
    company = marshmallow.fields.String(allow_none=True, missing=None)
    department = marshmallow.fields.String(allow_none=True, missing=None)
    building = marshmallow.fields.String(allow_none=True, missing=None)
    apartment = marshmallow.fields.String(allow_none=True, missing=None)
    p_o_box = marshmallow.fields.String(allow_none=True, missing=None, data_key="pOBox")
    phone = marshmallow.fields.String(allow_none=True, missing=None)
    mobile = marshmallow.fields.String(allow_none=True, missing=None)
    email = marshmallow.fields.String(allow_none=True, missing=None)
    fax = marshmallow.fields.String(allow_none=True, missing=None)
    additional_address_info = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="additionalAddressInfo"
    )
    external_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Address(**data)


class AssetDimensionsSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.AssetDimensions`."""

    w = marshmallow.fields.Integer(allow_none=True)
    h = marshmallow.fields.Integer(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.AssetDimensions(**data)


class AssetDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.AssetDraft`."""

    sources = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AssetSourceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    name = LocalizedStringField(allow_none=True)
    description = LocalizedStringField(allow_none=True, missing=None)
    tags = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), missing=None
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.AssetDraft(**data)


class AssetSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.Asset`."""

    id = marshmallow.fields.String(allow_none=True)
    sources = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AssetSourceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    name = LocalizedStringField(allow_none=True)
    description = LocalizedStringField(allow_none=True, missing=None)
    tags = marshmallow.fields.List(
        marshmallow.fields.String(allow_none=True), missing=None
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Asset(**data)


class AssetSourceSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.AssetSource`."""

    uri = marshmallow.fields.String(allow_none=True)
    key = marshmallow.fields.String(allow_none=True, missing=None)
    dimensions = helpers.LazyNestedField(
        nested="commercetools._schemas._common.AssetDimensionsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    content_type = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="contentType"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.AssetSource(**data)


class BaseResourceSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.BaseResource`."""

    id = marshmallow.fields.String(allow_none=True)
    version = marshmallow.fields.Integer(allow_none=True)
    created_at = marshmallow.fields.DateTime(allow_none=True, data_key="createdAt")
    last_modified_at = marshmallow.fields.DateTime(
        allow_none=True, data_key="lastModifiedAt"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.BaseResource(**data)


class ClientLoggingSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ClientLogging`."""

    client_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="clientId"
    )
    external_user_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="externalUserId"
    )
    customer = helpers.LazyNestedField(
        nested="commercetools._schemas._customer.CustomerReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    anonymous_id = marshmallow.fields.String(
        allow_none=True, missing=None, data_key="anonymousId"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ClientLogging(**data)


class DiscountedPriceSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.DiscountedPrice`."""

    value = helpers.LazyNestedField(
        nested="commercetools._schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    discount = helpers.LazyNestedField(
        nested="commercetools._schemas._product_discount.ProductDiscountReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.DiscountedPrice(**data)


class GeoJsonSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.GeoJson`."""

    type = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.GeoJson(**data)


class ImageDimensionsSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ImageDimensions`."""

    w = marshmallow.fields.Integer(allow_none=True)
    h = marshmallow.fields.Integer(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ImageDimensions(**data)


class ImageSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.Image`."""

    url = marshmallow.fields.String(allow_none=True)
    dimensions = helpers.LazyNestedField(
        nested="commercetools._schemas._common.ImageDimensionsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    label = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Image(**data)


class KeyReferenceSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.KeyReference`."""

    type_id = marshmallow_enum.EnumField(
        types.ReferenceTypeId, by_value=True, data_key="typeId"
    )
    key = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.KeyReference(**data)


class MoneySchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.Money`."""

    cent_amount = marshmallow.fields.Integer(allow_none=True, data_key="centAmount")
    currency_code = marshmallow.fields.String(data_key="currencyCode")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Money(**data)


class PagedQueryResponseSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.PagedQueryResponse`."""

    limit = marshmallow.fields.Integer(allow_none=True)
    count = marshmallow.fields.Integer(allow_none=True)
    total = marshmallow.fields.Integer(allow_none=True, missing=None)
    offset = marshmallow.fields.Integer(allow_none=True)
    results = helpers.LazyNestedField(
        nested="commercetools._schemas._common.BaseResourceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
    )
    facets = helpers.LazyNestedField(
        nested="commercetools._schemas._product.FacetResultsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    meta = marshmallow.fields.Dict(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.PagedQueryResponse(**data)


class PriceDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.PriceDraft`."""

    value = helpers.LazyNestedField(
        nested="commercetools._schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    country = marshmallow.fields.String(missing=None)
    customer_group = helpers.LazyNestedField(
        nested="commercetools._schemas._customer_group.CustomerGroupResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested="commercetools._schemas._channel.ChannelResourceIdentifierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    tiers = helpers.LazyNestedField(
        nested="commercetools._schemas._common.PriceTierDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )
    discounted = helpers.LazyNestedField(
        nested="commercetools._schemas._common.DiscountedPriceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.PriceDraft(**data)


class PriceSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.Price`."""

    id = marshmallow.fields.String(allow_none=True)
    value = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools._schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools._schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    country = marshmallow.fields.String(missing=None)
    customer_group = helpers.LazyNestedField(
        nested="commercetools._schemas._customer_group.CustomerGroupReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested="commercetools._schemas._channel.ChannelReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
    discounted = helpers.LazyNestedField(
        nested="commercetools._schemas._common.DiscountedPriceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    tiers = helpers.LazyNestedField(
        nested="commercetools._schemas._common.PriceTierSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Price(**data)


class PriceTierDraftSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.PriceTierDraft`."""

    minimum_quantity = marshmallow.fields.Integer(
        allow_none=True, data_key="minimumQuantity"
    )
    value = helpers.LazyNestedField(
        nested="commercetools._schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.PriceTierDraft(**data)


class PriceTierSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.PriceTier`."""

    minimum_quantity = marshmallow.fields.Integer(
        allow_none=True, data_key="minimumQuantity"
    )
    value = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools._schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools._schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.PriceTier(**data)


class QueryPriceSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.QueryPrice`."""

    id = marshmallow.fields.String(allow_none=True)
    value = helpers.LazyNestedField(
        nested="commercetools._schemas._common.MoneySchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    country = marshmallow.fields.String(missing=None)
    customer_group = helpers.LazyNestedField(
        nested="commercetools._schemas._customer_group.CustomerGroupReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested="commercetools._schemas._channel.ChannelReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
    discounted = helpers.LazyNestedField(
        nested="commercetools._schemas._common.DiscountedPriceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    tiers = helpers.LazyNestedField(
        nested="commercetools._schemas._common.PriceTierDraftSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        many=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.QueryPrice(**data)


class ReferenceSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.Reference`."""

    type_id = marshmallow_enum.EnumField(
        types.ReferenceTypeId, by_value=True, data_key="typeId"
    )
    id = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.Reference(**data)


class ResourceIdentifierSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ResourceIdentifier`."""

    type_id = marshmallow_enum.EnumField(
        types.ReferenceTypeId, by_value=True, missing=None, data_key="typeId"
    )
    id = marshmallow.fields.String(allow_none=True, missing=None)
    key = marshmallow.fields.String(allow_none=True, missing=None)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type_id"]
        return types.ResourceIdentifier(**data)


class ScopedPriceSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.ScopedPrice`."""

    id = marshmallow.fields.String(allow_none=True)
    value = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools._schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools._schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
    )
    current_value = helpers.Discriminator(
        discriminator_field=("type", "type"),
        discriminator_schemas={
            "centPrecision": "commercetools._schemas._common.CentPrecisionMoneySchema",
            "highPrecision": "commercetools._schemas._common.HighPrecisionMoneySchema",
        },
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        data_key="currentValue",
    )
    country = marshmallow.fields.String(missing=None)
    customer_group = helpers.LazyNestedField(
        nested="commercetools._schemas._customer_group.CustomerGroupReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
        data_key="customerGroup",
    )
    channel = helpers.LazyNestedField(
        nested="commercetools._schemas._channel.ChannelReferenceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    valid_from = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validFrom"
    )
    valid_until = marshmallow.fields.DateTime(
        allow_none=True, missing=None, data_key="validUntil"
    )
    discounted = helpers.LazyNestedField(
        nested="commercetools._schemas._common.DiscountedPriceSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )
    custom = helpers.LazyNestedField(
        nested="commercetools._schemas._type.CustomFieldsSchema",
        unknown=marshmallow.EXCLUDE,
        allow_none=True,
        missing=None,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.ScopedPrice(**data)


class TypedMoneySchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.TypedMoney`."""

    type = marshmallow_enum.EnumField(types.MoneyType, by_value=True)
    fraction_digits = marshmallow.fields.Integer(
        allow_none=True, data_key="fractionDigits"
    )
    cent_amount = marshmallow.fields.Integer(allow_none=True, data_key="centAmount")
    currency_code = marshmallow.fields.String(data_key="currencyCode")

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.TypedMoney(**data)


class UpdateActionSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.UpdateAction`."""

    action = marshmallow.fields.String(allow_none=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.UpdateAction(**data)


class UpdateSchema(marshmallow.Schema):
    """Marshmallow schema for :class:`commercetools.types.Update`."""

    version = marshmallow.fields.Integer(allow_none=True)
    actions = marshmallow.fields.List(
        helpers.LazyNestedField(
            nested="commercetools._schemas._common.UpdateActionSchema",
            unknown=marshmallow.EXCLUDE,
            allow_none=True,
        ),
        allow_none=True,
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.Update(**data)


class CentPrecisionMoneySchema(TypedMoneySchema):
    """Marshmallow schema for :class:`commercetools.types.CentPrecisionMoney`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.CentPrecisionMoney(**data)


class CreatedBySchema(ClientLoggingSchema):
    """Marshmallow schema for :class:`commercetools.types.CreatedBy`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.CreatedBy(**data)


class GeoJsonPointSchema(GeoJsonSchema):
    """Marshmallow schema for :class:`commercetools.types.GeoJsonPoint`."""

    coordinates = marshmallow.fields.List(
        marshmallow.fields.Integer(allow_none=True), allow_none=True
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.GeoJsonPoint(**data)


class HighPrecisionMoneySchema(TypedMoneySchema):
    """Marshmallow schema for :class:`commercetools.types.HighPrecisionMoney`."""

    precise_amount = marshmallow.fields.Integer(
        allow_none=True, data_key="preciseAmount"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.HighPrecisionMoney(**data)


class LastModifiedBySchema(ClientLoggingSchema):
    """Marshmallow schema for :class:`commercetools.types.LastModifiedBy`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        return types.LastModifiedBy(**data)


class TypedMoneyDraftSchema(MoneySchema):
    """Marshmallow schema for :class:`commercetools.types.TypedMoneyDraft`."""

    type = marshmallow_enum.EnumField(types.MoneyType, by_value=True)

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.TypedMoneyDraft(**data)


class CentPrecisionMoneyDraftSchema(TypedMoneyDraftSchema):
    """Marshmallow schema for :class:`commercetools.types.CentPrecisionMoneyDraft`."""

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.CentPrecisionMoneyDraft(**data)


class HighPrecisionMoneyDraftSchema(TypedMoneyDraftSchema):
    """Marshmallow schema for :class:`commercetools.types.HighPrecisionMoneyDraft`."""

    precise_amount = marshmallow.fields.Integer(
        allow_none=True, data_key="preciseAmount"
    )

    class Meta:
        unknown = marshmallow.EXCLUDE

    @marshmallow.post_load
    def post_load(self, data, **kwargs):
        del data["type"]
        return types.HighPrecisionMoneyDraft(**data)
