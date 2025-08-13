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

class Book():

  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self):
    return "Title: {}, Author: {}, Page: {}".format(self.title, self.author, self.pages)
  
  def __len__(self):
    return self.pages;

  def __del__(self):
    print("Book has been destroy")

book = Book("Python", "Manish", 200)
print(book);
print(len(book));
del book;

my_list = [1,2,3,4]
print(my_list)

