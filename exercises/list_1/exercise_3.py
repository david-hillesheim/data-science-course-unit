def draw(length):
    for i in range (length):
        print("_", end="")
        
draw(5)

print("")

def drawList(list):
    for i in range (len(list)):
        print((i + 1), " - ", list[i])

drawList(["A", 123, True])

def calcAverage(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    
    print("Média: ", sum / len(numbers))

calcAverage([1, 1, 10])