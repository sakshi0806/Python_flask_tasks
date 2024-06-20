# OOPS concepts in Python
# ENCAPSULATON
'''Encapsualtion is one of the fundamental concepts in object-oriented programming (OOP). 
It does wrapping of data and functions (methods that work on data) in single unit (a capsule).'''

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine_status = 'off'

    def start_engine(self):
        self.engine_status = 'on'
        print('Engine started.')

    def stop_engine(self):
        self.engine_status = 'off'
        print('Engine stopped.')


# Creating an object of the Car class
my_car = Car('Toyota', 'Fortuner')
print(my_car.brand)
print(my_car.model)
my_car.start_engine()
print(my_car.engine_status)

# INHERITANCE
'''Inheritance allows a class (subclass) to inherit properties and behavior from another class (superclass). 
This promotes code reusability and establishes a hierarchy among classes.'''

class Vehicle:
  def __init__(self, brand, model):
      self.brand = brand
      self.model = model

  def display_info(self):
      print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
  def start_engine(self):
      print('Engine started.')

# Creating objects of the Vehicle and Car classes
my_vehicle = Vehicle('Honda', 'Civic')
my_car = Car('Toyota', 'Camry')

my_vehicle.display_info()  
my_car.display_info()  
my_car.start_engine()  

#POLYMORPHISM
'''Polymorphism allows objects of different classes to be treated as objects of a common superclass. 
It enables flexibility in how objects are used, as different classes can implement methods with the same name but different behaviors.'''

class Shape:
  def area(self):
      pass

class Rectangle(Shape):
  def __init__(self, length, width):
      self.length = length
      self.width = width

  def area(self):
      return self.length * self.width

class Circle(Shape):
  def __init__(self, radius):
      self.radius = radius

  def area(self):
      return 3.14 * self.radius * self.radius

# Creating objects of the Rectangle and Circle classes
my_rectangle = Rectangle(5, 4)
my_circle = Circle(3)

print("Area of rectangle:", my_rectangle.area())
print("Area of circle:", my_circle.area()) 