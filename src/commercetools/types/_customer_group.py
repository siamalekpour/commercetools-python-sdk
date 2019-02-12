# DO NOT EDIT! This file is automatically generated

import datetime
import typing

import attr

from commercetools.types._base import PagedQueryResponse, Update, UpdateAction
from commercetools.types._common import Reference, ReferenceTypeId, Resource

if typing.TYPE_CHECKING:
    from ._type import CustomFields, FieldContainer, TypeReference
__all__ = [
    "CustomerGroup",
    "CustomerGroupChangeNameAction",
    "CustomerGroupDraft",
    "CustomerGroupPagedQueryResponse",
    "CustomerGroupReference",
    "CustomerGroupSetCustomFieldAction",
    "CustomerGroupSetCustomTypeAction",
    "CustomerGroupSetKeyAction",
    "CustomerGroupUpdate",
    "CustomerGroupUpdateAction",
]


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroupDraft:
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupDraftSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str` `(Named` ``groupName`` `in Commercetools)`
    group_name: typing.Optional[str]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        key: typing.Optional[str] = None,
        group_name: typing.Optional[str] = None,
        custom: typing.Optional["CustomFields"] = None
    ) -> None:
        self.key = key
        self.group_name = group_name
        self.custom = custom

    def __repr__(self) -> str:
        return "CustomerGroupDraft(key=%r, group_name=%r, custom=%r)" % (
            self.key,
            self.group_name,
            self.custom,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroup(Resource):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]
    #: :class:`str`
    name: typing.Optional[str]
    #: Optional :class:`commercetools.types.CustomFields`
    custom: typing.Optional["CustomFields"]

    def __init__(
        self,
        *,
        id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        created_at: typing.Optional[datetime.datetime] = None,
        last_modified_at: typing.Optional[datetime.datetime] = None,
        key: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        custom: typing.Optional["CustomFields"] = None
    ) -> None:
        self.key = key
        self.name = name
        self.custom = custom
        super().__init__(
            id=id,
            version=version,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

    def __repr__(self) -> str:
        return (
            "CustomerGroup(id=%r, version=%r, created_at=%r, last_modified_at=%r, key=%r, name=%r, custom=%r)"
            % (
                self.id,
                self.version,
                self.created_at,
                self.last_modified_at,
                self.key,
                self.name,
                self.custom,
            )
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroupPagedQueryResponse(PagedQueryResponse):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupPagedQueryResponseSchema`."
    #: List of :class:`commercetools.types.CustomerGroup`
    results: typing.Optional[typing.Sequence["CustomerGroup"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["CustomerGroup"]] = None
    ) -> None:
        self.results = results
        super().__init__(count=count, total=total, offset=offset, results=results)

    def __repr__(self) -> str:
        return (
            "CustomerGroupPagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)"
            % (self.count, self.total, self.offset, self.results)
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroupReference(Reference):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupReferenceSchema`."
    #: Optional :class:`commercetools.types.CustomerGroup`
    obj: typing.Optional["CustomerGroup"]

    def __init__(
        self,
        *,
        type_id: typing.Optional["ReferenceTypeId"] = None,
        id: typing.Optional[str] = None,
        key: typing.Optional[str] = None,
        obj: typing.Optional["CustomerGroup"] = None
    ) -> None:
        self.obj = obj
        super().__init__(type_id=ReferenceTypeId.CUSTOMER_GROUP, id=id, key=key)

    def __repr__(self) -> str:
        return "CustomerGroupReference(type_id=%r, id=%r, key=%r, obj=%r)" % (
            self.type_id,
            self.id,
            self.key,
            self.obj,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroupUpdate(Update):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupUpdateSchema`."
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
        return "CustomerGroupUpdate(version=%r, actions=%r)" % (
            self.version,
            self.actions,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroupUpdateAction(UpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupUpdateActionSchema`."

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        super().__init__(action=action)

    def __repr__(self) -> str:
        return "CustomerGroupUpdateAction(action=%r)" % (self.action,)


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroupChangeNameAction(CustomerGroupUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupChangeNameActionSchema`."
    #: :class:`str`
    name: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, name: typing.Optional[str] = None
    ) -> None:
        self.name = name
        super().__init__(action="changeName")

    def __repr__(self) -> str:
        return "CustomerGroupChangeNameAction(action=%r, name=%r)" % (
            self.action,
            self.name,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroupSetCustomFieldAction(CustomerGroupUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupSetCustomFieldActionSchema`."
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
        return "CustomerGroupSetCustomFieldAction(action=%r, name=%r, value=%r)" % (
            self.action,
            self.name,
            self.value,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroupSetCustomTypeAction(CustomerGroupUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupSetCustomTypeActionSchema`."
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
        return "CustomerGroupSetCustomTypeAction(action=%r, type=%r, fields=%r)" % (
            self.action,
            self.type,
            self.fields,
        )


@attr.s(auto_attribs=True, init=False, repr=False)
class CustomerGroupSetKeyAction(CustomerGroupUpdateAction):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.CustomerGroupSetKeyActionSchema`."
    #: Optional :class:`str`
    key: typing.Optional[str]

    def __init__(
        self, *, action: typing.Optional[str] = None, key: typing.Optional[str] = None
    ) -> None:
        self.key = key
        super().__init__(action="setKey")

    def __repr__(self) -> str:
        return "CustomerGroupSetKeyAction(action=%r, key=%r)" % (self.action, self.key)
