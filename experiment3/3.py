import math
from fractions import Fraction

#  a) 基本运算：加、减、乘、除、取模、取余、四舍五入、取整

def add(op1, op2):
    """加法：返回 op1 + op2，支持整数和浮点数"""
    return op1 + op2

def sub(op1, op2):
    """减法：返回 op1 - op2"""
    return op1 - op2

def mul(op1, op2):
    """乘法：返回 op1 * op2"""
    return op1 * op2

def div(op1, op2):
    """除法：返回 op1 / op2（真除法）"""
    if op2 == 0:
        return "错误：除数不能为 0"
    return op1 / op2

def mod(op1, op2):
    """取模：结果符号与除数相同（Python 的 %）"""
    if op2 == 0:
        return "错误：除数不能为 0"
    return op1 % op2

def remainder(op1, op2):
    """取余：结果符号与被除数相同（math.fmod）"""
    if op2 == 0:
        return "错误：除数不能为 0"
    return math.fmod(op1, op2)

def round_num(num, decimals=0):
    """四舍五入：保留 decimals 位小数（默认取整）"""
    return round(num, decimals)

def floor_num(num):
    """向下取整（地板取整）"""
    return math.floor(num)

def ceil_num(num):
    """向上取整（天花板取整）"""
    return math.ceil(num)

def trunc_num(num):
    """截断取整（向零取整）"""
    return math.trunc(num)

#  b) 十进制转换为 2 / 8 / 16 进制输出

def to_binary(n):
    """十进制整数 → 二进制字符串"""
    return bin(int(n))

def to_octal(n):
    """十进制整数 → 八进制字符串"""
    return oct(int(n))

def to_hex(n):
    """十进制整数 → 十六进制字符串"""
    return hex(int(n))

def to_all_bases(n):
    """同时输出三种进制"""
    n = int(n)
    print(f"  十进制：{n}")
    print(f"  二进制：{bin(n)}")
    print(f"  八进制：{oct(n)}")
    print(f"  十六进制：{hex(n)}")

#  c) 支持 2 / 8 / 16 进制输入，并完成 a) 中运算

def parse_num(s):
    """
    解析多进制字符串为十进制整数
      '0b1010' → 二进制   '0o12' → 八进制   '0xff' → 十六进制
      '10'     → 十进制（默认）
    """
    s = str(s).strip()
    if   s.startswith(("0b", "0B")): return int(s, 2)
    elif s.startswith(("0o", "0O")): return int(s, 8)
    elif s.startswith(("0x", "0X")): return int(s, 16)
    else:                             return int(s)

def calc_multi_base(s1, op, s2):
    """
    多进制输入计算器
      s1, s2：任意进制字符串
      op：'+' '-' '*' '/' '%'
    """
    a, b = parse_num(s1), parse_num(s2)
    ops = {'+': add, '-': sub, '*': mul, '/': div, '%': mod}
    if op not in ops:
        return "错误：不支持的运算符"
    return ops[op](a, b)

#  d) 数字转换成科学计数法输出

def to_scientific(num, decimals=4):
    """将数字转为科学计数法字符串，保留 decimals 位有效小数"""
    return f"{num:.{decimals}e}"

#  e) 支持科学计数法输入数字

def parse_scientific(s):
    """
    解析科学计数法字符串为浮点数
      支持：'1.5e3'  '2.3E-4'  '1.5*10^3'
    """
    s = str(s).strip().replace(" ", "")
    if "*10^" in s:
        base, exp = s.split("*10^")
        return float(base) * (10 ** float(exp))
    return float(s)

#  f) 自由发挥  角度  弧度互转，弧度保留 π 的分数形式

def deg_to_rad(degrees):
    """角度 → 弧度，以 π 分数形式输出，如 90° → π/2"""
    if degrees == 0:
        return "0"
    frac = Fraction(degrees, 180)   # 化最简分数
    n, d = frac.numerator, frac.denominator
    if n == 1 and d == 1:
        return "π"
    elif d == 1:
        return f"{n}π"
    elif n == 1:
        return f"π/{d}"
    else:
        return f"{n}π/{d}"

def rad_to_deg(rad_str):
    """弧度（π表达式字符串）→ 角度，如 'π/2' → 90.0°"""
    rad_str = str(rad_str).strip().replace("π", str(math.pi))
    return eval(rad_str) / math.pi * 180

#  测试

print("=" * 50)
print("【a) 基本运算测试】")
print("=" * 50)
print("测试加法          :", add(3, 5))
print("测试浮点加法      :", add(3.5, 5.5))
print("测试减法          :", sub(10, 4))
print("测试乘法          :", mul(6, 7))
print("测试除法          :", div(10, 3))
print("测试除以 0        :", div(5, 0))
print("测试取模  7 % 3   :", mod(7, 3))
print("测试取模 -7 % 3   :", mod(-7, 3))       # 结果与除数同号（正）
print("测试取余 -7 % 3   :", remainder(-7, 3)) # 结果与被除数同号（负）
print("测试四舍五入      :", round_num(3.14159, 2))
print("测试四舍五入取整  :", round_num(3.6))
print("测试向下取整      :", floor_num(3.9))
print("测试向上取整      :", ceil_num(3.1))
print("测试截断取整      :", trunc_num(-3.9))  # 向零，结果 -3

print()
print("=" * 50)
print("【b) 进制转换测试】")
print("=" * 50)
print("255 转二进制      :", to_binary(255))
print("255 转八进制      :", to_octal(255))
print("255 转十六进制    :", to_hex(255))
print("42  三种进制同时输出：")
to_all_bases(42)

print()
print("=" * 50)
print("【c) 多进制输入运算测试】")
print("=" * 50)
print("0b1010 + 0b0110  =", calc_multi_base("0b1010", "+", "0b0110"))  # 10+6=16
print("0o17   * 0o2     =", calc_multi_base("0o17",   "*", "0o2"))     # 15*2=30
print("0xff   - 0x0f    =", calc_multi_base("0xff",   "-", "0x0f"))    # 255-15=240
print("0b1100 + 0o10    =", calc_multi_base("0b1100", "+", "0o10"))    # 12+8=20
print("100    / 4       =", calc_multi_base("100",    "/", "4"))

print()
print("=" * 50)
print("【d) 科学计数法输出测试】")
print("=" * 50)
print("123456789 →", to_scientific(123456789))
print("0.000314  →", to_scientific(0.000314))
print("光速(保留2位) →", to_scientific(299792458, 2))

print()
print("=" * 50)
print("【e) 科学计数法输入测试】")
print("=" * 50)
print("解析 '1.5e3'     =", parse_scientific("1.5e3"))
print("解析 '2.3E-4'    =", parse_scientific("2.3E-4"))
print("解析 '1.5*10^3'  =", parse_scientific("1.5*10^3"))
print("科学计数法加法   =", add(parse_scientific("1.5e3"), parse_scientific("2.5e2")))

print()
print("=" * 50)
print("【f) ★ 角度 ↔ 弧度互转测试】")
print("=" * 50)
print("【角度 → 弧度】")
for deg in [0, 30, 45, 60, 90, 120, 135, 180, 270, 360]:
    print(f"  {deg:>4}° → {deg_to_rad(deg)}")

print("\n【弧度 → 角度】")
for rad in ["π/6", "π/4", "π/3", "π/2", "2π/3", "3π/4", "π", "3π/2", "2π"]:
    print(f"  {rad:>6} → {rad_to_deg(rad):.1f}°")

print("\n互转验证（135° → 弧度 → 角度）:")
rad = deg_to_rad(135)
print(f"  135° → {rad} → {rad_to_deg(rad):.1f}°")