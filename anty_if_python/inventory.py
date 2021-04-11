from __future__ import annotations
from abc import ABC, abstractmethod


class Quality:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def degrade(self) -> None:
        if self.amount > 0:
            self.amount = self.amount - 1

    def increase(self) -> None:
        if self.amount < 50:
            self.amount = self.amount + 1

    def reset(self) -> None:
        self.amount = 0


class Good(ABC):
    @abstractmethod  # pragma: no mutate
    def update(self, quality: Quality) -> None:
        pass


class Generic(Good):
    @staticmethod
    def update(quality: Quality) -> None:
        quality.degrade()

    @staticmethod  # pragma: no mutate
    def build(sell_in: int) -> Generic:
        if sell_in < 0:
            return Generic.Expired()
        else:
            return Generic()

    class Expired(Good):
        @staticmethod
        def update(quality: Quality) -> None:
            quality.degrade()
            quality.degrade()


class AgedBrie(Good):
    @staticmethod
    def update(quality: Quality) -> None:
        quality.increase()

    @staticmethod  # pragma: no mutate
    def build(sell_in: int) -> AgedBrie:
        if sell_in < 0:
            return AgedBrie.Expired()
        else:
            return AgedBrie()

    class Expired(Good):
        @staticmethod
        def update(quality: Quality) -> None:
            quality.increase()
            quality.increase()


class BackstagePass(Good):
    @staticmethod
    def update(quality):
        quality.increase()

    @staticmethod  # pragma: no mutate
    def build(sell_in: int) -> BackstagePass:
        if sell_in < 0:
            return BackstagePass.Expired()
        elif sell_in < 5:
            return BackstagePass.LessThan5Days()
        elif sell_in < 10:
            return BackstagePass.LessThan10Days()
        else:
            return BackstagePass()

    class Expired(Good):
        @staticmethod
        def update(quality: Quality) -> None:
            quality.reset()

    class LessThan5Days(Good):
        @staticmethod
        def update(quality: Quality) -> None:
            quality.increase()
            quality.increase()
            quality.increase()

    class LessThan10Days(Good):
        @staticmethod
        def update(quality: Quality) -> None:
            quality.increase()
            quality.increase()
