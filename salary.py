def setSalaryIncrease(salary):
    if salary > 2.000:
        return salary*1.07
    else:
        return salary*1.15


print(setSalaryIncrease(float(input('Salário atual: '))))