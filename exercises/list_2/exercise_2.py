for i in range(5):
    bestProductionDay = -9999999
    total = 0

    dayProduction = int(input("Produção do dia: "))
    
    if(dayProduction > bestProductionDay):
        bestProductionDay = dayProduction
    
    total += dayProduction
    average = dayProduction

print(bestProductionDay)