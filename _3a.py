#
age=input("Age: ")
print(age)

boy_age=int(input("Boy age is: "))
boy_name=input("Boy name is: ")
girl_age=int(input("Girl age is: "))
girl_name=input("Girl name is: ")
age_diff = (boy_age) - (girl_age)

#Text and variable display
print(boy_name +" loves "+ girl_name +".Age difference is "+str(age_diff))
#f-strings
print(f"{boy_name} loves { girl_name}.Age difference is {str(age_diff)} ")
