var = {}

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def is_more_than_one():
    value = 0
    for i in var:
        value += var[i] 
    if value > 1: return True

def withRemaining():
    remaining = 1
    for i in var:
        remaining -= var[i]
    
    print(f'remaining{remaining}')    
    value = input("masukan value : ")
    value = value.split(',')
    for i in operation:
        if i in value[1]:
            result = value[1].split(i)
            value[1] = operation[i](multiply(remaining, int(result[0])), int(result[1]))
            break
    var[value[0]] = value[1]
    
operation = {
    '+' : add,
    '-': substract,
    '/': divide,
    'x': multiply
}


while True:
    value = input("masukan value : ")
    value = value.split(',')
    lastitem = value[0]
    if value[1] == 'a':
        var[value[0]] = 1
        if len(var) > 1: 
            for i in var:
                if i != value[0]:
                    var[value[0]] -= var[i] 
        break
    for i in operation:
        if i in value[1]:
            result = value[1].split(i)
            value[1] = operation[i](int(result[0]), int(result[1]))
            break
    var[value[0]] = value[1]
    if is_more_than_one() == True: 
        print("value more than 1")
        print(f"{lastitem} with value {var.pop(lastitem)}, has been removed")
        break 
    isContinue = input("continue? y/n (r with remaining)")
    if isContinue == 'r':
        withRemaining()
        isContinue = input("continue? y/n (r with remaining)")
    if isContinue == 'n': break 
    
while True:
    listHowMany = []
    for i in var:
        print(i)
    value = input('choose one : ')
    howMany = input(f'how many {value} known? :' )
    
    for i in var:
        value1 = var[i] / var[value] * float(howMany)
        listHowMany.append(value1)
    listHowMany.append(howMany)
    
    for i, v in enumerate(var):
        print(f'{v} : {listHowMany[i]} ')
    listHowMany.clear()
        
print(var)