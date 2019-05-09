# Initialize a list
primes = []
def genPrimes(n):
    for possiblePrime in range(2, n):
        
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
                break
        
        if isPrime:
            primes.append(possiblePrime)
    print(primes)

genPrimes(int(input("Enter number: ")))