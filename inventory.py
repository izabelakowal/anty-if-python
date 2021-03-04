
class Quality:
    def __init__(self, amount):
        self.amount = amount

    def degrade(self):
        if self.amount > 0:
            self.amount = self.amount - 1

    def increase(self):
        if self.amount < 50:
            self.amount = self.amount + 1

    def reset(self):
        self.amount = 0

    def is_less_than_50(self):
        return self.amount < 50


class Generic:
    def __init__(self, quality, sell_in):
        self._quality = Quality(quality)
        self.sell_in = sell_in

    @property
    def quality(self):
        return self._quality.amount

    def update(self):
        self._quality.degrade()
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self._quality.degrade()


class AgedBrie:
    def __init__(self, quality, sell_in):
        self._quality = Quality(quality)
        self.sell_in = sell_in

    @property
    def quality(self):
        return self._quality.amount

    def update(self):
        self._quality.increase()
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self._quality.increase()


class BackstagePass:
    def __init__(self, quality, sell_in):
        self._quality = Quality(quality)
        self.sell_in = sell_in

    @property
    def quality(self):
        return self._quality.amount

    def update(self):
        self._quality.increase()
        if self._quality.is_less_than_50():
            if self.sell_in < 11:
                self._quality.increase()
            if self.sell_in < 6:
                self._quality.increase()
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self._quality.reset()
