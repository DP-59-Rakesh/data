# encapsulation

class TV:
    def __init__(self):
        self.__brand=None
    def set_brand(self,brand):
        self.__brand=brand
    def get_brand(self):
        return self.__brand

tv=TV()
tv.set_brand("LG")
print(tv._TV__brand)
print(tv.get_brand())   




#  Polymorphism (Overloading & Overriding)

# ---------------method overloading--------------
class cal:
    def add(self,a,b,c=0):
        print(a+b+c)
c=cal()        
c.add(10,20)
c.add(10,20,30)


class call:
    def add(self,*args):
        print(args)
        if len(args)==2:
            print(args[0]+args[1])
        elif len(args)==3:
            print(args[0]+args[1]+args[2])


cc=call()
cc.add(10,20)
cc.add(10,20,30)

# from functools import singledispatch
# class cal:
#     @singledispatch
#     def add(self,a):
#         print("unsoported data")
#     @add.register    
#     def _(self,a:int,b:int):
#         return a+b
#     @add.register    
#     def _(self,a:int,b:int,c:int):
#         return a+b+c
# a=cal()
# print(a.add(10,20))
# print(a.add(10,20,30) )  
  


# from functools import singledispatchmethod

# class Calculator:
#     @singledispatchmethod
#     def add(self, a:int, b: int):
#         """Add two integers."""
#         print(a+b)

#     @add.register
#     def _(self, a: int, b: int, c: int):
#         """Add three integers."""
#         print(a + b + c)

#     @add.register
#     def _(self, a: float, b: float):
#         """Add two floats."""
#         print(a + b)

# # Usage
# calc = Calculator()
# calc.add(10, 20)       # Calls the two-integer version
# calc.add(10, 20, 30)   # Calls the three-integer version
# calc.add(1.5, 2.5)      # Calls the two-float version




from functools import singledispatch

@singledispatch
def process(data):
    """Default implementation for unsupported types"""
    print(f"Processing generic data: {data}")

@process.register(str)
def _(data):
    print(f"Processing string: {data.upper()}")

@process.register(list)
def _(data):
    print(f"Processing list: {', '.join(map(str, data))}")

@process.register(int)
def _(data):
    print(f"Processing integer: {data * 2}")

# Usage
process("hello")       # Calls string version
process([1, 2, 3])     # Calls list version
process(2)           # Calls integer version
process(3.14)          # Calls default version






#----------------- method overriding------------


class animals:
    def sound(self):
        print("animal makes sounds")
class dog(animals)  :
    def sound(self) :
        print('dog barks') 
a=animals()
a.sound()
d=dog() 
d.sound()       





# ----------------inheretance-------------



class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print(f"{self.brand} is honking...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Inheriting brand from Vehicle
        self.model = model

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Usage
car = Car("Ford", "Mustang")
car.honk()         # Inherited method
car.display()      # Child class method







# ------------abstraction------------------

from abc import ABC, abstractmethod

class Animal(ABC):
    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Usage
dog = Dog()
dog.sound()  # Calls implemented abstract method
dog.sleep()  # Calls non-abstract method from Animal class




# -----------------static method----------------



# Static Method Example
# Static methods do not modify class or instance state.
# They are defined using the @staticmethod decorator.
# They behave like regular functions but belong to the class’s namespace and can be called without creating an instance.
# we can call static method using object also


class Math:
    def __init__(self,c):
        self.c=c
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
    def sub(self,a,b):
        print(a+b+self.c)

# Usage
m=Math(10)
print(Math.add(5, 3))       # Output: 8
print(Math.multiply(4, 7))  # Output: 28
m.sub(20,10)




# -------------Class Method Example---------------------




# Class methods operate on the class itself and are defined with the @classmethod decorator.
# They take cls as the first parameter, referring to the class.




class Vehicle:
    wheels = 0  # Class attribute

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_wheels(cls, num):
        cls.wheels = num

    @classmethod
    def from_name(cls, name):
        return cls(name)

# Usage
print(Vehicle.wheels)
Vehicle.set_wheels(4)  # Set class-level attribute
print(f"Vehicle has {Vehicle.wheels} wheels")  # Output: Vehicle has 4 wheels

car = Vehicle.from_name("Car")  # Create an instance using class method
print(f"Created vehicle: {car.name}")  # Output: Created vehicle: Car
