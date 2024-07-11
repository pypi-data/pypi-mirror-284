from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from typing import TypeVar

from categories.data.semigroup import Semigroup
from categories.type import typeclass

__all__ = (
    'Monoid',
)


a = TypeVar('a')


@dataclass(frozen=True)
class Monoid(Semigroup[a], typeclass[a]):
    def empty(self, /) -> a:
        return self.concat([])

    def concat(self, xs : list[a], /) -> a:
        return reduce(self.append, xs, self.empty())
