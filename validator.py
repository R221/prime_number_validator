def factorial(n):
    if n == 1:
        return n
    else:
        factorial_result = (n * factorial(n-1))
        return factorial_result
    
def findPrime(n, i=2):
    if n % i == 0:
        return False
    else:
        findPrime(n-1)
        return True
    
def menu():
    n = int(input("Enter a number: "))
    choice = str(input("Do you want to see its factorial or if it's a prime number?"))
    
    if choice == "factorial":
        print(factorial(n))
    elif choice == "prime":
        if findPrime(n) is False:
            print(n, "is not a prime number.")
    else: print(n, "is a prime number.")
menu()