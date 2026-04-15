#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):
    pass

    @abstractmethod
    def heal(self, target: Creature) -> str:
        pass


class TransformCapability(ABC):
    pass

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
