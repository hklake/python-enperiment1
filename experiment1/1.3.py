# 方法一：for 循环
result = []
for n in range(2, 9):
    result.append((n, n**2, n*(n+1)))
print(result)


# 方法二：列表推导式
result = [(n, n**2, n*(n+1)) for n in range(2, 9)]
print(result)

# 方法三：map + lambda
result = list(map(lambda n: (n, n**2, n*(n+1)), range(2, 9)))
print(result)