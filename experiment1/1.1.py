def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

result = [n for n in range(1, 201) if n % 10 == 3 and is_prime(n)]
print(result)
