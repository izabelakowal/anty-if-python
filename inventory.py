
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


class Generic:
    def __init__(self, quality):
        self._quality = Quality(quality)

    @property
    def quality(self):
        return self._quality.amount

    def update(self, sell_in):
        self._quality.degrade()
        if sell_in < 0:
            self._quality.degrade()


class AgedBrie:
    def __init__(self, quality):
        self._quality = Quality(quality)

    @property
    def quality(self):
        return self._quality.amount

    def update(self, sell_in):
        self._quality.increase()
        if sell_in < 0:
            self._quality.increase()


class BackstagePass:
    def __init__(self, quality):
        self._quality = Quality(quality)

    @property
    def quality(self):
        return self._quality.amount

    def update(self, sell_in):
        self._quality.increase()
        if sell_in < 10:
            self._quality.increase()
        if sell_in < 5:
            self._quality.increase()
            
        if sell_in < 0:
            self._quality.reset()
