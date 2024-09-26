#Lists

items=["Bru","Milk","Sugar"]

#Accessing list elements
print(items[-1])
print(items[-2])
print(items[0])

print(items)

items.pop()#To remove last element from list

print(items)
items.pop(0)#To remove from zeroth index
print(items)

#To add elements into list
items.append("Biscuit")

print(items)
(items.remove("Biscuit"))
print(items)
items.insert(1,"Biscuit")
print(items)

#To remove all elements
items.clear()
print(items)

#Modifying lists
items=["Bru","Milk","Sugar","Biscuit"]
items[0]="Coffee Powder"
print(items)

#Splicing

print(items[0::2])#it gives from 0th index to last skipping one
#[start:stop:step]
#append()	Adds an element at the end of the list
'''clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''
items2=items.copy()
print(items2)
print(items2.count("Coffee Powder"))
print(items.index("Milk"))
items1=["Chicken","Kebab Powder"]
items2.extend(items1)
print(items2)
items2.reverse()
print(items2)
list=[1,45,23,101,57]
list.sort(reverse=True)#False is default which sorts in ascending
print(list)


#Common functions
print(len(items2))#Gives length

list1=[25,50,100,75,250,155]
print(sorted(list1))

#Nested List

Matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(Matrix[1][1])

 