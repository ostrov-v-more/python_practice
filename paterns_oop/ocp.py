# OCP = open for extension, closed from modification
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Peoduct:
    def __init__(self, name, color, size):
        self.size = size
        self.color = color
        self.name = name


class Specification:  # можно и без этого обойтись, но не понял зачем он нужен
    def is_satisfied(self, item):
        pass


class Filter:  # можно и без этого обойтись, но не понял зачем он нужен
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.agrs = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.agrs
        ))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Peoduct('Apple', Color.GREEN, Size.SMALL)
    tree = Peoduct('Tree', Color.GREEN, Size.LARGE)
    house = Peoduct('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    large = SizeSpecification(Size.LARGE)
    green_and_large = AndSpecification(green, large)

    # for p in bf.filter(products, green):
    #     print(p.name)

    for p in bf.filter(products, green_and_large):
        print(p.name)

