def find_next_prime(n):
    # Do your coding here
    def is_prime(n):
        for i in range(2, n/2):
            if n%i == 0:
                return False
        else: 
            return True

    while True:
        if is_prime(n+1) == True:
            return n+1
        else:
            n += 1

    
