"""
s1= "Python is fun"
print(s1[0])
print(s1[-1])
print(len(s1))

language="Python"
version="3.13.3"
print(language+version)
"""
# s1="Python"
# print(s1*3)
#in string, '*' is repetition operator

"""
#Membership operation
#in
s1="Python is fun"
print("Python" in s1)
print("i" in s1)
print("z" in s1)
print("Java" in s1)

# not in
print("Python" not in s1)
print("z" not in s1)
print("Java" not in s1)
"""

"""
#Comparison of strings
print("Python" == "Python")
print("Python " == "Python")

#Removing spaces from a string - strip()

s1=" Python "
s2=s1.strip()
print(s2)

print(s1.strip() == "Python")
"""

#replace()
s1="We are learning Python"
print(s1)
print(s1.replace("Python","Java"))
print(s1.replace("e","E"))
print(s1.replace("e","E",1))
