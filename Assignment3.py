#Set union
a = {55,6,8,9,11}
b = {44,55,89,54}
print('Set union : ', a | b)

#Set is not allow duplicate item
#Example:
st = {1,2,3,4,5,3,4,2}
print(st)

#Print keys in dictionary
B={'Django': 16, 'Project': 8, 'Students': 20}
print(B.keys())

#Create a function & call the function.
def add_numbers(a, b):
    result = a + b
    return result

#Now call the function
num1 = 5
num2 = 7
sum_result = add_numbers(num1, num2)

print(f"The sum of {num1} and {num2} is {sum_result}")

#Create class and object

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Rongon", 22)
person2 = Person("Jim", 23)

person1.introduce()
person2.introduce()


#Inheritance Example:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


dog = Dog("Tommy")
cat = Cat("Pussy")


print(dog.speak())  
print(cat.speak())  
