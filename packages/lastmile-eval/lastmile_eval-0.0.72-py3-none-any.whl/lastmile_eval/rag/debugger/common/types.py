"""
Utils file for defining types used in the tracing SDK
"""

from dataclasses import dataclass
from typing import (
    NewType,
    Optional,
    ParamSpec,
    TypeVar,
)
from enum import Enum
from result import Result


T_ParamSpec = ParamSpec("T_ParamSpec")

APIToken = NewType("APIToken", str)
BaseURL = NewType("BaseURL", str)
ProjectID = NewType("ProjectID", str)
ProjectName = NewType("ProjectName", str)
CreatorID = NewType("CreatorID", str)
OrganizationID = NewType("OrganizationID", str)

T_cov = TypeVar("T_cov", covariant=True)
T_Inv = TypeVar("T_Inv")

Res = Result[T_cov, Exception]


@dataclass(frozen=True)
class ParsedHTTPResponse:
    returned_id: str
    status_code: int
    text: str


# FYI: kw_only is needed due to position args with default values
# being delcared before non-default args. This is only supported on
# python 3.10 and above
@dataclass(kw_only=True)
class Node:
    """Node used during ingestion"""

    id: str
    title: Optional[str] = None
    text: str


@dataclass(kw_only=True)
class RetrievedNode(Node):
    """Node used during retrieval that also adds a retrieval score"""

    score: float


@dataclass(kw_only=True)
class TextEmbedding:
    """Object used for storing text embedding info"""

    id: str
    title: Optional[str] = None
    text: str
    vector: list[float]


class RagFlowType(Enum):
    """
    Enum to define the type of flow that the RAG debugger is in.
    """

    INGESTION = "ingestion"
    QUERY = "query"
