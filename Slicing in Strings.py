s1="Hello World"
"""
Syntax of indexing:  string[index]
Syntax of slicing: string[start:end:step]
-start: starting index at which the slicing operation starts
-end: ending index at which the slicing stops (excluded)
-step: integer that specifies the step for the slicing
"""
"""
print(s1)
#length of string
print(len(s1))
#Indexing
print("First Character: ",s1[0])
print("Last Character: ",s1[-1])
"""

# print(s1[2:7:1])
# print(s1[2:9:2])
s1_slice=s1[1:12:3]
print(type(s1_slice))

print(s1_slice)
