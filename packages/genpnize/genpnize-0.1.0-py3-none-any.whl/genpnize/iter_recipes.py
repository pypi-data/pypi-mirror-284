from __future__ import annotations

from collections.abc import Generator, Iterable
from itertools import zip_longest
from typing import TypeVar, overload

T = TypeVar("T")


@overload
def grouper(
    iterable: Iterable[T], n: int, fillvalue: T
) -> Generator[tuple[T], None, None]: ...


@overload
def grouper(
    iterable: Iterable[T], n: int, fillvalue: None = None
) -> Generator[tuple[T | None], None, None]: ...


def grouper(
    iterable: Iterable[T], n: int, fillvalue: T | None = None
) -> Generator[tuple[T | None], None, None]:
    """Based on `grouper` in `the itertools recipes section <https://docs.python.org/3/library/itertools.html#itertools-recipes>`__.

    >>> list(grouper("ABCDEFG", 3))
    [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', None, None)]
    >>> list(grouper("ABCDEFG", 3, fillvalue="x"))
    [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]
    """  # NOQA: E501
    iterators = [iter(iterable)] * n
    yield from zip_longest(*iterators, fillvalue=fillvalue)
