# 斐波那契数列 非递归+生成器
def fib(num):
    if num < 2:
        return 1
    a, b = 1, 1
    for i in range(num):
        yield a
        a, b = b, a + b


f = fib(8)
for i in f:
    print(i)

# 非递归


def fib2(num):
    if num < 2:
        return 1
    a, b = 1, 2
    for i in range(num-2):
        a, b = b, a + b
    return b


print(fib2(8))

# 一只青蛙一次能上1 or 2个台阶，上n个台阶有多少种上法, f(n-1)+f(n-2)正好是斐波那契数列


def fib3(n):
    if n == 0:
        return 1
    if n < 3:
        return n
    a, b = 1, 2
    for i in range(n - 2):
        a, b = b, a + b
    return b


print(fib3(8))

# 一个青蛙一次能上至多n个台阶， 请问他上n个台阶有多少种上法。
# f(n-1) = f(n-2)+f(n-3)+...+f(2)+f(1)
# f(n) = f(n-1)+f(n-2)+f(n-3)+...+f(2)+f(1)
# f(n) = 2f(n-1)
# 等比数列 f(n)/f(n-1) = 2


def fib4(n):
    import math
    if n == 0:
        return 1
    return int(math.pow(2, n - 1))  # pow返回浮点型


print(fib4(1))
