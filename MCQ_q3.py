school = { "Maths":"Irene",
           "Computer Science": "Sinéad",
           "Science":"Neil"}

...

#incorrect solution
for subject in school:
    print(subject,school)
print("------------")

#a correct solution
for subject,teacher in school.items():
    print(subject,teacher)
print("------------")

#a correct solution
for subject in school:
    print(subject,school[subject])
print("------------")
