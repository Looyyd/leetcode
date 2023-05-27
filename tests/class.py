from dataclasses import dataclass

def outer_function():
    x = 10

    def inner_function():
        def inner_inner_function():
            nonlocal x
            x += 5
            print("Inner inner function:", x)
        #nonlocal x
        inner_inner_function()
        print("Inner function:", x)

    inner_function()
    print("Outer function:", x)

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    def __init__(self):
        self.i = 54321

    def set_i(self, i):
        self.i = i


class MyInheritClass(MyClass):
    def __init__(self):
        self.i = 54321

    def set_i(self, i):
        self.i = i


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

@dataclass
class Employee:
    name: str
    age: int
    salary: float

def main() -> float:
    for char in reverse('golf'):
        print(char)

    name: str = "John"
    age: int = 25
    price: float

    print(name, age)
    price = {name: age}
    print(price)
    print("type of price:", type(price))

    return price



def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


if __name__ == '__main__':
    main()