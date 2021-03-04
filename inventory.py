
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
    def update(self, quality, sell_in):
        quality.degrade()
        if sell_in < 0:
            quality.degrade()


class AgedBrie:
    @staticmethod
    def build(sell_in):
        if sell_in < 0:
            return AgedBrie.Expired()
        else:
            return AgedBrie()

    class Expired:
        def update(self, quality, _):
            quality.increase()
            quality.increase()

    def update(self, quality, _):
        quality.increase()


class BackstagePass:
    def update(self, quality, sell_in):
        quality.increase()
        if sell_in < 10:
            quality.increase()
        if sell_in < 5:
            quality.increase()
            
        if sell_in < 0:
            quality.reset()
