#input
txt=input("This is first python program")
print(txt)

#indentation
x=1;
if x>0 :
 print("This is single space indentation")
 print("This is single space indentation")

#Spaces and tabs
x=1;
if x>0 :
    print("This statement has a single space+tab indentation")
    print("This statement has a single space+tab indentation")

#tab indentation
x=1;
if x>0 :
    print("This is single tab indentation")
    print("This is single tab indentation")

#multiple statements on a single line
print("Statement1"); print("Statement2")

#numbers
a = 1452
print(type (a))
b = (- 4587)
print(type (b))
c = 0
print(type (c))
g = 1
print(type (g))
h = - 11.23
print(type (h))
i = 0.34
print(type (i))
j = 2.122e-10
print(type (j))
k=5E220
print(type (k))

#Boolean
x = True
print(type (x))
y = False
print(type (y))

#Complex
x = complex (1,2)
print(x)
print(type (x))
z = 1+2j
print(z)
print(type (z))
z = 1+2J
print(z)
print(type (z))

#strings
str1="string1"
print(str1)
str2="string2"
print(str2)
str3="string3"
print(str3)

#String indicies
string1="PYTHON TUTORIAL"
print(string1 [0])
print(string1 [-15])
print(string1 [14])
print(string1 [-1])
print(string1 [4])
print(string1 [-11])
#print(string1 [16]) string index out of range

#Special characters in strings 
print("this is a backslash (\\) mark")
print ("this is a tab \t key")
print("these are \'single quotes\'")
print("these are \"double quotes\"")
print("this is a new line \n New line")

#list
my_list1 = [5, 12, 13, 14] # the list contains all integer values
print (my_list1)
print(type(my_list1))
my_list2 = ['red', 'blue', 'black', 'white'] # the list contains all string values
print(my_list2)
my_list3 = ['red', 12, 112.12] # the list contains a string, an intger and a float values
print(my_list3)

#list indicies
color_list=["RED", "Blue", "Green", "Black"] # The List have four elements indices start at 0 and end at 3
print(color_list [0])# Return the First Element
print (color_list[0], color_list[3]) # Print First and Last Elements
print(color_list[-1]) # Return Last Element
#print(color_list[4]) list index out of range

#list slices
color_list=["RED", "Blue", "Green", "Black"] # The List have four elements indices start at 0 and end at 3

print (color_list [0:2]) 
# cut first two items
print (color_list[1:2]) # Cut second item 
print (color_list [1:-2]) # Cut second item
print (color_list[:3]) # Cut first three items
print (color_list[:]) # Creates copy of original list
