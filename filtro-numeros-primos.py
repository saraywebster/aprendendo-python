def readNumbers(): 
    number = 0
    numberList = []

    while number >= 0:
        number = int(input(''))
        if number >= 0:
            numberList.append(number)

    return numberList

def filterPrimeNumbers(numberList):
    isPrimeNumberList = []

    for number in numberList:
        isPrimeNumberList.append(checkIfIsPrimeNumber(number))
    
    return isPrimeNumberList


def checkIfIsPrimeNumber(number):
    basicPrimeNumbers = [2, 3, 5, 7]

    if number in basicPrimeNumbers:
        return 1

    if checkIfHaveIntSquareRoot(number): 
        return 0

    if checkIfIsDivisibleBy(number, 2) or checkIfIsDivisibleBy(number, 3) or checkIfIsDivisibleBy(number, 5) or checkIfIsDivisibleBy(number, 7):
        return 0 

    return 1
   
def checkIfHaveIntSquareRoot(number):
    root = number**(1/2)
    return ((root.real - int(root.real)) == 0)

def checkIfIsDivisibleBy(a, b):
    return a%b == 0

def startProgram ():
    inputNumbers = readNumbers()
    out = filterPrimeNumbers(inputNumbers)
    for number in out:
        print(number)

startProgram()


