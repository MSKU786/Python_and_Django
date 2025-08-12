class Circle():

  pi = 3.14

  def __init__(self, radius=1):
    self.radius = radius

  def area(self):
    return Circle.pi * self.radius * self.radius
  
  def set_radius(self, new_radius):
    self.radius = new_radius
  

myCircle = Circle(5)
print(myCircle.area());

myCircle.radius = 10;
print(myCircle.area());

myCircle.set_radius = 20;
print(myCircle.area());