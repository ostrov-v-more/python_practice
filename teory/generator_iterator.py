from collections.abc import Iterable

# генератор
def flatten(items: Iterable):
    for item in items:
        yield item
        if isinstance(item, Iterable):
            yield from flatten(item)
        else:
            yield item


items = [[0, 1, 2], 3, 4, [[5], [6, 7]], [[[8]]], 9]
print(list(flatten(items)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = flatten(items)
print(next(a))
print(next(a))
print(next(a))