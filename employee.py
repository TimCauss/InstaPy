class Product:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self, val):
        self._x = val

    @value.deleter
    def value(self):
        print('Value deleted')


p = Product(12, 24)
