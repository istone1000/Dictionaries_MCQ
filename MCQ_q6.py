teachers = { }

#answers

teachers = { "Maths":"Irene",
          "Computer Science": "Sinéad",
          "Science":"Neil"}

# teachers["Maths"]:"Irene"
# teachers["Computer Science"]:"Sinéad"
# teachers["Science"]:"Neil"
# 
# teachers{"Maths"="Irene"}
# teachers{"Computer Science"="Sinéad"}
# teachers{"Science"="Neil"}

teachers["Maths"]="Irene"
teachers["Computer Science"]="Sinéad"
teachers["Science"]="Neil"

print(teachers)
del teachers["Maths"]
print(teachers)