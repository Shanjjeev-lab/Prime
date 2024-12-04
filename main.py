from math import sqrt

def is_prime(num):
    global iteration
    iteration = 0
    if num <= 1:
        return False
    sqrt_num = int(sqrt(num))
    for i in range(2, sqrt_num + 1):
        iteration += 1
        if num % i == 0:
            return False
        return True
        
num = int(input("Enter a number: "))
result = is_prime(num)
if result:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")