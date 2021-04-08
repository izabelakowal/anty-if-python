from anty_if_course_code_python import inventory


class GoodCategory:
    @staticmethod
    def build_for(item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return inventory.BackstagePass.build(item.sell_in)
        elif item.name == "Aged Brie":
            return inventory.AgedBrie.build(item.sell_in)
        else:
            return inventory.Generic.build(item.sell_in)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if not self.is_sulfuras(item):
                item.sell_in = item.sell_in - 1
                quality = inventory.Quality(item.quality)
                good = GoodCategory().build_for(item)
                good.update(quality)
                item.quality = quality.amount

    @staticmethod
    def is_sulfuras(item):
        return item.name == "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
