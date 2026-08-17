grade1 = float(input("Nota 1: "))
grade2 = float(input("Nota 2: "))

average = (grade1 + grade2) / 2

if(average >= 6):
    print("Aprovado")
elif(average >= 4):
    print("Em exame")  
else:
    print("Reprovado") 
