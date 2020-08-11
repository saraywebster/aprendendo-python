def defineFactorial(number):
    factorial = 1
    if number < 0:
        print('O número ' + str(number) + ' não possui um fatorial pois é negativo. No entanto o fatorial do seu simetrico é: ')
        number *= -1
    for i in range(1, number+1):
        factorial *= i  
    return factorial

print(defineFactorial(int(input('Número: '))))

