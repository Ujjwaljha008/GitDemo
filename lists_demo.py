"""
name = "John"
age = 20
percent = 85.5

student = ["John", 20, 85.5]     #------List are sequence, collection of any data of any data type

print(type(student))
print(student)

days_of_week = ["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
print(days_of_week)
print(len(days_of_week)) #------Length of a list => the number of items/elements in the list
print(days_of_week[3])
print(f"Last day of the week is {days_of_week[6]}")
print(f"Last day of the week is {days_of_week[-1]}")

print(days_of_week[8])
"""

"""
#Slicing of lists
l1=[3,8,1,0,4,9,7,3,6]
print(len(l1))
print(l1[1:6:1])
print(l1[2:7:2])
"""

"""
#Concatenation of lists
l1=[1,7,2]
l2=[0,5]
print(l1+l2)
print(l2+l1)
"""

"""
#Repition of lists
l1=[1,7,2]
l2=[0,5]

# *
print(l2*3)
"""

"""
#append()
#adds an item to the end of the list

fruits=["Mango","Apple","Orange"]
print(fruits)
#syntax: list.append("item")
fruits.append("Pineapple")
print(fruits)
"""

"""
#insert -  adds an element before the specified index
#syntax: list.insert(index,item)
fruits = ["Mango","Apple","Orange"]
print(fruits)
fruits.insert(2,"Pineapple")
print(fruits)
"""

"""
#list_operations
extend()
remove()
pop()
"""

"""
#extend()
fruits=["Mango","Apple","Orange"]
print(fruits)
fruits.extend(["Banana","Grapes"])
print(fruits)
fruits.append(["Banana","Grapes"])
print(fruits)
print(len(fruits))
"""

"""
#remove()
fruits=["Mango","Apple","Orange","Apple"]
print(fruits)
fruits.remove("Apple")
print(fruits)
"""

"""
#pop()
fruits=["Mango","Apple","Orange","Apple"]
print(fruits)
fruits.pop(2)
print(fruits)
"""

"""
reverse()
sort()
count()
Membership operation
"""

"""
days_of_week=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
print(days_of_week)
days_of_week.reverse()
print(days_of_week)
"""

"""
nums=[4,9,0,1,2,8]
print(nums)
#sort()
nums.sort()
print("Sorted List:",nums)
nums.sort(reverse=True)
print("Sorted List:",nums)
"""

"""
#count()
numbers=[0,1,3,4,1,0,5,0,0,3,0]
print(f"The list is : {numbers}")
item_to_count=int(input("Enter the number to be counted from the above list: "))
c=numbers.count(item_to_count)
print(f"Occurrence of {item_to_count} is {c}")

language=["Python", "Java", "C++", "Python"]
print(f"The list is : {language}")
item_to_count=input("Enter the item to be counted from the above list: ")
c=language.count(item_to_count)
print(f"Occurrence of {item_to_count} is {c}")
"""

#membership function ---- in(), not in()
language=["Python", "Java", "C++", "Python"]
print("Python" in language)
print("Node.js" in language)
print("C++" not in language)
print("Javascript" not in language)

