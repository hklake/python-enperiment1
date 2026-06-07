# 方法1：for循环

print("方法1：for循环")

result1 = []

for n in range(2, 201):
    if n % 10 == 3:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            result1.append(n)

print(result1)


# 方法2：列表推导式

print("\n方法2：列表推导式")

result2 = [
    n for n in range(2, 201)
    if n % 10 == 3
    and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
]

print(result2)


# 方法3：filter + lambda

print("\n方法3：filter + lambda")

result3 = list(
    filter(
        lambda n:
        n % 10 == 3 and
        all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)),
        range(2, 201)
    )
)

print(result3)