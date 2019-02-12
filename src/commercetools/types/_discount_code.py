# DO NOT EDIT! This file is automatically generated

import datetime
import typing

import attr

from commercetools.types._base import PagedQueryResponse, Update, UpdateAction
from commercetools.types._common import Reference, ReferenceTypeId, Resource

if typing.TYPE_CHECKING:
    from ._cart_discount import CartDiscountReference
    from ._common import LocalizedString
    from ._type import CustomFields, CustomFieldsDraft, FieldContainer, TypeReference
__all__ = [
    "DiscountCode",
    "DiscountCodeChangeCartDiscountsAction",
    "DiscountCodeChangeGroupsAction",
    "DiscountCodeChangeIsActiveAction",
    "DiscountCodeDraft",
    "DiscountCodePagedQueryResponse",
    "DiscountCodeReference",
    "DiscountCodeSetCartPredicateAction",
    "DiscountCodeSetCustomFieldAction",
    "DiscountCodeSetCustomTypeAction",
    "DiscountCodeSetDescriptionAction",
    "DiscountCodeSetMaxApplicationsAction",
    "DiscountCodeSetMaxApplicationsPerCustomerAction",
    "DiscountCodeSetNameAction",
    "DiscountCodeSetValidFromAction",
    "DiscountCodeSetValidFromAndUntilAction",
    "DiscountCodeSetValidUntilAction",
    "DiscountCodeUpdate",
    "DiscountCodeUpdateAction",
]


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeDraft:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeDraftSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: :class:`str`
    code: typing.Optional[str]
    #: List of :class:`commercetools.types.CartDiscountReference` `(Named` ``cartDiscounts`` `in Commercetools)`
    cart_discounts: typing.Optional[typing.List["CartDiscountReference"]]
    #: Optional :class:`str` `(Named` ``cartPredicate`` `in Commercetools)`
    cart_predicate: typing.Optional[str]
    #: Optional :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: typing.Optional[bool]
    #: Optional :class:`int` `(Named` ``maxApplications`` `in Commercetools)`
    max_applications: typing.Optional[int]
    #: Optional :class:`int` `(Named` ``maxApplicationsPerCustomer`` `in Commercetools)`
    max_applications_per_customer: typing.Optional[int]
    #: Optional :class:`commercetools.types.CustomFieldsDraft`
    custom: typing.Optional["CustomFieldsDraft"]
    #: Optional :class:`list`
    groups: typing.Optional[list]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        code: typing.Optional[str] = None,
        cart_discounts: typing.Optional[typing.List["CartDiscountReference"]] = None,
        cart_predicate: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        max_applications: typing.Optional[int] = None,
        max_applications_per_customer: typing.Optional[int] = None,
        custom: typing.Optional["CustomFieldsDraft"] = None,
        groups: typing.Optional[list] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.name = name
        self.description = description
        self.code = code
        self.cart_discounts = cart_discounts
        self.cart_predicate = cart_predicate
        self.is_active = is_active
        self.max_applications = max_applications
        self.max_applications_per_customer = max_applications_per_customer
        self.custom = custom
        self.groups = groups
        self.valid_from = valid_from
        self.valid_until = valid_until

    def __repr__(self) -> str:
        return (
            "DiscountCodeDraft(name=%r, description=%r, code=%r, cart_discounts=%r, cart_predicate=%r, is_active=%r, max_applications=%r, max_applications_per_customer=%r, custom=%r, groups=%r, valid_from=%r, valid_until=%r)"
            % (
                self.name,
                self.description,
                self.code,
                self.cart_discounts,
                self.cart_predicate,
                self.is_active,
                self.max_applications,
                self.max_applications_per_customer,
                self.custom,
                self.groups,
                self.valid_from,
                self.valid_until,
            )
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCode(Resource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: :class:`str`
    code: typing.Optional[str]
    #: List of :class:`commercetools.types.CartDiscountReference` `(Named` ``cartDiscounts`` `in Commercetools)`
    cart_discounts: typing.Optional[typing.List["CartDiscountReference"]]
    #: Optional :class:`str` `(Named` ``cartPredicate`` `in Commercetools)`
    cart_predicate: typing.Optional[str]
    #: :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: typing.Optional[bool]
    #: List of :class:`commercetools.types.Reference`
    references: typing.Optional[typing.List["Reference"]]
    #: Optional :class:`int` `(Named` ``maxApplications`` `in Commercetools)`
    max_applications: typing.Optional[int]
    #: Optional :class:`int` `(Named` ``maxApplicationsPerCustomer`` `in Commercetools)`
    max_applications_per_customer: typing.Optional[int]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]
    #: List of :class:`str`
    groups: typing.Optional[typing.List[str]]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        code: typing.Optional[str] = None,
        cart_discounts: typing.Optional[typing.List["CartDiscountReference"]] = None,
        cart_predicate: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        references: typing.Optional[typing.List["Reference"]] = None,
        max_applications: typing.Optional[int] = None,
        max_applications_per_customer: typing.Optional[int] = None,
        custom: typing.Optional["CustomFields"] = None,
        groups: typing.Optional[typing.List[str]] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.name = name
        self.description = description
        self.code = code
        self.cart_discounts = cart_discounts
        self.cart_predicate = cart_predicate
        self.is_active = is_active
        self.references = references
        self.max_applications = max_applications
        self.max_applications_per_customer = max_applications_per_customer
        self.custom = custom
        self.groups = groups
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "DiscountCode(id=%r, version=%r, created_at=%r, last_modified_at=%r, name=%r, description=%r, code=%r, cart_discounts=%r, cart_predicate=%r, is_active=%r, references=%r, max_applications=%r, max_applications_per_customer=%r, custom=%r, groups=%r, valid_from=%r, valid_until=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.name,
                self.description,
                self.code,
                self.cart_discounts,
                self.cart_predicate,
                self.is_active,
                self.references,
                self.max_applications,
                self.max_applications_per_customer,
                self.custom,
                self.groups,
                self.valid_from,
                self.valid_until,
            )
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodePagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodePagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.DiscountCode`
    results: typing.Optional[typing.Sequence["DiscountCode"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["DiscountCode"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return (
            "DiscountCodePagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeReferenceSchema`."
    #: Optional :class:`commercetools.types.DiscountCode`
    obj: typing.Optional["DiscountCode"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        obj: typing.Optional["DiscountCode"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.DISCOUNT_CODE, id=id, key=key)

    def __repr__(self) -> str:
        return "DiscountCodeReference(type_id=%r, id=%r, key=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.key,
            self.obj,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeUpdate(Update):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeUpdateSchema`."
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None
    ) -> None:
        self.actions = actions
        super().__init__(version=version, actions=actions)

    def __repr__(self) -> str:
        return "DiscountCodeUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeUpdateAction(UpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeUpdateActionSchema`."

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        super().__init__(action=action)

    def __repr__(self) -> str:
        return "DiscountCodeUpdateAction(action=%r)" % (self.action,)


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeChangeCartDiscountsAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeChangeCartDiscountsActionSchema`."
    #: List of :class:`commercetools.types.CartDiscountReference` `(Named` ``cartDiscounts`` `in Commercetools)`
    cart_discounts: typing.Optional[typing.List["CartDiscountReference"]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        cart_discounts: typing.Optional[typing.List["CartDiscountReference"]] = None
    ) -> None:
        self.cart_discounts = cart_discounts
        super().__init__(action="changeCartDiscounts")

    def __repr__(self) -> str:
        return "DiscountCodeChangeCartDiscountsAction(action=%r, cart_discounts=%r)" % (
            self.action,
            self.cart_discounts,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeChangeGroupsAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeChangeGroupsActionSchema`."
    #: List of :class:`str`
    groups: typing.Optional[typing.List[str]]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        groups: typing.Optional[typing.List[str]] = None
    ) -> None:
        self.groups = groups
        super().__init__(action="changeGroups")

    def __repr__(self) -> str:
        return "DiscountCodeChangeGroupsAction(action=%r, groups=%r)" % (
            self.action,
            self.groups,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeChangeIsActiveAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeChangeIsActiveActionSchema`."
    #: :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: typing.Optional[bool]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None
    ) -> None:
        self.is_active = is_active
        super().__init__(action="changeIsActive")

    def __repr__(self) -> str:
        return "DiscountCodeChangeIsActiveAction(action=%r, is_active=%r)" % (
            self.action,
            self.is_active,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetCartPredicateAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetCartPredicateActionSchema`."
    #: Optional :class:`str` `(Named` ``cartPredicate`` `in Commercetools)`
    cart_predicate: typing.Optional[str]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        cart_predicate: typing.Optional[str] = None
    ) -> None:
        self.cart_predicate = cart_predicate
        super().__init__(action="setCartPredicate")

    def __repr__(self) -> str:
        return "DiscountCodeSetCartPredicateAction(action=%r, cart_predicate=%r)" % (
            self.action,
            self.cart_predicate,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetCustomFieldAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetCustomFieldActionSchema`."
    #: :class:`str`
    name: typing.Optional[str]
    #: Optional :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        value: typing.Optional[typing.Any] = None
    ) -> None:
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    def __repr__(self) -> str:
        return "DiscountCodeSetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetCustomTypeAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetCustomTypeActionSchema`."
    #: Optional :class:`commercetools.types.TypeReference`
    type: typing.Optional["TypeReference"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        type: typing.Optional["TypeReference"] = None,
        fields: typing.Optional["FieldContainer"] = None
    ) -> None:
        self.type = type
        self.fields = fields
        super().__init__(action="setCustomType")

    def __repr__(self) -> str:
        return "DiscountCodeSetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetDescriptionAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetDescriptionActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        description: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "DiscountCodeSetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetMaxApplicationsAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetMaxApplicationsActionSchema`."
    #: Optional :class:`int` `(Named` ``maxApplications`` `in Commercetools)`
    max_applications: typing.Optional[int]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        max_applications: typing.Optional[int] = None
    ) -> None:
        self.max_applications = max_applications
        super().__init__(action="setMaxApplications")

    def __repr__(self) -> str:
        return (
            "DiscountCodeSetMaxApplicationsAction(action=%r, max_applications=%r)"
            % (self.action, self.max_applications)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetMaxApplicationsPerCustomerAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetMaxApplicationsPerCustomerActionSchema`."
    #: Optional :class:`int` `(Named` ``maxApplicationsPerCustomer`` `in Commercetools)`
    max_applications_per_customer: typing.Optional[int]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        max_applications_per_customer: typing.Optional[int] = None
    ) -> None:
        self.max_applications_per_customer = max_applications_per_customer
        super().__init__(action="setMaxApplicationsPerCustomer")

    def __repr__(self) -> str:
        return (
            "DiscountCodeSetMaxApplicationsPerCustomerAction(action=%r, max_applications_per_customer=%r)"
            % (self.action, self.max_applications_per_customer)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetNameAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetNameActionSchema`."
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        name: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.name = name
        super().__init__(action="setName")

    def __repr__(self) -> str:
        return "DiscountCodeSetNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetValidFromAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetValidFromActionSchema`."
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        valid_from: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_from = valid_from
        super().__init__(action="setValidFrom")

    def __repr__(self) -> str:
        return "DiscountCodeSetValidFromAction(action=%r, valid_from=%r)" % (
            self.action,
            self.valid_from,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetValidFromAndUntilAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetValidFromAndUntilActionSchema`."
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_from = valid_from
        self.valid_until = valid_until
        super().__init__(action="setValidFromAndUntil")

    def __repr__(self) -> str:
        return (
            "DiscountCodeSetValidFromAndUntilAction(action=%r, valid_from=%r, valid_until=%r)"
            % (self.action, self.valid_from, self.valid_until)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class DiscountCodeSetValidUntilAction(DiscountCodeUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.DiscountCodeSetValidUntilActionSchema`."
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        action: typing.Optional[str] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_until = valid_until
        super().__init__(action="setValidUntil")

    def __repr__(self) -> str:
        return "DiscountCodeSetValidUntilAction(action=%r, valid_until=%r)" % (
            self.action,
            self.valid_until,
        )
