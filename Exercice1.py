class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print('Name : ', self.name)
        print('Balance :', self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self._isbn = isbn
        self._title = title
        self._author = author
        self._publisher = publisher
        self._pages = pages
        self._price = price
        self._copies = copies

    def display_info(self):
        print(self._title)
        print(f'ISBN : {self._isbn}')
        print(f'Price : {self._price}$')
        print(f'Number of copies : {self._copies}')
        print('.....')

    def in_stock(self):
        if 0 < self._copies:
            return True
        else:
            return False

    def sell(self):
        if self.in_stock():
            self._copies -= 1
        else:
            print('No more stock for ', self._isbn)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 50 <= new_price <= 1000:
            self._price = new_price
        else:
            raise ValueError('Price must be between 50 and 1000')


book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry', 'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)


book_list = [book1, book2, book3, book4]
[(x.display_info()) for x in book_list]


class Fraction:
    def __init__(self, nr, dr=1):
        if dr < 0:
            dr = -dr
            nr = -nr
        self.nr = nr
        self.dr = dr

    def show(self):
        print(self.nr, '/', self.dr)

    def multiply(self, fraction):
        if isinstance(fraction, int):
            fraction = Fraction(fraction, 1)
        return Fraction(self.nr * fraction.nr, self.dr * fraction.dr)

    def add(self, nbr):
        if isinstance(nbr, int):
            nbr = Fraction(nbr, 1)
        return Fraction((self.nr * nbr.dr + self.dr * nbr.nr), (self.dr * nbr.dr))


f1 = Fraction(2, 3)
f1.show()

f2 = Fraction(3, 4)
f2.show()

f3 = f1.multiply(f2)
f3.show()

f3 = f1.add(f2)
f3.show()

f3 = f1.add(5)
f3.show()

f3 = f1.multiply(5)
f3.show()


class Product:
    def __init__(self, pid, marked_price, discount):
        self.pid = pid
        self.marked_price = marked_price
        self._discount = discount

    def display(self):
        print(self.pid, self.marked_price, self._discount)

    @property
    def selling_price(self):
        return self.marked_price - (self.marked_price * (self._discount / 100))

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = value


p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

print(p1.pid, p1.selling_price)
print(p2.pid, p2.selling_price)
print(p3.pid, p3.selling_price)
print(p4.pid, p4.selling_price)


class Circle:



    def __init__(self, radius):
        self.radius = radius
        self._diameter = self.radius * 2
        self._circumference = self.radius * 2 * 3.14
        self._area = self.radius * self.radius * 3.14

    @property
    def radius(self):
        return self.radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius > 0:
            self.radius = new_radius
        else:
            raise ValueError('Radius cannot be under zero')
