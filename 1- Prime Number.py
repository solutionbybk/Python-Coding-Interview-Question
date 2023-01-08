def prime(num):
    is_prime = True
    for value in range(2,num):
        if num % value == 0:
            is_prime = False
            return is_prime
    return is_prime

output = prime(17)
print(output)
