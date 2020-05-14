file = open("calcFile1.txt", mode='r')
listOfCalcs = file.read().splitlines()
file.close()

sum = 0
for instruction in listOfCalcs:
    parts = instruction.split()
    if(parts[1] == '+'):
        sum += (int(parts[2]) + int(parts[3]))
    elif(parts[1] == '-'):
        sum += (int(parts[2]) - int(parts[3]))
    elif(parts[1] == 'x'):
        sum += (int(parts[2]) * int(parts[3]))
    elif(parts[1] == '/'):
        sum += (int(parts[2]) / int(parts[3]))
    elif(parts[1] == '%'):
        sum += (int(parts[2]) % int(parts[3]))
    else:
        print('Invalid operation.')
print(sum)