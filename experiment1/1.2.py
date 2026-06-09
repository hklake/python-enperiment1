# 方法1：for循环

print("方法1：for循环")

used = set()
result1 = []

for n in range(8, 101, 8):
    digits = set(str(n))

    if not digits.issubset(used):
        result1.append(n)
        used.update(digits)

print(result1)


# 方法2：列表推导式

print("\n方法2：列表推导式")

used = set()

result2 = [
    n for n in range(8, 101, 8)
    if not set(str(n)).issubset(used)
    and not used.update(set(str(n)))
]

print(result2)


# 方法3：filter + lambda

print("\n方法3：filter + lambda")

used = set()

result3 = list(
    filter(
        lambda n:
        (not set(str(n)).issubset(used))
        and (not used.update(set(str(n)))),
        range(8, 101, 8)
    )
)

print(result3)
