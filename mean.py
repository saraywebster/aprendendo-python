def receiverNumbers():
    numbers = []
    for i in range(0, 3):
        numbers.append(int(input('Digite um número: ')))
    return numbers

def setArithmeticAverage(numbers):
    return (sum(numbers)/len(numbers))

print(setArithmeticAverage(receiverNumbers()))

