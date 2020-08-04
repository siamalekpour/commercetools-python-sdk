# DO NOT EDIT! This file is automatically generated
import datetime
import enum
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    BaseResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._common import CreatedBy, LastModifiedBy, LocalizedString
__all__ = [
    "AttributeBooleanType",
    "AttributeConstraintEnum",
    "AttributeConstraintEnumDraft",
    "AttributeDateTimeType",
    "AttributeDateType",
    "AttributeDefinition",
    "AttributeDefinitionDraft",
    "AttributeEnumType",
    "AttributeLocalizableTextType",
    "AttributeLocalizedEnumType",
    "AttributeLocalizedEnumValue",
    "AttributeMoneyType",
    "AttributeNestedType",
    "AttributeNumberType",
    "AttributePlainEnumValue",
    "AttributeReferenceType",
    "AttributeSetType",
    "AttributeTextType",
    "AttributeTimeType",
    "AttributeType",
    "ProductType",
    "ProductTypeAddAttributeDefinitionAction",
    "ProductTypeAddLocalizedEnumValueAction",
    "ProductTypeAddPlainEnumValueAction",
    "ProductTypeChangeAttributeConstraintAction",
    "ProductTypeChangeAttributeNameAction",
    "ProductTypeChangeAttributeOrderAction",
    "ProductTypeChangeAttributeOrderByNameAction",
    "ProductTypeChangeDescriptionAction",
    "ProductTypeChangeEnumKeyAction",
    "ProductTypeChangeInputHintAction",
    "ProductTypeChangeIsSearchableAction",
    "ProductTypeChangeLabelAction",
    "ProductTypeChangeLocalizedEnumValueLabelAction",
    "ProductTypeChangeLocalizedEnumValueOrderAction",
    "ProductTypeChangeNameAction",
    "ProductTypeChangePlainEnumValueLabelAction",
    "ProductTypeChangePlainEnumValueOrderAction",
    "ProductTypeDraft",
    "ProductTypePagedQueryResponse",
    "ProductTypeReference",
    "ProductTypeRemoveAttributeDefinitionAction",
    "ProductTypeRemoveEnumValuesAction",
    "ProductTypeResourceIdentifier",
    "ProductTypeSetInputTipAction",
    "ProductTypeSetKeyAction",
    "ProductTypeUpdate",
    "ProductTypeUpdateAction",
    "TextInputHint",
]


class AttributeConstraintEnum(enum.Enum):
    NONE = "None"
    UNIQUE = "Unique"
    COMBINATION_UNIQUE = "CombinationUnique"
    SAME_FOR_ALL = "SameForAll"


class AttributeConstraintEnumDraft(enum.Enum):
    NONE = "None"


class AttributeDefinition(_BaseType):
    #: :class:`commercetools.types.AttributeType`
    type: "AttributeType"
    #: :class:`str`
    name: str
    #: :class:`commercetools.types.LocalizedString`
    label: "LocalizedString"
    #: :class:`bool` `(Named` ``isRequired`` `in Commercetools)`
    is_required: bool
    #: :class:`commercetools.types.AttributeConstraintEnum` `(Named` ``attributeConstraint`` `in Commercetools)`
    attribute_constraint: "AttributeConstraintEnum"
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``inputTip`` `in Commercetools)`
    input_tip: typing.Optional["LocalizedString"]
    #: :class:`commercetools.types.TextInputHint` `(Named` ``inputHint`` `in Commercetools)`
    input_hint: "TextInputHint"
    #: :class:`bool` `(Named` ``isSearchable`` `in Commercetools)`
    is_searchable: bool

    def __init__(
        self,
        *,
        type: "AttributeType" = None,
        name: str = None,
        label: "LocalizedString" = None,
        is_required: bool = None,
        attribute_constraint: "AttributeConstraintEnum" = None,
        input_tip: typing.Optional["LocalizedString"] = None,
        input_hint: "TextInputHint" = None,
        is_searchable: bool = None
    ) -> None:
        self.type = type
        self.name = name
        self.label = label
        self.is_required = is_required
        self.attribute_constraint = attribute_constraint
        self.input_tip = input_tip
        self.input_hint = input_hint
        self.is_searchable = is_searchable
        super().__init__()

    def __repr__(self) -> str:
        return (
            "AttributeDefinition(type=%r, name=%r, label=%r, is_required=%r, attribute_constraint=%r, input_tip=%r, input_hint=%r, is_searchable=%r)"
            % (
                self.type,
                self.name,
                self.label,
                self.is_required,
                self.attribute_constraint,
                self.input_tip,
                self.input_hint,
                self.is_searchable,
            )
        )


class AttributeDefinitionDraft(_BaseType):
    #: :class:`commercetools.types.AttributeType`
    type: "AttributeType"
    #: :class:`str`
    name: str
    #: :class:`commercetools.types.LocalizedString`
    label: "LocalizedString"
    #: :class:`bool` `(Named` ``isRequired`` `in Commercetools)`
    is_required: bool
    #: Optional :class:`commercetools.types.AttributeConstraintEnum` `(Named` ``attributeConstraint`` `in Commercetools)`
    attribute_constraint: typing.Optional["AttributeConstraintEnum"]
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``inputTip`` `in Commercetools)`
    input_tip: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.TextInputHint` `(Named` ``inputHint`` `in Commercetools)`
    input_hint: typing.Optional["TextInputHint"]
    #: Optional :class:`bool` `(Named` ``isSearchable`` `in Commercetools)`
    is_searchable: typing.Optional[bool]

    def __init__(
        self,
        *,
        type: "AttributeType" = None,
        name: str = None,
        label: "LocalizedString" = None,
        is_required: bool = None,
        attribute_constraint: typing.Optional["AttributeConstraintEnum"] = None,
        input_tip: typing.Optional["LocalizedString"] = None,
        input_hint: typing.Optional["TextInputHint"] = None,
        is_searchable: typing.Optional[bool] = None
    ) -> None:
        self.type = type
        self.name = name
        self.label = label
        self.is_required = is_required
        self.attribute_constraint = attribute_constraint
        self.input_tip = input_tip
        self.input_hint = input_hint
        self.is_searchable = is_searchable
        super().__init__()

    def __repr__(self) -> str:
        return (
            "AttributeDefinitionDraft(type=%r, name=%r, label=%r, is_required=%r, attribute_constraint=%r, input_tip=%r, input_hint=%r, is_searchable=%r)"
            % (
                self.type,
                self.name,
                self.label,
                self.is_required,
                self.attribute_constraint,
                self.input_tip,
                self.input_hint,
                self.is_searchable,
            )
        )


class AttributeLocalizedEnumValue(_BaseType):
    #: :class:`str`
    key: str
    #: :class:`commercetools.types.LocalizedString`
    label: "LocalizedString"

    def __init__(self, *, key: str = None, label: "LocalizedString" = None) -> None:
        self.key = key
        self.label = label
        super().__init__()

    def __repr__(self) -> str:
        return "AttributeLocalizedEnumValue(key=%r, label=%r)" % (self.key, self.label)


class AttributePlainEnumValue(_BaseType):
    #: :class:`str`
    key: str
    #: :class:`str`
    label: str

    def __init__(self, *, key: str = None, label: str = None) -> None:
        self.key = key
        self.label = label
        super().__init__()

    def __repr__(self) -> str:
        return "AttributePlainEnumValue(key=%r, label=%r)" % (self.key, self.label)


class AttributeType(_BaseType):
    #: :class:`str`
    name: str

    def __init__(self, *, name: str = None) -> None:
        self.name = name
        super().__init__()

    def __repr__(self) -> str:
        return "AttributeType(name=%r)" % (self.name,)


class ProductType(BaseResource):
    #: :class:`str`
    id: str
    #: :class:`int`
    version: int
    #: :class:`datetime.datetime` `(Named` ``createdAt`` `in Commercetools)`
    created_at: datetime.datetime
    #: :class:`datetime.datetime` `(Named` ``lastModifiedAt`` `in Commercetools)`
    last_modified_at: datetime.datetime
    #: Optional :class:`commercetools.types.LastModifiedBy` `(Named` ``lastModifiedBy`` `in Commercetools)`
    last_modified_by: typing.Optional["LastModifiedBy"]
    #: Optional :class:`commercetools.types.CreatedBy` `(Named` ``createdBy`` `in Commercetools)`
    created_by: typing.Optional["CreatedBy"]
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: str
    #: :class:`str`
    description: str
    #: Optional list of :class:`commercetools.types.AttributeDefinition`
    attributes: typing.Optional[typing.List["AttributeDefinition"]]

    def __init__(
        self,
        *,
        id: str = None,
        version: int = None,
        created_at: datetime.datetime = None,
        last_modified_at: datetime.datetime = None,
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        key: typing.Optional[str] = None,
        name: str = None,
        description: str = None,
        attributes: typing.Optional[typing.List["AttributeDefinition"]] = None
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by
        self.created_by = created_by
        self.key = key
        self.name = name
        self.description = description
        self.attributes = attributes
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "ProductType(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, key=%r, name=%r, description=%r, attributes=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
                self.key,
                self.name,
                self.description,
                self.attributes,
            )
        )


class ProductTypeDraft(_BaseType):
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: str
    #: :class:`str`
    description: str
    #: Optional list of :class:`commercetools.types.AttributeDefinitionDraft`
    attributes: typing.Optional[typing.List["AttributeDefinitionDraft"]]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        name: str = None,
        description: str = None,
        attributes: typing.Optional[typing.List["AttributeDefinitionDraft"]] = None
    ) -> None:
        self.key = key
        self.name = name
        self.description = description
        self.attributes = attributes
        super().__init__()

    def __repr__(self) -> str:
        return "ProductTypeDraft(key=%r, name=%r, description=%r, attributes=%r)" % (
            self.key,
            self.name,
            self.description,
            self.attributes,
        )


class ProductTypePagedQueryResponse(_BaseType):
    #: :class:`int`
    limit: int
    #: :class:`int`
    count: int
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: int
    #: List of :class:`commercetools.types.ProductType`
    results: typing.Sequence["ProductType"]

    def __init__(
        self,
        *,
        limit: int = None,
        count: int = None,
        total: typing.Optional[int] = None,
        offset: int = None,
        results: typing.Sequence["ProductType"] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "ProductTypePagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class ProductTypeReference(Reference):
    #: Optional :class:`commercetools.types.ProductType`
    obj: typing.Optional["ProductType"]

    def __init__(
        self,
        *,
        type_id: "ReferenceTypeId" = None,
        id: str = None,
        obj: typing.Optional["ProductType"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.PRODUCT_TYPE, id=id)

    def __repr__(self) -> str:
        return "ProductTypeReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class ProductTypeResourceIdentifier(ResourceIdentifier):
    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.PRODUCT_TYPE, id=id, key=key)

    def __repr__(self) -> str:
        return "ProductTypeResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class ProductTypeUpdate(_BaseType):
    #: :class:`int`
    version: int
    #: :class:`list`
    actions: list

    def __init__(self, *, version: int = None, actions: list = None) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "ProductTypeUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


class ProductTypeUpdateAction(_BaseType):
    #: :class:`str`
    action: str

    def __init__(self, *, action: str = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "ProductTypeUpdateAction(action=%r)" % (self.action,)


class TextInputHint(enum.Enum):
    SINGLE_LINE = "SingleLine"
    MULTI_LINE = "MultiLine"


class AttributeBooleanType(AttributeType):
    def __init__(self, *, name: str = None) -> None:
        super().__init__(name="boolean")

    def __repr__(self) -> str:
        return "AttributeBooleanType(name=%r)" % (self.name,)


class AttributeDateTimeType(AttributeType):
    def __init__(self, *, name: str = None) -> None:
        super().__init__(name="datetime")

    def __repr__(self) -> str:
        return "AttributeDateTimeType(name=%r)" % (self.name,)


class AttributeDateType(AttributeType):
    def __init__(self, *, name: str = None) -> None:
        super().__init__(name="date")

    def __repr__(self) -> str:
        return "AttributeDateType(name=%r)" % (self.name,)


class AttributeEnumType(AttributeType):
    #: List of :class:`commercetools.types.AttributePlainEnumValue`
    values: typing.List["AttributePlainEnumValue"]

    def __init__(
        self, *, name: str = None, values: typing.List["AttributePlainEnumValue"] = None
    ) -> None:
        self.values = values
        super().__init__(name="enum")

    def __repr__(self) -> str:
        return "AttributeEnumType(name=%r, values=%r)" % (self.name, self.values)


class AttributeLocalizableTextType(AttributeType):
    def __init__(self, *, name: str = None) -> None:
        super().__init__(name="ltext")

    def __repr__(self) -> str:
        return "AttributeLocalizableTextType(name=%r)" % (self.name,)


class AttributeLocalizedEnumType(AttributeType):
    #: List of :class:`commercetools.types.AttributeLocalizedEnumValue`
    values: typing.List["AttributeLocalizedEnumValue"]

    def __init__(
        self,
        *,
        name: str = None,
        values: typing.List["AttributeLocalizedEnumValue"] = None
    ) -> None:
        self.values = values
        super().__init__(name="lenum")

    def __repr__(self) -> str:
        return "AttributeLocalizedEnumType(name=%r, values=%r)" % (
            self.name,
            self.values,
        )


class AttributeMoneyType(AttributeType):
    def __init__(self, *, name: str = None) -> None:
        super().__init__(name="money")

    def __repr__(self) -> str:
        return "AttributeMoneyType(name=%r)" % (self.name,)


class AttributeNestedType(AttributeType):
    #: :class:`commercetools.types.ProductTypeReference` `(Named` ``typeReference`` `in Commercetools)`
    type_reference: "ProductTypeReference"

    def __init__(
        self, *, name: str = None, type_reference: "ProductTypeReference" = None
    ) -> None:
        self.type_reference = type_reference
        super().__init__(name="nested")

    def __repr__(self) -> str:
        return "AttributeNestedType(name=%r, type_reference=%r)" % (
            self.name,
            self.type_reference,
        )


class AttributeNumberType(AttributeType):
    def __init__(self, *, name: str = None) -> None:
        super().__init__(name="number")

    def __repr__(self) -> str:
        return "AttributeNumberType(name=%r)" % (self.name,)


class AttributeReferenceType(AttributeType):
    #: :class:`commercetools.types.ReferenceTypeId` `(Named` ``referenceTypeId`` `in Commercetools)`
    reference_type_id: "ReferenceTypeId"

    def __init__(
        self, *, name: str = None, reference_type_id: "ReferenceTypeId" = None
    ) -> None:
        self.reference_type_id = reference_type_id
        super().__init__(name="reference")

    def __repr__(self) -> str:
        return "AttributeReferenceType(name=%r, reference_type_id=%r)" % (
            self.name,
            self.reference_type_id,
        )


class AttributeSetType(AttributeType):
    #: :class:`commercetools.types.AttributeType` `(Named` ``elementType`` `in Commercetools)`
    element_type: "AttributeType"

    def __init__(
        self, *, name: str = None, element_type: "AttributeType" = None
    ) -> None:
        self.element_type = element_type
        super().__init__(name="set")

    def __repr__(self) -> str:
        return "AttributeSetType(name=%r, element_type=%r)" % (
            self.name,
            self.element_type,
        )


class AttributeTextType(AttributeType):
    def __init__(self, *, name: str = None) -> None:
        super().__init__(name="text")

    def __repr__(self) -> str:
        return "AttributeTextType(name=%r)" % (self.name,)


class AttributeTimeType(AttributeType):
    def __init__(self, *, name: str = None) -> None:
        super().__init__(name="time")

    def __repr__(self) -> str:
        return "AttributeTimeType(name=%r)" % (self.name,)


class ProductTypeAddAttributeDefinitionAction(ProductTypeUpdateAction):
    #: :class:`commercetools.types.AttributeDefinitionDraft`
    attribute: "AttributeDefinitionDraft"

    def __init__(
        self, *, action: str = None, attribute: "AttributeDefinitionDraft" = None
    ) -> None:
        self.attribute = attribute
        super().__init__(action="addAttributeDefinition")

    def __repr__(self) -> str:
        return "ProductTypeAddAttributeDefinitionAction(action=%r, attribute=%r)" % (
            self.action,
            self.attribute,
        )


class ProductTypeAddLocalizedEnumValueAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`commercetools.types.AttributeLocalizedEnumValue`
    value: "AttributeLocalizedEnumValue"

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        value: "AttributeLocalizedEnumValue" = None
    ) -> None:
        self.attribute_name = attribute_name
        self.value = value
        super().__init__(action="addLocalizedEnumValue")

    def __repr__(self) -> str:
        return (
            "ProductTypeAddLocalizedEnumValueAction(action=%r, attribute_name=%r, value=%r)"
            % (self.action, self.attribute_name, self.value)
        )


class ProductTypeAddPlainEnumValueAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`commercetools.types.AttributePlainEnumValue`
    value: "AttributePlainEnumValue"

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        value: "AttributePlainEnumValue" = None
    ) -> None:
        self.attribute_name = attribute_name
        self.value = value
        super().__init__(action="addPlainEnumValue")

    def __repr__(self) -> str:
        return (
            "ProductTypeAddPlainEnumValueAction(action=%r, attribute_name=%r, value=%r)"
            % (self.action, self.attribute_name, self.value)
        )


class ProductTypeChangeAttributeConstraintAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`commercetools.types.AttributeConstraintEnumDraft` `(Named` ``newValue`` `in Commercetools)`
    new_value: "AttributeConstraintEnumDraft"

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        new_value: "AttributeConstraintEnumDraft" = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changeAttributeConstraint")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeAttributeConstraintAction(action=%r, attribute_name=%r, new_value=%r)"
            % (self.action, self.attribute_name, self.new_value)
        )


class ProductTypeChangeAttributeNameAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`str` `(Named` ``newAttributeName`` `in Commercetools)`
    new_attribute_name: str

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        new_attribute_name: str = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_attribute_name = new_attribute_name
        super().__init__(action="changeAttributeName")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeAttributeNameAction(action=%r, attribute_name=%r, new_attribute_name=%r)"
            % (self.action, self.attribute_name, self.new_attribute_name)
        )


class ProductTypeChangeAttributeOrderAction(ProductTypeUpdateAction):
    #: List of :class:`commercetools.types.AttributeDefinition`
    attributes: typing.List["AttributeDefinition"]

    def __init__(
        self,
        *,
        action: str = None,
        attributes: typing.List["AttributeDefinition"] = None
    ) -> None:
        self.attributes = attributes
        super().__init__(action="changeAttributeOrder")

    def __repr__(self) -> str:
        return "ProductTypeChangeAttributeOrderAction(action=%r, attributes=%r)" % (
            self.action,
            self.attributes,
        )


class ProductTypeChangeAttributeOrderByNameAction(ProductTypeUpdateAction):
    #: List of :class:`str` `(Named` ``attributeNames`` `in Commercetools)`
    attribute_names: typing.List[str]

    def __init__(
        self, *, action: str = None, attribute_names: typing.List[str] = None
    ) -> None:
        self.attribute_names = attribute_names
        super().__init__(action="changeAttributeOrderByName")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeAttributeOrderByNameAction(action=%r, attribute_names=%r)"
            % (self.action, self.attribute_names)
        )


class ProductTypeChangeDescriptionAction(ProductTypeUpdateAction):
    #: :class:`str`
    description: str

    def __init__(self, *, action: str = None, description: str = None) -> None:
        self.description = description
        super().__init__(action="changeDescription")

    def __repr__(self) -> str:
        return "ProductTypeChangeDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class ProductTypeChangeEnumKeyAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`str`
    key: str
    #: :class:`str` `(Named` ``newKey`` `in Commercetools)`
    new_key: str

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        key: str = None,
        new_key: str = None
    ) -> None:
        self.attribute_name = attribute_name
        self.key = key
        self.new_key = new_key
        super().__init__(action="changeEnumKey")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeEnumKeyAction(action=%r, attribute_name=%r, key=%r, new_key=%r)"
            % (self.action, self.attribute_name, self.key, self.new_key)
        )


class ProductTypeChangeInputHintAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`commercetools.types.TextInputHint` `(Named` ``newValue`` `in Commercetools)`
    new_value: "TextInputHint"

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        new_value: "TextInputHint" = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changeInputHint")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeInputHintAction(action=%r, attribute_name=%r, new_value=%r)"
            % (self.action, self.attribute_name, self.new_value)
        )


class ProductTypeChangeIsSearchableAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`bool` `(Named` ``isSearchable`` `in Commercetools)`
    is_searchable: bool

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        is_searchable: bool = None
    ) -> None:
        self.attribute_name = attribute_name
        self.is_searchable = is_searchable
        super().__init__(action="changeIsSearchable")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeIsSearchableAction(action=%r, attribute_name=%r, is_searchable=%r)"
            % (self.action, self.attribute_name, self.is_searchable)
        )


class ProductTypeChangeLabelAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`commercetools.types.LocalizedString`
    label: "LocalizedString"

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        label: "LocalizedString" = None
    ) -> None:
        self.attribute_name = attribute_name
        self.label = label
        super().__init__(action="changeLabel")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeLabelAction(action=%r, attribute_name=%r, label=%r)"
            % (self.action, self.attribute_name, self.label)
        )


class ProductTypeChangeLocalizedEnumValueLabelAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`commercetools.types.AttributeLocalizedEnumValue` `(Named` ``newValue`` `in Commercetools)`
    new_value: "AttributeLocalizedEnumValue"

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        new_value: "AttributeLocalizedEnumValue" = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changeLocalizedEnumValueLabel")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeLocalizedEnumValueLabelAction(action=%r, attribute_name=%r, new_value=%r)"
            % (self.action, self.attribute_name, self.new_value)
        )


class ProductTypeChangeLocalizedEnumValueOrderAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: List of :class:`commercetools.types.AttributeLocalizedEnumValue`
    values: typing.List["AttributeLocalizedEnumValue"]

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        values: typing.List["AttributeLocalizedEnumValue"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.values = values
        super().__init__(action="changeLocalizedEnumValueOrder")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangeLocalizedEnumValueOrderAction(action=%r, attribute_name=%r, values=%r)"
            % (self.action, self.attribute_name, self.values)
        )


class ProductTypeChangeNameAction(ProductTypeUpdateAction):
    #: :class:`str`
    name: str

    def __init__(self, *, action: str = None, name: str = None) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "ProductTypeChangeNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class ProductTypeChangePlainEnumValueLabelAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: :class:`commercetools.types.AttributePlainEnumValue` `(Named` ``newValue`` `in Commercetools)`
    new_value: "AttributePlainEnumValue"

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        new_value: "AttributePlainEnumValue" = None
    ) -> None:
        self.attribute_name = attribute_name
        self.new_value = new_value
        super().__init__(action="changePlainEnumValueLabel")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangePlainEnumValueLabelAction(action=%r, attribute_name=%r, new_value=%r)"
            % (self.action, self.attribute_name, self.new_value)
        )


class ProductTypeChangePlainEnumValueOrderAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: List of :class:`commercetools.types.AttributePlainEnumValue`
    values: typing.List["AttributePlainEnumValue"]

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        values: typing.List["AttributePlainEnumValue"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.values = values
        super().__init__(action="changePlainEnumValueOrder")

    def __repr__(self) -> str:
        return (
            "ProductTypeChangePlainEnumValueOrderAction(action=%r, attribute_name=%r, values=%r)"
            % (self.action, self.attribute_name, self.values)
        )


class ProductTypeRemoveAttributeDefinitionAction(ProductTypeUpdateAction):
    #: :class:`str`
    name: str

    def __init__(self, *, action: str = None, name: str = None) -> None:
        self.name = name
        super().__init__(action="removeAttributeDefinition")

    def __repr__(self) -> str:
        return "ProductTypeRemoveAttributeDefinitionAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class ProductTypeRemoveEnumValuesAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: List of :class:`str`
    keys: typing.List[str]

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        keys: typing.List[str] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.keys = keys
        super().__init__(action="removeEnumValues")

    def __repr__(self) -> str:
        return (
            "ProductTypeRemoveEnumValuesAction(action=%r, attribute_name=%r, keys=%r)"
            % (self.action, self.attribute_name, self.keys)
        )


class ProductTypeSetInputTipAction(ProductTypeUpdateAction):
    #: :class:`str` `(Named` ``attributeName`` `in Commercetools)`
    attribute_name: str
    #: Optional :class:`commercetools.types.LocalizedString` `(Named` ``inputTip`` `in Commercetools)`
    input_tip: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: str = None,
        attribute_name: str = None,
        input_tip: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.attribute_name = attribute_name
        self.input_tip = input_tip
        super().__init__(action="setInputTip")

    def __repr__(self) -> str:
        return (
            "ProductTypeSetInputTipAction(action=%r, attribute_name=%r, input_tip=%r)"
            % (self.action, self.attribute_name, self.input_tip)
        )


class ProductTypeSetKeyAction(ProductTypeUpdateAction):
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(self, *, action: str = None, key: typing.Optional[str] = None) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "ProductTypeSetKeyAction(action=%r, key=%r)" % (self.action, self.key)
