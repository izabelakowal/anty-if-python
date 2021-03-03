
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