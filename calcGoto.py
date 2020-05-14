import math

def calc(operation, num1, num2):
    if(operation == '+'):
        return (int(num1) + int(num2))
    elif(operation == '-'):
        return (int(num1) - int(num2))
    elif(operation == 'x'):
        return (int(num1) * int(num2))
    elif(operation == '/'):
        return math.floor(int(num1) / int(num2))
    else:
        raise Exception('Operation invalid.')

file = open("calcFile2.txt", mode='r')
listOfGotos = file.read().splitlines()
file.close()

linesSeen = set()
currentLine = 1
while not currentLine in linesSeen:
    linesSeen.add(currentLine)
    lineParts = listOfGotos[currentLine - 1].split()
    print(lineParts)
    if(lineParts[1] == 'calc'):
        currentLine = calc(lineParts[2], lineParts[3], lineParts[4])
    else:
        currentLine = int(lineParts[1])
    print(currentLine)