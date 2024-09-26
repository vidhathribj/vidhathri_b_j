#1.
a=int(input("Enter a: "))
b=int(input("Enter b: "))

print(a>10 and b>10)
print(a<5 or b<5)
print("First number is not greater than second")
print(not(a>b))

#2.
age=int(input("Enter age: "))
if age>=18:
  print("You are an adult")
elif age<18:
   print("You are a minor")

#3.
string=input("Enter a string: ")
print("a" in string)
print("Python" not in string)

#4.
a=4
b=2
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b>>1)



