class Animal():

    def __init__(self,fur):
        self.fur = fur
        print('Animal Created')

    def report(self):
        print('Animal')

    def eat(self):
        print('Eating!')




class Dog(Animal):

    def __init__(self,fur):
        Animal.__init__(self,fur)
        print('Dog Created')

    def report(self):
        print('ı am a dog')


d = Dog('Fuzzy')
d.eat()
d.report()
