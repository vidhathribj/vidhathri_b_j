#Tuples and Sets

gender=("Male","Female","Others")
print(type(gender))
print(len(gender))
print(gender[1])
print(gender[0::2])

#Adding element to tupple
b="Male V2"
new=gender+(b,)
print(new)

gender1=list(gender)
print(gender1)
gender1.append("Male V2")
print(gender1)

#Adding two tuples or concatenation

tuple1=(1,2,3)
tuple2=(4,5,6)
concatenated=tuple1+tuple2
print(concatenated)
#Tuple repetition
repeat=tuple1 *3
print(repeat)

#Checking membership

print("apple"  not in gender)
print("apple"  in gender)

#Tuple methods

print(gender.count("Male"))
print(gender.index("Male"))

#Sets=unordered and unindexed
s={1,4,3,100,1000}
print(s)

s2=set((1,2,3))
print(s2)
s=set()
print(type(s))


a={1,2,3}
b={3,4,5}

print(a & b)#Intersection
print(a-b)#Difference
print(a|b)#Union
print(a^b)#Symmetric Difference

#Set Methods
b.add(6)
print(b)
a.remove(3)
print(a)
a.discard(4)
print(a)

b.pop()
print(b)


