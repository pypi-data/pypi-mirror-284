# Copyright (c) 2017-2024 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import abc
from datetime import datetime
import sys
from typing import (
    AbstractSet,
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Collection,
    DefaultDict,
    List,
    Optional,
    Sequence,
    TypeVar,
    Union,
    overload,
)

from .. import (
    Connection as _Connection,
    PackageService as _PackageService,
    QueryStream as _QueryStream,
)
from ...damlast.daml_lf_1 import PackageRef, TypeConName
from ...prim import ContractData, ContractId, Party, TimeDeltaLike
from ...query import Queries, Query
from ..api_types import (
    ArchiveEvent,
    Boundary,
    Command,
    CreateEvent,
    ExerciseResponse,
    MeteringReport,
    PartyInfo,
    Right,
    SubmitResponse,
    User,
    Version,
)
from .pkgloader import PackageLoader

if sys.version_info >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    from typing_extensions import Protocol, runtime_checkable

__all__ = ["PackageService", "Connection", "QueryStream", "QueryStreamBase", "PackageLoader"]

ConnSelf = TypeVar("ConnSelf", bound="Connection")
QSSelf = TypeVar("QSSelf", bound="QueryStream")
CreateFn = TypeVar("CreateFn", bound=Callable[[CreateEvent], SubmitResponse])
ACreateFn = TypeVar("ACreateFn", bound=Callable[[CreateEvent], Awaitable[SubmitResponse]])
ArchiveFn = TypeVar("ArchiveFn", bound=Callable[[ArchiveEvent], SubmitResponse])
AArchiveFn = TypeVar("AArchiveFn", bound=Callable[[ArchiveEvent], Awaitable[SubmitResponse]])
BoundaryFn = TypeVar("BoundaryFn", bound=Callable[[Boundary], SubmitResponse])
ABoundaryFn = TypeVar("ABoundaryFn", bound=Callable[[Boundary], Awaitable[SubmitResponse]])

# mypy treats Callables as _covariant_ in their arguments, and _contravariant_ in their return
# types. That means that A -> A and B -> B are incompatible types.
#
# However, we can define an object that has two overloaded __call__ signatures, which means that
# we have an *object* that can be used like a function, but supports adding additional "overloads",
# such that the base type supports being called with A, and returns A, and the subtype supports
# that, AS WELL AS being called with B and returning B.
#
# mypy completely understands what is going on here, and manages to validate correct usages of these
# decorators, *as well as* flagging incorrect usages!
class ACreateDecorator(Protocol):
    @overload
    def __call__(self, __fn: CreateFn) -> CreateFn: ...
    @overload
    def __call__(self, __fn: ACreateFn) -> ACreateFn: ...

class AArchiveDecorator(Protocol):
    @overload
    def __call__(self, __fn: ArchiveFn) -> ArchiveFn: ...
    @overload
    def __call__(self, __fn: AArchiveFn) -> AArchiveFn: ...

class ABoundaryDecorator(Protocol):
    @overload
    def __call__(self, __fn: BoundaryFn) -> BoundaryFn: ...
    @overload
    def __call__(self, __fn: ABoundaryFn) -> ABoundaryFn: ...

class PackageService(_PackageService, Protocol):
    async def get_package(
        self, __package_id: PackageRef, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> bytes: ...
    async def list_package_ids(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> AbstractSet[PackageRef]: ...

@runtime_checkable
class Connection(_Connection, PackageService, Protocol):
    async def __aenter__(self: ConnSelf) -> ConnSelf: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...
    async def open(self) -> None: ...
    async def close(self) -> None: ...
    async def submit(
        self,
        __commands: Union[Command, Sequence[Command]],
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
        deduplication_duration: Optional[TimeDeltaLike] = ...,
        deduplication_offset: Optional[str] = ...,
    ) -> None: ...
    async def create(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
        deduplication_duration: Optional[TimeDeltaLike] = ...,
        deduplication_offset: Optional[str] = ...,
    ) -> CreateEvent: ...
    async def exercise(
        self,
        __contract_id: ContractId,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        choice_interface_id: Union[None, str, TypeConName] = None,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
        deduplication_duration: Optional[TimeDeltaLike] = ...,
        deduplication_offset: Optional[str] = ...,
    ) -> ExerciseResponse: ...
    async def create_and_exercise(
        self,
        __template_id: Union[str, TypeConName],
        __payload: ContractData,
        __choice_name: str,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
        deduplication_duration: Optional[TimeDeltaLike] = ...,
        deduplication_offset: Optional[str] = ...,
    ) -> ExerciseResponse: ...
    async def exercise_by_key(
        self,
        __template_id: Union[str, TypeConName],
        __choice_name: str,
        __key: Any,
        __argument: Optional[ContractData] = None,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
        deduplication_duration: Optional[TimeDeltaLike] = ...,
        deduplication_offset: Optional[str] = ...,
    ) -> ExerciseResponse: ...
    async def archive(
        self,
        __contract_id: ContractId,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
        deduplication_duration: Optional[TimeDeltaLike] = ...,
        deduplication_offset: Optional[str] = ...,
    ) -> ArchiveEvent: ...
    async def archive_by_key(
        self,
        __template_id: str,
        __key: Any,
        *,
        workflow_id: Optional[str] = None,
        command_id: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        act_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
        deduplication_duration: Optional[TimeDeltaLike] = ...,
        deduplication_offset: Optional[str] = ...,
    ) -> ArchiveEvent: ...
    async def get_ledger_end(self, *, timeout: Optional[TimeDeltaLike] = ...) -> str: ...
    def query(
        self,
        __template_id: Union[str, TypeConName] = "*",
        __query: Query = None,
        *,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def query_many(
        self,
        *queries: Queries,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def stream(
        self,
        __template_id: Union[str, TypeConName] = "*",
        __query: Query = None,
        *,
        offset: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    def stream_many(
        self,
        *queries: Queries,
        offset: Optional[str] = None,
        read_as: Union[None, Party, Collection[Party]] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> QueryStream: ...
    async def get_user(
        self, user_id: Optional[str] = None, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> User: ...
    async def create_user(
        self,
        user: User,
        rights: Optional[Sequence[Right]] = ...,
        *,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> User: ...
    async def list_users(self, *, timeout: Optional[TimeDeltaLike] = ...) -> Sequence[User]: ...
    async def list_user_rights(
        self, user_id: Optional[str] = None, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Sequence[Right]: ...
    async def allocate_party(
        self,
        *,
        identifier_hint: Optional[str] = None,
        display_name: Optional[str] = None,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> PartyInfo: ...
    async def list_known_parties(
        self, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> Sequence[PartyInfo]: ...
    async def get_version(self, *, timeout: Optional[TimeDeltaLike] = ...) -> Version: ...
    async def upload_package(
        self, contents: bytes, *, timeout: Optional[TimeDeltaLike] = ...
    ) -> None: ...
    async def get_metering_report(
        self,
        from_: datetime,
        to: Optional[datetime] = None,
        application_id: Optional[str] = None,
        *,
        timeout: Optional[TimeDeltaLike] = ...,
    ) -> MeteringReport: ...

# PyCharm doesn't know what to make of these overloads with respect to the parent protocol,
# but mypy understands that these type signatures do not conflict with the parent base class
# noinspection PyProtocol,PyMethodOverriding
@runtime_checkable
class QueryStream(_QueryStream, Protocol):
    @overload
    def on_create(self) -> ACreateDecorator: ...
    @overload
    def on_create(self, __fn: CreateFn) -> CreateFn: ...
    @overload
    def on_create(self, __fn: ACreateFn) -> ACreateFn: ...
    @overload
    def on_create(self, __name: Union[str, TypeConName]) -> ACreateDecorator: ...
    @overload
    def on_create(self, __name: Union[str, TypeConName], __fn: CreateFn) -> CreateFn: ...
    @overload
    def on_create(self, __name: Union[str, TypeConName], __fn: ACreateFn) -> ACreateFn: ...
    @overload
    def on_archive(self) -> AArchiveDecorator: ...
    @overload
    def on_archive(self, __fn: ArchiveFn) -> ArchiveFn: ...
    @overload
    def on_archive(self, __fn: AArchiveFn) -> AArchiveFn: ...
    @overload
    def on_archive(self, __name: Union[str, TypeConName]) -> AArchiveDecorator: ...
    @overload
    def on_archive(self, __name: Union[str, TypeConName], __fn: ArchiveFn) -> ArchiveFn: ...
    @overload
    def on_archive(self, __name: Union[str, TypeConName], __fn: AArchiveFn) -> AArchiveFn: ...
    @overload
    def on_boundary(self) -> ABoundaryDecorator: ...
    @overload
    def on_boundary(self, __fn: BoundaryFn) -> BoundaryFn: ...
    @overload
    def on_boundary(self, __fn: ABoundaryFn) -> ABoundaryFn: ...
    def creates(self) -> AsyncIterator[CreateEvent]: ...
    def events(self) -> AsyncIterator[Union[CreateEvent, ArchiveEvent]]: ...
    def items(self) -> AsyncIterator[Union[CreateEvent, ArchiveEvent, Boundary]]: ...
    def __aiter__(self) -> AsyncIterator[Union[CreateEvent, ArchiveEvent, Boundary]]: ...
    async def run(self) -> None: ...
    async def close(self) -> None: ...
    async def __aenter__(self: QSSelf) -> QSSelf: ...
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None: ...

class QueryStreamBase(QueryStream, abc.ABC):
    @property
    def _callbacks(self) -> DefaultDict[str, List[Callable]]: ...
    @abc.abstractmethod
    def items(self): ...
    async def _emit(self, name: str, obj: Any) -> None: ...
    async def _emit_create(self, event: CreateEvent) -> None: ...
    async def _emit_archive(self, event: ArchiveEvent) -> None: ...
    async def _emit_boundary(self, event: Boundary) -> None: ...
