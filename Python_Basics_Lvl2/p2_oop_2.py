class Dog():
  
  # Class object attributes
  species = "Mammal"

  def __init__(self, breed, name):
    self.breed = breed
    self.name = name

  # Methods which use to manipulate or use attributes 

myDog = Dog();
print(type(myDog))
print(myDog.name)
print(myDog.breed)
print(myDog.species)
