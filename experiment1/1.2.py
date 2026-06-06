result = []
used_digits = set()

for n in range(8, 101, 8):
    digits = set(int(d) for d in str(n))
    if digits.issubset(used_digits):  # 各位数字全已出现 → 跳过
        continue
    result.append(n)
    used_digits.update(digits)

print(result)
