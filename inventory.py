
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
    @staticmethod
    def build(sell_in):
        if sell_in < 0:
            return Generic.Expired()
        else:
            return Generic()

    class Expired:
        def update(self, quality):
            quality.degrade()
            quality.degrade()

    def update(self, quality):
        quality.degrade()



class AgedBrie:
    @staticmethod
    def build(sell_in):
        if sell_in < 0:
            return AgedBrie.Expired()
        else:
            return AgedBrie()

    class Expired:
        def update(self, quality):
            quality.increase()
            quality.increase()

    def update(self, quality):
        quality.increase()


class BackstagePass:
    @staticmethod
    def build(sell_in):
        if sell_in < 0:
            return BackstagePass.Expired()
        elif sell_in < 5:
            return BackstagePass.LessThan5Days()
        elif sell_in < 10:
            return BackstagePass.LessThan10Days()
        else:
            return BackstagePass()

    def update(self, quality):
        quality.increase()

    class Expired:
        def update(self, quality):
            quality.reset()

    class LessThan5Days:
        def update(self, quality):
            quality.increase()
            quality.increase()
            quality.increase()

    class LessThan10Days:
        def update(self, quality):
            quality.increase()
            quality.increase()

