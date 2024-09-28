#1
'''Tuple Operations:

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.'''

Tuple=(1,45,63,72,13)
print(Tuple[1:3])

First=(1,2,3)
Second=(4,5,6)
Concatenate=First+Second

print(Concatenate)

#2
'''Set Operations:

Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?
'''
my_favourite={"Mango","Banana","Pineapple"}
friend_favourite={"Kiwi","Watermelon","Pineapple"}

common=my_favourite & friend_favourite
union=my_favourite | friend_favourite
difference=my_favourite - friend_favourite
print(common)
print(union)
print(difference)

my_favourite.add("Apple")
print(my_favourite)

my_favourite.remove("Apple")
my_favourite.discard("Raspberry")
print(my_favourite)

#3
'''Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?'''

list1=[1,2,6,14]

print(tuple(list1))
print(set(list1))

tuple=(1,45,29)
set={5,32,26}
list2=list(tuple)
list2.append(48)
print(list2)

list3=list(set)
list3.append(63)
print(list3)







