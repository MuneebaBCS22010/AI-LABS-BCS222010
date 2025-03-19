# Python program to illustrate while loop
count = 0
while (count < 3):
 count = count + 1
 print("Hello Geek")

# Python program to illustrate Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
 print(i)

 # Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
 print(i)

 # Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s :
 print(i)

# Python program to illustrate Iterating by index
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
 print (list[index])

# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
 if letter == 'e' or letter == 's':
  continue
 print ('Current Letter:', letter)

print("break statement working")
for letter in 'geeksforgeeks':
    # break the loop as soon as it sees 'e' or 's'
    if letter == 'e' or letter == 's':
        break
    print('Current Letter:', letter)

print("Creating a function in python and calling it")
def my_function():
 print("Hello from a function")
my_function()

print("Use of default parameter in a funtion")
def my_function(country ="Norway"):
  print("I am from "+ country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print("How list of parameters work in a function:")
def my_function(food):
 for x in food:
  print(x)
fruits = ["apple", "banana", "cherry"] 
my_function(fruits)

print("Return statement in a function")
def my_function(x):
 return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

print("Key arguments in a function")
def my_function(child3, child2, child1):
 print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("Class and its objects in a python")
class MyClass: 
  x = 5
p1 = MyClass() 
print(p1.x)

print("__init__ Function")
class Person:
 def __init__ (self, name, age): 
   self.name = name
   self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

print("Object function")
class Person:
 def __init__ (self, name, age): 
  self.name = name
  self.age = age
 def myfunc(self):
  print("Hello my name is " + self.name)

p1 = Person("John", 36) 
p1.myfunc()