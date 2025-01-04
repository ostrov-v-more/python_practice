import functools

def start_finish_decorator(func):
    def _wrapper(*args, **kwargs):
        print('Start')
        print(f"Result {func(*args,**kwargs)}")
        print("Finish")
        return func(*args,**kwargs)
    return _wrapper


"""
Использование декоратора аналогично вызову
summ = start_finish_decorator(summ)
summ(10, 12)
"""


@start_finish_decorator
def summ(a: int, b: int) -> int:
    return a + b


re_1 = summ(10, 12)


"""
Для передачи в декораторе параметров нужно обернуть еще одной функцией.
Использование аналогично вызову
summ = text_decorator("текст")(summ)
summ(10, 12)
"""


def text_decorator(text=""):
    def _decorator(func):
        def _wrapper(*args, **kwargs):
            print(f'Start {text}')
            print(f"Result {func(*args, **kwargs)}")
            print(f"Finish {text}")
            return func(*args, **kwargs)

        return _wrapper
    return _decorator


@text_decorator("вычисления")
def summ(a: int, b: int) -> int:
    return a + b


summ(10, 13 )

"""
Декоратор считает время выполнения функции
"""


def benchmark(func):
    @functools.wraps(func)  # необходимо, чтоб при обращении к задекорированной функции через __name__
    # возвращалось имя задекорированной функции, а не _wrapper
    def _wrapper(*args, **kwargs):
        from datetime import datetime
        start = datetime.now()
        print(f"Start in {start}")
        result = func(*args, **kwargs)
        finish = datetime.now()
        print(f"Finish in {finish}")
        print(f"time: {finish - start}")
        return result
    return _wrapper


@benchmark
def summ(a: int, b: int) -> int:
    return a + b


# summ(12, 20)

print(summ.__name__)