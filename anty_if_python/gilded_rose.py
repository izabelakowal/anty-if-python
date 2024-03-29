from typing import List

from anty_if_python import inventory


class Item:
    def __init__(self, name: str, sell_in: int, quality: inventory.Quality) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GoodCategory:
    @staticmethod  # pragma: no mutate
    def build_for(item: Item) -> inventory.Good:
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return inventory.BackstagePass.build(item.sell_in)
        elif item.name == "Aged Brie":
            return inventory.AgedBrie.build(item.sell_in)
        else:
            return inventory.Generic.build(item.sell_in)


class GildedRose:
    def __init__(self, items: List[Item]) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            if not self.is_sulfuras(item):
                item.sell_in = item.sell_in - 1
                quality = inventory.Quality(item.quality)
                good = GoodCategory().build_for(item)
                good.update(quality)
                item.quality = quality.amount

    @staticmethod
    def is_sulfuras(item: Item) -> bool:
        return item.name == "Sulfuras, Hand of Ragnaros"
