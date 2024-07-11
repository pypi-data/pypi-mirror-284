from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Mapping, Tuple, TypedDict, Union

import pandas as pd
import polars as pl

if TYPE_CHECKING:
    import sys

    if sys.version_info >= (3, 10):
        from typing import TypeAlias

        from typing_extensions import TypeIs
    else:
        from typing_extensions import TypeAlias, TypeIs


MedRecordAttribute: TypeAlias = Union[str, int]
MedRecordAttributeInputList: TypeAlias = Union[
    List[str], List[int], List[MedRecordAttribute]
]
MedRecordValue: TypeAlias = Union[str, int, float, bool, None]
NodeIndex: TypeAlias = MedRecordAttribute
NodeIndexInputList: TypeAlias = MedRecordAttributeInputList
EdgeIndex: TypeAlias = int
EdgeIndexInputList: TypeAlias = List[EdgeIndex]
Group: TypeAlias = MedRecordAttribute
GroupInputList: TypeAlias = MedRecordAttributeInputList
Attributes: TypeAlias = Dict[MedRecordAttribute, MedRecordValue]
AttributesInput: TypeAlias = Union[
    Mapping[MedRecordAttribute, MedRecordValue],
    Mapping[str, MedRecordValue],
    Mapping[int, MedRecordValue],
]
NodeTuple: TypeAlias = Union[
    Tuple[str, AttributesInput],
    Tuple[int, AttributesInput],
    Tuple[NodeIndex, AttributesInput],
]
EdgeTuple: TypeAlias = Union[
    Tuple[str, str, AttributesInput],
    Tuple[str, int, AttributesInput],
    Tuple[str, NodeIndex, AttributesInput],
    Tuple[int, str, AttributesInput],
    Tuple[int, int, AttributesInput],
    Tuple[int, NodeIndex, AttributesInput],
    Tuple[NodeIndex, str, AttributesInput],
    Tuple[NodeIndex, int, AttributesInput],
    Tuple[NodeIndex, NodeIndex, AttributesInput],
]
PolarsNodeDataFrameInput: TypeAlias = Tuple[pl.DataFrame, str]
PolarsEdgeDataFrameInput: TypeAlias = Tuple[pl.DataFrame, str, str]
PandasNodeDataFrameInput: TypeAlias = Tuple[pd.DataFrame, str]
PandasEdgeDataFrameInput: TypeAlias = Tuple[pd.DataFrame, str, str]


class GroupInfo(TypedDict):
    nodes: List[NodeIndex]
    edges: List[EdgeIndex]


def is_medrecord_attribute(value: object) -> TypeIs[MedRecordAttribute]:
    return isinstance(value, (str, int))


def is_medrecord_value(value: object) -> TypeIs[MedRecordValue]:
    return isinstance(value, (str, int, float, bool)) or value is None


def is_node_index(value: object) -> TypeIs[NodeIndex]:
    return is_medrecord_attribute(value)


def is_edge_index(value: object) -> TypeIs[EdgeIndex]:
    return isinstance(value, int)


def is_group(value: object) -> TypeIs[Group]:
    return is_medrecord_attribute(value)


def is_attributes(value: object) -> TypeIs[Attributes]:
    return isinstance(value, dict)


def is_node_tuple(value: object) -> TypeIs[NodeTuple]:
    return (
        isinstance(value, tuple)
        and len(value) == 2
        and is_medrecord_attribute(value[0])
        and is_attributes(value[1])
    )


def is_node_tuple_list(value: object) -> TypeIs[List[NodeTuple]]:
    return isinstance(value, list) and all(is_node_tuple(input) for input in value)


def is_edge_tuple(value: object) -> TypeIs[EdgeTuple]:
    return (
        isinstance(value, tuple)
        and len(value) == 3
        and is_medrecord_attribute(value[0])
        and is_medrecord_attribute(value[1])
        and is_attributes(value[2])
    )


def is_edge_tuple_list(value: object) -> TypeIs[List[EdgeTuple]]:
    return isinstance(value, list) and all(is_edge_tuple(input) for input in value)


def is_polars_node_dataframe_input(
    value: object,
) -> TypeIs[PolarsNodeDataFrameInput]:
    return (
        isinstance(value, tuple)
        and len(value) == 2
        and isinstance(value[0], pl.DataFrame)
        and isinstance(value[1], str)
    )


def is_polars_node_dataframe_input_list(
    value: object,
) -> TypeIs[List[PolarsNodeDataFrameInput]]:
    return isinstance(value, list) and all(
        is_polars_node_dataframe_input(input) for input in value
    )


def is_polars_edge_dataframe_input(
    value: object,
) -> TypeIs[PolarsEdgeDataFrameInput]:
    return (
        isinstance(value, tuple)
        and len(value) == 3
        and isinstance(value[0], pl.DataFrame)
        and isinstance(value[1], str)
        and isinstance(value[2], str)
    )


def is_polars_edge_dataframe_input_list(
    value: object,
) -> TypeIs[List[PolarsEdgeDataFrameInput]]:
    return isinstance(value, list) and all(
        is_polars_edge_dataframe_input(input) for input in value
    )


def is_pandas_node_dataframe_input(
    value: object,
) -> TypeIs[PandasNodeDataFrameInput]:
    return (
        isinstance(value, tuple)
        and len(value) == 2
        and isinstance(value[0], pd.DataFrame)
        and isinstance(value[1], str)
    )


def is_pandas_node_dataframe_input_list(
    value: object,
) -> TypeIs[List[PandasNodeDataFrameInput]]:
    return isinstance(value, list) and all(
        is_pandas_node_dataframe_input(input) for input in value
    )


def is_pandas_edge_dataframe_input(
    value: object,
) -> TypeIs[PandasEdgeDataFrameInput]:
    return (
        isinstance(value, tuple)
        and len(value) == 3
        and isinstance(value[0], pd.DataFrame)
        and isinstance(value[1], str)
        and isinstance(value[2], str)
    )


def is_pandas_edge_dataframe_input_list(
    value: object,
) -> TypeIs[List[PandasEdgeDataFrameInput]]:
    return isinstance(value, list) and all(
        is_pandas_edge_dataframe_input(input) for input in value
    )
