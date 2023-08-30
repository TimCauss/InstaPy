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
        print(self._isbn, '-', self._title, '-', self._price, '$ -', self._copies)

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
        if 50 < new_price < 1000:
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
        self.nr = nr
        self.dr = dr

    def show(self):
        print(self.nr, '/', self.dr)

    def multiply(self, fraction):
        return Fraction(self.nr * fraction.nr, self.dr * fraction.dr)


f1 = Fraction(2, 3)
f1.show()

f2 = Fraction(3, 4)
f2.show()

f3 = f1.multiply(f2)
f3.show()
