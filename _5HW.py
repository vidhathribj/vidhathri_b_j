#1
'''List Manipulation Exercise:

Create a list of 5 items (strings or numbers).
Add a new item to the end of the list and another at the second position.
Remove the third item from the list.
Print the list after each operation.'''

list=[1,4,156,34,100]
list.append(23)
print(list)
list.insert(1,45)
print(list)
list.remove(4)
print(list)

#2
'''Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

Prints the entire matrix row by row.
Prints the sum of each row in the matrix.'''

list1=[]
n=int(input("Enter the number of elements in the list: "))
print("Enter elements:")
for i in range (0,n):
   ele=int(input())
   list1.append(ele)    
print(list1)

