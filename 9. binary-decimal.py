choice = raw_input('To convert binary to decimal, enter "A". \nTo convert decimal to binary, enter "B". \n')

def binar(x):
    decimal = 0
    count = 0
    b = str(x)[::-1]
    for i in b:
        if int(i) == 1:
            decimal += 2**count
        count += 1
    return decimal

def decim(x):
    binary = ''
    while x > 0:
        binary += str(x%2)
        x = x/2
    return int(binary[::-1])

if choice.lower().startswith('a'):
    y = raw_input("Enter the binary ")
    print "The decimal of {} is {}" .format(y, binar(y))

if choice.lower().startswith('b'):
    al = raw_input("Enter the decimal ")
    print "The binary of {} is {}" .format(al, decim(al))
