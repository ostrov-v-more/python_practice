import time
from contextlib import contextmanager
from datetime import datetime


class Timer:
    def __enter__(self):
        self.start = datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.result = datetime.now() - self.start
        # так можно вывести ошибку при использовании менеджера контекста
        self.err_val = exc_val
        self.err_type = exc_type
        self.err_tb = exc_tb
        return self

    def __str__(self):
        return str(self.result)


with Timer() as t:
    time.sleep(1)
    raise Exception("Error_1")
    print("Hello")

# вытаскиваем ошибку
print(t.err_val, t.err_type, t.err_tb)


@contextmanager
def context_man(tme: int):
    time.sleep(tme)  # задержка перед выполнением контекста
    print("Start")
    try:
        yield
    except Exception as err:
        print(err)
    finally:
        print("Exit")


with context_man(1):
    print("Hello ")
    raise Exception("Error_1")
