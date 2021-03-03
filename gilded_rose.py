# -*- coding: utf-8 -*-


class Generic:
    def __init__(self, quality, sell_in):
        self.quality = quality
        self.sell_in = sell_in

    def update(self):
        if self.quality > 0:
            self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality > 0:
                self.quality = self.quality - 1
                

class AgedBrie:
    def __init__(self, quality, sell_in):
        self.quality = quality
        self.sell_in = sell_in

    def update(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality < 50:
                self.quality = self.quality + 1
                
                
class Sulfuras:
    def __init__(self, quality, sell_in):
        self.quality = quality
        self.sell_in = sell_in

    def update(self):
        pass
                
                
class BackstagePass:
    def __init__(self, quality, sell_in):
        self.quality = quality
        self.sell_in = sell_in

    def update(self):
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality = self.quality + 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = self.quality - self.quality


class GoodCategory:
    def build_for(self, item):
        if self.is_sulfuras(item):
            return Sulfuras(item.quality, item.sell_in)
        elif self.is_generic(item):
            return Generic(item.quality, item.sell_in)
        elif self.is_aged_brie(item):
            return AgedBrie(item.quality, item.sell_in)
        elif self.is_backstage_pass(item):
            return BackstagePass(item.quality, item.sell_in)

    def is_generic(self, item):
        return not (self.is_aged_brie(item) or self.is_backstage_pass(item) or self.is_sulfuras(item))

    def is_aged_brie(self, item):
        return item.name == "Aged Brie"

    def is_backstage_pass(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"

    def is_sulfuras(self, item):
        return item.name == "Sulfuras, Hand of Ragnaros"
    

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            good = GoodCategory().build_for(item)
            good.update()
            item.quality = good.quality
            item.sell_in = good.sell_in


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
