def getDividers(number):
    dividers = []
    for i in range(1, number+1):
        if number%i == 0:
            dividers.append(i)
    return sum(dividers)
    

print(getDividers(int(input('Número: '))))