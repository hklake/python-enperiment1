import re

#  Token 类型定义

TOKEN_RULES = [
    ("浮点数",   r'\d+\.\d+'),          # 必须在整数前面匹配，否则会被截断
    ("整数",     r'\d+'),
    ("幂运算",   r'\*\*'),              # 必须在乘号前面，否则 ** 被识别成两个 *
    ("地板除",   r'//'),               # 必须在除号前面
    ("乘号",     r'\*'),
    ("除号",     r'/'),
    ("取模",     r'%'),
    ("加号",     r'\+'),
    ("减号",     r'-'),
    ("左括号",   r'\('),
    ("右括号",   r'\)'),
    ("空白",     r'\s+'),              # 空白跳过，不输出
]

# 编译成一个总的正则，用命名分组
MASTER_PATTERN = re.compile(
    "|".join(f"(?P<{name.replace('运算','_op').replace('括号','_paren')}_{i}>{pattern})"
             for i, (name, pattern) in enumerate(TOKEN_RULES))
)

#  词法分析主函数

def lexer(expression):
    """
    简易词法分析器：将算术表达式字符串解析为 token 列表
    
    参数：
        expression: 输入的算术表达式字符串
    返回：
        tokens: [(类型, 值), ...] 列表，最后追加 ('终止符', '$')
    """
    tokens = []
    pos = 0
    expr = expression.strip()

    # 用于识别负数：若当前 '-' 前面是数字或右括号，则为减号；否则为负数的一部分
    i = 0
    # 重新用逐字符+re.match方式，更灵活处理负数
    while i < len(expr):
        matched = False

        #  特殊处理负数 
        # 条件：当前是 '-'，且前一个有效token不是数字/右括号
        if expr[i] == '-':
            prev = tokens[-1][0] if tokens else None
            is_negative = prev not in ("整数", "浮点数", "右括号")
            if is_negative:
                # 尝试匹配负浮点数或负整数
                m = re.match(r'-\d+\.\d+|-\d+', expr[i:])
                if m:
                    val = m.group()
                    tok_type = "浮点数" if '.' in val else "整数"
                    tokens.append((tok_type, val))
                    i += len(val)
                    matched = True

        if matched:
            continue

        #  按规则顺序匹配 
        for name, pattern in TOKEN_RULES:
            m = re.match(pattern, expr[i:])
            if m:
                val = m.group()
                if name != "空白":          # 空白直接跳过
                    tokens.append((name, val))
                i += len(val)
                matched = True
                break

        if not matched:
            raise SyntaxError(f"无法识别的字符：'{expr[i]}' （位置 {i}）")

    tokens.append(("终止符", "$"))
    return tokens


#  格式化输出函数

def format_tokens(tokens):
    """将 token 列表格式化为 <类型:值> 字符串"""
    return "".join(f"<{t}:{v}>" for t, v in tokens)

def format_tokens_simple(tokens):
    """只输出类型，如题目示例：<数字><乘号>..."""
    return "".join(f"<{t}>" for t, v in tokens)

def print_result(expr):
    """完整输出一个表达式的词法分析结果"""
    print(f"\n  输入：{expr}")
    try:
        tokens = lexer(expr)
        print(f"  简洁：{format_tokens_simple(tokens)}")
        print(f"  详细：{format_tokens(tokens)}")
        print(f"  列表：{tokens}")
    except SyntaxError as e:
        print(f"  错误：{e}")


#  单元测试

print("=" * 60)
print("【题目示例】")
print("=" * 60)
print_result("3*(2-3)")

print()
print("=" * 60)
print("【整数与基本四则运算】")
print("=" * 60)
print_result("1 + 2")
print_result("10 - 3 * 4")
print_result("100 / 4 + 5")

print()
print("=" * 60)
print("【浮点数】")
print("=" * 60)
print_result("3.14 * 2")
print_result("1.5 + 2.5 - 0.1")

print()
print("=" * 60)
print("【负数】")
print("=" * 60)
print_result("-3 + 5")
print_result("(-3.14) * 2")
print_result("10 + -2")       # 加负数

print()
print("=" * 60)
print("【幂运算 **】")
print("=" * 60)
print_result("2 ** 10")
print_result("3 ** 2 + 1")

print()
print("=" * 60)
print("【取模 % 与地板除 //】")
print("=" * 60)
print_result("17 % 5")
print_result("17 // 5")
print_result("17 % 5 + 17 // 5")

print()
print("=" * 60)
print("【括号与复杂表达式】")
print("=" * 60)
print_result("(1 + 2) * (3 - 4)")
print_result("((2 + 3) * 4) // 6")
print_result("2 ** (3 + 1) - 10 % 3")

print()
print("=" * 60)
print("【综合压力测试】")
print("=" * 60)
print_result("-3.14 * (2 ** 8) // 10 + 99 % 7 - (-1.5)")

print()
print("=" * 60)
print("【错误处理测试】")
print("=" * 60)
print_result("3 @ 2")      # 非法字符