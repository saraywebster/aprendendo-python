def receiveNumbers():
    numbers = []
    for i in range(0, 10):
        numbers.append(int(input(": ")))
    return numbers

def getHigherNumber(numbers):
    numbers.sort()
    return numbers[len(numbers) - 1]

def getSmallerNumber(numbers):
    numbers.sort()
    return numbers[0]

def setArithmeticAverage(numbers):
    return (sum(numbers)/len(numbers))

def getsmallerThan(average, numbers):
    smaller = []
    for i in range(0, len(numbers)):
        if numbers[i] < average:
            if (smaller.count(numbers[i])) == 0 :
                smaller.append(numbers[i])
    smaller.sort()
    return smaller


def startProgram():
    numbers = receiveNumbers()
    print("O maior número: " + str(getHigherNumber(numbers)))
    print("O menor número: " + str(getSmallerNumber(numbers)))
    print("Média: " + str(setArithmeticAverage(numbers)))
    print("Menores que a média: " + str(getsmallerThan(setArithmeticAverage(numbers), numbers)))

startProgram()