#program 1
for i in range(1500,2700):
 if i%7==0 and i%5==0:
  print(i)

#program 2
celsius=float(input("Give temperature in celsius:"))
farenheit=(celsius*(9/5))+32
print("Temperature in Fahrenheit is", farenheit)

farenheit=float(input("Give temperature in farenheit:"))
celsius=(farenheit-32)*5/9
print("Temperature in celsius is", int(celsius))
 
#program3
import random
number = random.randint(1,9) 
print(number)
guess=int(input("Enter your guessed number:"))
while(guess!=number):
 print("you entered a wrong guess")
 guess=int(input("guess number again"))
print("Well guessed")

#program4
for i in range(1, 6):
    for j in range(1,i+1):

        print("*",end=" ")
    # Printing inside the outer loop
    print()
for i in range(1, 5):
    for j in range(4,i-1,-1):

        print("*",end=" ")
    # Printing inside the outer loop
    print()

#program5
text=input("Enter a word: ")
reversed_string=text[::-1]
print(reversed_string)

#program6
mylist=(7,8,9,5,4)
e=0
o=0
for i in mylist:
   if i%2==0:
      e=e+1
   else:
      o=o+1
print("Total even numbers are:", e)
print("Total odd numbers are:" , o)

#program7
mylist=[1452,11.23,1+2j,True,'w3resource',(0,-1),[5,12],{"class:"'V',"section:"'A'}]
for i in mylist:
   print(type(i))

#program8
for i in range(0,7):
   if(i==3 or i==6):
      continue
   else:
      print(i)

#program 9
start=0
end=50
b=1
while  start<=end:
    print(start,end=" ")
    start,b=b,start+b

#program 
for i in range(1,51):
    if i%3==0 and i%5==0:
       print("FizzBuzz")  
    elif i%3==0:
      print("Fizz")
    elif i%5==0:
      print("Buzz")
    else :
       print(i)  

#program 10
m=int(input(" Enter Row value"))
n=int(input(" Enter col Value"))
multi_list=[[0 for col in range(n)]for row in range(m)]
for row in range(m):
    for col in range(n):
        multi_list[row][col]=row*col

print(multi_list) 

#program 11
lines=[]
while True:
    l=input()
    if l:
        lines.append(l.lower())
    else:
        break    

for l in lines:
    print(l)

#program 12
binary_numbers = input("Enter comma-separated 4-digit binary numbers: ").split(',')
divisible_by_5 = []
for num in binary_numbers:
    if int(num, 2) % 5 == 0:
        divisible_by_5.append(num)
print(",".join(divisible_by_5))

#progarm 13
str=input()
count=0
l=0
for i in str:
    if i.isdigit():
        count=count+1
    elif i.isalpha():
        l=l+1
    else:
        pass    
print("Letters: ",l) 
print("Digits: ",count)   

# program 14
import re
p = input("Input your password")

x = True

while x:  
    
    if (len(p) < 6 or len(p) > 12):
        break
    
    elif not re.search("[a-z]", p):
        break
    
    elif not re.search("[0-9]", p):
        break
    
    elif not re.search("[A-Z]", p):
        break

    elif not re.search("[$#@]", p):
        break

    elif re.search("\s", p):
        break

    else:
        print("Valid Password")
        x = False
        break
if x:
    print("Not a Valid Password")
