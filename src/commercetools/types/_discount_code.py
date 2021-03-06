# DO NOT EDIT! This file is automatically generated
import datetime
import typing

from commercetools.types._abstract import _BaseType
from commercetools.types._common import (
    BaseResource,
    Reference,
    ReferenceTypeId,
    ResourceIdentifier,
)

if typing.TYPE_CHECKING:
    from ._cart_discount import CartDiscountReference, CartDiscountResourceIdentifier
    from ._common import CreatedBy, LastModifiedBy, LocalizedString
    from ._type import (
        CustomFields,
        CustomFieldsDraft,
        FieldContainer,
        TypeResourceIdentifier,
    )
__all__ = [
    "DiscountCode",
    "DiscountCodeChangeCartDiscountsAction",
    "DiscountCodeChangeGroupsAction",
    "DiscountCodeChangeIsActiveAction",
    "DiscountCodeDraft",
    "DiscountCodePagedQueryResponse",
    "DiscountCodeReference",
    "DiscountCodeResourceIdentifier",
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


class DiscountCode(BaseResource):
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
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: :class:`str`
    code: str
    #: List of :class:`commercetools.types.CartDiscountReference` `(Named` ``cartDiscounts`` `in Commercetools)`
    cart_discounts: typing.List["CartDiscountReference"]
    #: Optional :class:`str` `(Named` ``cartPredicate`` `in Commercetools)`
    cart_predicate: typing.Optional[str]
    #: :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: bool
    #: List of :class:`commercetools.types.Reference`
    references: typing.List["Reference"]
    #: Optional :class:`int` `(Named` ``maxApplications`` `in Commercetools)`
    max_applications: typing.Optional[int]
    #: Optional :class:`int` `(Named` ``maxApplicationsPerCustomer`` `in Commercetools)`
    max_applications_per_customer: typing.Optional[int]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]
    #: List of :class:`str`
    groups: typing.List[str]
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        id: str,
        version: int,
        created_at: datetime.datetime,
        last_modified_at: datetime.datetime,
        code: str,
        cart_discounts: typing.List["CartDiscountReference"],
        is_active: bool,
        references: typing.List["Reference"],
        groups: typing.List[str],
        last_modified_by: typing.Optional["LastModifiedBy"] = None,
        created_by: typing.Optional["CreatedBy"] = None,
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
        cart_predicate: typing.Optional[str] = None,
        max_applications: typing.Optional[int] = None,
        max_applications_per_customer: typing.Optional[int] = None,
        custom: typing.Optional["CustomFields"] = None,
        valid_from: typing.Optional[datetime.datetime] = None,
        valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.id = id
        self.version = version
        self.created_at = created_at
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by
        self.created_by = created_by
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
            "DiscountCode(id=%r, version=%r, created_at=%r, last_modified_at=%r, last_modified_by=%r, created_by=%r, name=%r, description=%r, code=%r, cart_discounts=%r, cart_predicate=%r, is_active=%r, references=%r, max_applications=%r, max_applications_per_customer=%r, custom=%r, groups=%r, valid_from=%r, valid_until=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.last_modified_by,
                self.created_by,
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


class DiscountCodeDraft(_BaseType):
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]
    #: :class:`str`
    code: str
    #: List of :class:`commercetools.types.CartDiscountResourceIdentifier` `(Named` ``cartDiscounts`` `in Commercetools)`
    cart_discounts: typing.List["CartDiscountResourceIdentifier"]
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
        code: str,
        cart_discounts: typing.List["CartDiscountResourceIdentifier"],
        name: typing.Optional["LocalizedString"] = None,
        description: typing.Optional["LocalizedString"] = None,
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
        super().__init__()

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


class DiscountCodePagedQueryResponse(_BaseType):
    #: :class:`int`
    limit: int
    #: :class:`int`
    count: int
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: int
    #: List of :class:`commercetools.types.DiscountCode`
    results: typing.Sequence["DiscountCode"]

    def __init__(
        self,
        *,
        limit: int,
        count: int,
        offset: int,
        results: typing.Sequence["DiscountCode"],
        total: typing.Optional[int] = None
    ) -> None:
        self.limit = limit
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return (
            "DiscountCodePagedQueryResponse(limit=%r, count=%r, total=%r, offset=%r, results=%r)"
            % (self.limit, self.count, self.total, self.offset, self.results)
        )


class DiscountCodeReference(Reference):
    #: Optional :class:`commercetools.types.DiscountCode`
    obj: typing.Optional["DiscountCode"]

    def __init__(self, *, id: str, obj: typing.Optional["DiscountCode"] = None) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.DISCOUNT_CODE, id=id)

    def __repr__(self) -> str:
        return "DiscountCodeReference(type_id=%r, id=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.obj,
        )


class DiscountCodeResourceIdentifier(ResourceIdentifier):
    def __init__(
        self, *, id: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        super().__init__(type_id=ReferenceTypeId.DISCOUNT_CODE, id=id, key=key)

    def __repr__(self) -> str:
        return "DiscountCodeResourceIdentifier(type_id=%r, id=%r, key=%r)" % (
            self.type_id,
            self.id,
            self.key,
        )


class DiscountCodeUpdate(_BaseType):
    #: :class:`int`
    version: int
    #: :class:`list`
    actions: list

    def __init__(self, *, version: int, actions: list) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "DiscountCodeUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


class DiscountCodeUpdateAction(_BaseType):
    #: :class:`str`
    action: str

    def __init__(self, *, action: str) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "DiscountCodeUpdateAction(action=%r)" % (self.action,)


class DiscountCodeChangeCartDiscountsAction(DiscountCodeUpdateAction):
    #: List of :class:`commercetools.types.CartDiscountResourceIdentifier` `(Named` ``cartDiscounts`` `in Commercetools)`
    cart_discounts: typing.List["CartDiscountResourceIdentifier"]

    def __init__(
        self, *, cart_discounts: typing.List["CartDiscountResourceIdentifier"]
    ) -> None:
        self.cart_discounts = cart_discounts
        super().__init__(action="changeCartDiscounts")

    def __repr__(self) -> str:
        return "DiscountCodeChangeCartDiscountsAction(action=%r, cart_discounts=%r)" % (
            self.action,
            self.cart_discounts,
        )


class DiscountCodeChangeGroupsAction(DiscountCodeUpdateAction):
    #: List of :class:`str`
    groups: typing.List[str]

    def __init__(self, *, groups: typing.List[str]) -> None:
        self.groups = groups
        super().__init__(action="changeGroups")

    def __repr__(self) -> str:
        return "DiscountCodeChangeGroupsAction(action=%r, groups=%r)" % (
            self.action,
            self.groups,
        )


class DiscountCodeChangeIsActiveAction(DiscountCodeUpdateAction):
    #: :class:`bool` `(Named` ``isActive`` `in Commercetools)`
    is_active: bool

    def __init__(self, *, is_active: bool) -> None:
        self.is_active = is_active
        super().__init__(action="changeIsActive")

    def __repr__(self) -> str:
        return "DiscountCodeChangeIsActiveAction(action=%r, is_active=%r)" % (
            self.action,
            self.is_active,
        )


class DiscountCodeSetCartPredicateAction(DiscountCodeUpdateAction):
    #: Optional :class:`str` `(Named` ``cartPredicate`` `in Commercetools)`
    cart_predicate: typing.Optional[str]

    def __init__(self, *, cart_predicate: typing.Optional[str] = None) -> None:
        self.cart_predicate = cart_predicate
        super().__init__(action="setCartPredicate")

    def __repr__(self) -> str:
        return "DiscountCodeSetCartPredicateAction(action=%r, cart_predicate=%r)" % (
            self.action,
            self.cart_predicate,
        )


class DiscountCodeSetCustomFieldAction(DiscountCodeUpdateAction):
    #: :class:`str`
    name: str
    #: Optional :class:`typing.Any`
    value: typing.Optional[typing.Any]

    def __init__(self, *, name: str, value: typing.Optional[typing.Any] = None) -> None:
        self.name = name
        self.value = value
        super().__init__(action="setCustomField")

    def __repr__(self) -> str:
        return "DiscountCodeSetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


class DiscountCodeSetCustomTypeAction(DiscountCodeUpdateAction):
    #: Optional :class:`commercetools.types.TypeResourceIdentifier`
    type: typing.Optional["TypeResourceIdentifier"]
    #: Optional :class:`commercetools.types.FieldContainer`
    fields: typing.Optional["FieldContainer"]

    def __init__(
        self,
        *,
        type: typing.Optional["TypeResourceIdentifier"] = None,
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


class DiscountCodeSetDescriptionAction(DiscountCodeUpdateAction):
    #: Optional :class:`commercetools.types.LocalizedString`
    description: typing.Optional["LocalizedString"]

    def __init__(
        self, *, description: typing.Optional["LocalizedString"] = None
    ) -> None:
        self.description = description
        super().__init__(action="setDescription")

    def __repr__(self) -> str:
        return "DiscountCodeSetDescriptionAction(action=%r, description=%r)" % (
            self.action,
            self.description,
        )


class DiscountCodeSetMaxApplicationsAction(DiscountCodeUpdateAction):
    #: Optional :class:`int` `(Named` ``maxApplications`` `in Commercetools)`
    max_applications: typing.Optional[int]

    def __init__(self, *, max_applications: typing.Optional[int] = None) -> None:
        self.max_applications = max_applications
        super().__init__(action="setMaxApplications")

    def __repr__(self) -> str:
        return (
            "DiscountCodeSetMaxApplicationsAction(action=%r, max_applications=%r)"
            % (self.action, self.max_applications)
        )


class DiscountCodeSetMaxApplicationsPerCustomerAction(DiscountCodeUpdateAction):
    #: Optional :class:`int` `(Named` ``maxApplicationsPerCustomer`` `in Commercetools)`
    max_applications_per_customer: typing.Optional[int]

    def __init__(
        self, *, max_applications_per_customer: typing.Optional[int] = None
    ) -> None:
        self.max_applications_per_customer = max_applications_per_customer
        super().__init__(action="setMaxApplicationsPerCustomer")

    def __repr__(self) -> str:
        return (
            "DiscountCodeSetMaxApplicationsPerCustomerAction(action=%r, max_applications_per_customer=%r)"
            % (self.action, self.max_applications_per_customer)
        )


class DiscountCodeSetNameAction(DiscountCodeUpdateAction):
    #: Optional :class:`commercetools.types.LocalizedString`
    name: typing.Optional["LocalizedString"]

    def __init__(self, *, name: typing.Optional["LocalizedString"] = None) -> None:
        self.name = name
        super().__init__(action="setName")

    def __repr__(self) -> str:
        return "DiscountCodeSetNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


class DiscountCodeSetValidFromAction(DiscountCodeUpdateAction):
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]

    def __init__(
        self, *, valid_from: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_from = valid_from
        super().__init__(action="setValidFrom")

    def __repr__(self) -> str:
        return "DiscountCodeSetValidFromAction(action=%r, valid_from=%r)" % (
            self.action,
            self.valid_from,
        )


class DiscountCodeSetValidFromAndUntilAction(DiscountCodeUpdateAction):
    #: Optional :class:`datetime.datetime` `(Named` ``validFrom`` `in Commercetools)`
    valid_from: typing.Optional[datetime.datetime]
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
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


class DiscountCodeSetValidUntilAction(DiscountCodeUpdateAction):
    #: Optional :class:`datetime.datetime` `(Named` ``validUntil`` `in Commercetools)`
    valid_until: typing.Optional[datetime.datetime]

    def __init__(
        self, *, valid_until: typing.Optional[datetime.datetime] = None
    ) -> None:
        self.valid_until = valid_until
        super().__init__(action="setValidUntil")

    def __repr__(self) -> str:
        return "DiscountCodeSetValidUntilAction(action=%r, valid_until=%r)" % (
            self.action,
            self.valid_until,
        )
