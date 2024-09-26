#Operators
#Assignment operators
x=input("Enter number: ")
x=int(x)
x+=2
print(int(x))
x-=4
print(int(x))
x*=6
print(int(x))
x/=2
print(int(x))

#Comparision operators
x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))

print(x==y)
print(x!=y)
print(x>y)
print(x<y)

#Logical operator
a=2
b=4

print(a>4 and b<4)
print(a>0 and b<4)
print(a>0 and b<54)

print(a>4 or b<4)
print(a>0 or b<4)
print(a>0 or b<5)
print(not(b<a))

#Membership Operators
#in and not in
print("Membership Operators")
string="Python"
print("P" in string)
print("P" not in string)

#Bitwise operator
a=3
b=4
print(a & b)
print(a|b)
print(~a)
print(a<<1)
print(a>>1)





