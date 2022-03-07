### PRACTICE LOOPS AND CONDITIONS ###


# Directions: Check if a number is prime

def is_prime(num):    
    if isinstance(num, int):    
        if num > 1:
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
        return primes
    else:
        print("Error: Parameter should be an integer")
        return None
        

# Directions: Find the largest prime factor of a given number

def get_max_prime_factor(num):
    if isinstance(num, int):    
        isPrime = None
        if isPrime:           
           print("The largest prime factor of %s is %s" % (num, num))
           return num
        else:
           # Return the max prime factor
           return None 
    else:
        print("Error: Parameter should be an integer")     
        return None
