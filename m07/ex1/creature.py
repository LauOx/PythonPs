#!/usr/bin/env python3

from ex0.creature import Creature
from .capability import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """"""
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self):
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        """"""
        return f"{self.name} heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    """"""
    def __init__(self) -> None:
        super().__init__("Blomelle", "Grass")

    def attack(self):
        return f"{self.name}  uses Petal Dance!"

    def heal(self) -> str:
        """"""
        return f"{self.name} heals itself for a small amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")

    def attack(self):
        return f"{self.name} performs a boosted strike!"

    def transform(self):
        return f"{self.name} shifts into a sharper form!"

    def revert(self):
        return f"{self.name} returns to normal"


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self):
        return f"{self.name} unleashes a devastating morph strike!"

    def transform(self):
        return f"{self.name} dragonic battle form"

    def revert(self):
        return f"{self.name} stabilizes its form"
