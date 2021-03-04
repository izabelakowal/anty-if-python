
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
        self.quality = quality

    def update(self, sell_in):
        self.quality.degrade()
        if sell_in < 0:
            self.quality.degrade()


class AgedBrie:
    def __init__(self, quality):
        self.quality = quality

    @staticmethod
    def build(quality, sell_in):
        if sell_in < 0:
            return AgedBrie.Expired(quality)
        else:
            return AgedBrie(quality)

    class Expired:
        def __init__(self, quality):
            self.quality = quality

        def update(self, _):
            self.quality.increase()
            self.quality.increase()

    def update(self, sell_in):
        self.quality.increase()


class BackstagePass:
    def __init__(self, quality):
        self.quality = quality

    def update(self, sell_in):
        self.quality.increase()
        if sell_in < 10:
            self.quality.increase()
        if sell_in < 5:
            self.quality.increase()
            
        if sell_in < 0:
            self.quality.reset()
