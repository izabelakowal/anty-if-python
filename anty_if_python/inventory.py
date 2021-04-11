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
            return Generic().Expired()
        else:
            return Generic()

    class Expired:
        @staticmethod
        def update(quality):
            quality.degrade()
            quality.degrade()

    @staticmethod
    def update(quality):
        quality.degrade()


class AgedBrie:
    @staticmethod
    def build(sell_in):
        if sell_in < 0:
            return AgedBrie().Expired()
        else:
            return AgedBrie()

    class Expired:
        @staticmethod
        def update(quality):
            quality.increase()
            quality.increase()

    @staticmethod
    def update(quality):
        quality.increase()


class BackstagePass:
    @staticmethod
    def build(sell_in):
        if sell_in < 0:
            return BackstagePass().Expired()
        elif sell_in < 5:
            return BackstagePass().LessThan5Days()
        elif sell_in < 10:
            return BackstagePass().LessThan10Days()
        else:
            return BackstagePass()

    @staticmethod
    def update(quality):
        quality.increase()

    class Expired:
        @staticmethod
        def update(quality):
            quality.reset()

    class LessThan5Days:
        @staticmethod
        def update(quality):
            quality.increase()
            quality.increase()
            quality.increase()

    class LessThan10Days:
        @staticmethod
        def update(quality):
            quality.increase()
            quality.increase()
