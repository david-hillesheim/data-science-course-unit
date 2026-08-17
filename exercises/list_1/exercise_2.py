sum = 0
for i in range(3, 334, 3):
    sum += i

print(sum)

count = 0
sum = 0
while count < 10:
    sum += float(input("Digite a nota: "))
    count += 1

print("Média: ", sum / 10)

num = int(input("Digite um número: "))

if(num <= 0 or num > 10):
    print("Número inválido!")

for i in range (1, 11):
    print(num, " X ", i, " = ", i * num)