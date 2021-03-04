# -*- coding: utf-8 -*-
import inventory


class GoodCategory:
    def build_for(self, item, quality: inventory.Quality):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return inventory.BackstagePass(quality)
        elif item.name == "Aged Brie":
            return inventory.AgedBrie.build(quality, item.sell_in)
        else:
            return inventory.Generic(quality)
    

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if not self.is_sulfuras(item):
                item.sell_in = item.sell_in - 1
                quality = inventory.Quality(item.quality)
                good = GoodCategory().build_for(item, quality)
                good.update(item.sell_in)
                item.quality = quality.amount

    def is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
