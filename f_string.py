name="John"
age=20
language ="Python"
hours=3

#John is 20 years old. He studies Python 3 hours a day.
print(name,"is",age,"years old. He studies",language,hours,"hours a day.")

#using f-string
print(f"{name} is {age} years old. He studies {language} {hours} hours a day.")

sub1=78
sub2=87
sub3=83

print(f"{name} scored {sub1+sub2+sub3} marks in total.")
percent=(sub1+sub2+sub3)/3
print(f"{name} got {percent:.2f}% percent.")

f_name=input("Enter your first name: ")
l_name=input("Enter your last name: ")
percent=float(input("Enter percentage: "))

print(f"{f_name} {l_name} scored {percent:.2f}% percentage")
