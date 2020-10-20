class Dog():

#Class object attributes(same for every Dog instances)

    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


sam = Dog('Husky','Sammy')

print(sam.breed)
print(sam.name)
print(sam.species)
