# This file will serve as random stuff to practice git merge conflicts and branching with.

class Test:

    def test(self):
        print ('hi')


class Product():

    def make_product(self):
        print('I made a product')


class Talapas():

    def where_am_i(self):
        print("I'm on Talapas")

x = Test()
y = Test()

x.test()
y.test()

z = Test()

z.test()
z.test()
z.test()
z.test()
x.test()

t = Product()

t.make_product()
