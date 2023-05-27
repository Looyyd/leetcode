import functools
from os import system
from shlex import quote as shlex_quote


@functools.lru_cache(maxsize=128)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


print([fibonacci(n) for n in range(1, 100)])
