# Inheritance

class Animal():

  def __init__(self):
    print("Animal Created")
  
  def whoAmI(self):
    print("Animal")

  def eat(self):
    print('EATING')

class Dog(Animal):

  def __init__(self):
    Animal.__init__(self)
    print("Dog Created")

  def bark(self):
    print("Wooof .... woooooof")

  def eat(self):
    print("Dog eat");    

myAnimal = Animal()
myAnimal.whoAmI()
myAnimal.eat()


myDog = Dog()
myDog.whoAmI()
myDog.bark()
myDog.eat();

# Special Methods

