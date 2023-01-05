school = { "Maths":"Irene",
           "Computer Science": "Sinéad",
           "Science":"Neil"}

...

#answer
for subject in school:
    print(subject,school)
print("------------")
    
for subject,teacher in school.items():
    print(subject,teacher)
print("------------")

for subject in school:
    print(subject,school[subject])
print("------------")