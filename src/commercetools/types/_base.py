# DO NOT EDIT! This file is automatically generated

import datetime
import typing

from commercetools.types._abstract import _BaseType

if typing.TYPE_CHECKING:
    from ._common import Resource
__all__ = ["PagedQueryResponse", "Update", "UpdateAction"]


class PagedQueryResponse(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.PagedQueryResponseSchema`."
    #: :class:`int`
    count: typing.Optional[int]
    #: Optional :class:`int`
    total: typing.Optional[int]
    #: :class:`int`
    offset: typing.Optional[int]
    #: List of :class:`commercetools.types.Resource`
    results: typing.Optional[typing.Sequence["Resource"]]

    def __init__(
        self,
        *,
        count: typing.Optional[int] = None,
        total: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        results: typing.Optional[typing.Sequence["Resource"]] = None
    ) -> None:
        self.count = count
        self.total = total
        self.offset = offset
        self.results = results
        super().__init__()

    def __repr__(self) -> str:
        return "PagedQueryResponse(count=%r, total=%r, offset=%r, results=%r)" % (
            self.count,
            self.total,
            self.offset,
            self.results,
        )


class Update(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.UpdateSchema`."
    #: :class:`int`
    version: typing.Optional[int]
    #: :class:`list`
    actions: typing.Optional[list]

    def __init__(
        self,
        *,
        version: typing.Optional[int] = None,
        actions: typing.Optional[list] = None
    ) -> None:
        self.version = version
        self.actions = actions
        super().__init__()

    def __repr__(self) -> str:
        return "Update(version=%r, actions=%r)" % (self.version, self.actions)


class UpdateAction(_BaseType):
    "Corresponding marshmallow schema is :class:`commercetools.schemas.UpdateActionSchema`."
    #: :class:`str`
    action: typing.Optional[str]

    def __init__(self, *, action: typing.Optional[str] = None) -> None:
        self.action = action
        super().__init__()

    def __repr__(self) -> str:
        return "UpdateAction(action=%r)" % (self.action,)
