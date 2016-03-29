
next_prime = raw_input("View next prime number? (y/n)")
current = 1

def isprime(x):
    if x%2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x%i == 0:
            return False
    else:
        return True

while next_prime.lower().startswith('y'):
    current += 1

    while isprime(current) == False:
        current += 1

    print "Next prime is " + str(current)
    next_prime = raw_input("View next prime number? (y/n)")
