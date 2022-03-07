### PRACTICE LOOPS AND CONDITIONS ###


# Directions: Check if a number is prime

def is_prime(num):    
    if isinstance(num, int):    
        if num > 1:
            for b in range(2, num):
                # Make a condition to check if num is divisible 
                # by any number between 2 and num.
                # If the remainder is zero -> num is not a prime number.
                if():
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
            # Check if a is a prime number. Hint: use your function is_prime().          
	    # Then make a condition if the numer is prime add it to the list primes.
            if len(primes) == x:
                print("List of the first %s numbers %s" % (x, primes))
                return primes
    else:
        print("Error: Parameter should be an integer")
        return None        


# Directions: Find the largest prime factor of a given number

def get_max_prime_factor(num):
    if isinstance(num, int):    
        # Check if num is prime. Hint: use your function is_prime()
        # and return the value in the followin variable isPrime.
        isPrime = None
        if isPrime:           
           print("The largest prime factor of %s is %s" % (num, num))
           return num
        else:
           for i in range(num, 2, -1):
	       # Check if num is prime. Hint: use your function is_prime()
	       # and return the value in the followin variable isPrime.           
               isPrime = None
               if isPrime and num % i == 0:
                   print("The largest prime factor of %s is %s" % (num, i))
                   return i           
    else:
        print("Error: Parameter should be an integer")     
        return None        
