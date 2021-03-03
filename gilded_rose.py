# -*- coding: utf-8 -*-


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if (
                not self.is_aged_brie(item)
                and not self.is_backstage_pass(item)
            ):
                if item.quality > 0:
                    if not self.is_sulfuras(item):
                        self.decrease_quality(item)
            else:
                if self.quality_less_than_50(item):
                    self.increase_quality(item)
                    if self.is_backstage_pass(item):
                        if item.sell_in < 11:
                            if self.quality_less_than_50(item):
                                self.increase_quality(item)
                        if item.sell_in < 6:
                            if self.quality_less_than_50(item):
                                self.increase_quality(item)
            if not self.is_sulfuras(item):
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if not self.is_aged_brie(item):
                    if not self.is_backstage_pass(item):
                        if item.quality > 0:
                            if not self.is_sulfuras(item):
                                self.decrease_quality(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if self.quality_less_than_50(item):
                        self.increase_quality(item)

    def increase_quality(self, item):
        item.quality = item.quality + 1

    def decrease_quality(self, item):
        item.quality = item.quality - 1

    def quality_less_than_50(self, item):
        return item.quality < 50

    def is_aged_brie(self, item):
        return item.name == "Aged Brie"

    def is_backstage_pass(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
