### PRACTICE LOOPS AND CONDITIONS ###


# Directions: Check if a number is prime

def is_prime(num):
    if isinstance(num, int):    
        if num > 1:
            for b in range(2, num):
                if(num%b == 0):
                    print(num, "is not a prime number")
                    return False       
            print(num, "is a prime number")         
            return True
        else:
            print(num, "is not a prime number")
            return False       
    else:
        print("Error: Parameter should be an integer")
        return None
        
        
# Directions: Find the first 100 prime numbers

def get_primes(x):
    if isinstance(x, int):    
        primes = []
        for a in range(1,100000):
            isPrime = is_prime(a)
            if isPrime:
                primes.append(a)
            if len(primes) == x:
                print("List of the first %s numbers %s" % (x, primes))
                return primes
    else:
        print("Error: Parameter should be an integer")
        return None
        

# Directions: Find the largest prime factor of a given number

def get_max_prime_factor(num):
    if isinstance(num, int):    
        isPrime = is_prime(num)
        if isPrime:
           print("The largest prime factor of %s is %s" % (num, num))
           return num
        else:
           for i in range(num, 2, -1):
               isPrime = is_prime(i)
               if isPrime and num % i == 0:
                   print("The largest prime factor of %s is %s" % (num, i))
                   return i           
    else:
        print("Error: Parameter should be an integer")     
        return None        
