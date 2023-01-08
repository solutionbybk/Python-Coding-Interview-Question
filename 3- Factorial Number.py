def factorial(num):
    fact = num
    for i in range(num-1,0,-1):
        #fact = fact * i
        fact *= i
    return fact

factorial(4)
        
