# SPDX-License-Identifier: BSD-3-Clause
# Copyright (c) 2023 Scipp contributors (https://github.com/scipp)
"""Tools for handling statistical uncertainties."""

from typing import TypeVar, Union, overload

import scipp as sc

T = TypeVar("T", bound=Union[sc.Variable, sc.DataArray])


@overload
def broadcast_with_upper_bound_variances(
    data: sc.Variable, sizes: dict[str, int]
) -> sc.Variable:
    pass


@overload
def broadcast_with_upper_bound_variances(
    data: sc.DataArray, sizes: dict[str, int]
) -> sc.DataArray:
    pass


def broadcast_with_upper_bound_variances(
    data: Union[sc.Variable, sc.DataArray], sizes: dict[str, int]
) -> Union[sc.Variable, sc.DataArray]:
    if _no_variance_broadcast(data, sizes):
        return data
    size = 1
    for dim, dim_size in sizes.items():
        if dim not in data.dims:
            size *= dim_size
    data = data.copy()
    data.variances *= size
    return data.broadcast(sizes={**sizes, **data.sizes}).copy()


def drop_variances_if_broadcast(
    data: Union[sc.Variable, sc.DataArray], sizes: dict[str, int]
) -> Union[sc.Variable, sc.DataArray]:
    if _no_variance_broadcast(data, sizes):
        return data
    return sc.values(data)


def _no_variance_broadcast(
    data: Union[sc.Variable, sc.DataArray], sizes: dict[str, int]
) -> bool:
    return (data.variances is None) or all(
        data.sizes.get(dim) == size for dim, size in sizes.items()
    )
