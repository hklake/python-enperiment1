scores = {"张三": 99, "李四": 78, "王五": 60, "周六": 96,
          "赵七": 65, "孙八": 90, "郑九": 78, "吴十": 99}

#  计算终端显示宽度
def cjk_len(s):
    return sum(2 if ord(c) > 127 else 1 for c in str(s))

def pad(s, width, align="left"):
    s = str(s)
    spaces = max(0, width - cjk_len(s))
    if align == "right":  return " " * spaces + s
    if align == "center": return " " * (spaces // 2) + s + " " * (spaces - spaces // 2)
    return s + " " * spaces                          # left（默认）

def grade(n):
    return "优秀" if n >= 90 else "良好" if n >= 80 else "中等" if n >= 70 else "及格" if n >= 60 else "不及格"

#  列宽设置 
W = [6, 8, 8, 10]   # 序号 | 姓名 | 分数 | 等级

def border(l, m, r):
    return l + (m.join("─" * (w + 2) for w in W)) + r

def row(idx, name, score, gr):
    return (f"│ {pad(idx,   W[0], 'center')} │"
            f" {pad(name,  W[1], 'left'  )} │"
            f" {pad(score, W[2], 'right' )} │"
            f" {pad(gr,    W[3], 'center')} │")

# 题目一：输出表格
print(border("┌", "┬", "┐"))
print(row("序号", "姓名", "分数", "等级"))
print(border("├", "┼", "┤"))
for i, (name, score) in enumerate(scores.items(), 1):
    print(row(i, name, score, grade(score)))
print(border("└", "┴", "┘"))

#  题目二：f-string 统计 
avg  = sum(scores.values()) / len(scores)
high = max(scores.values())
low  = min(scores.values())

print(f"\n平均分：{avg:.2f}")
print(f"最高分：{high}（{max(scores, key=scores.get)}）")
print(f"最低分：{low}（{min(scores, key=scores.get)}）")