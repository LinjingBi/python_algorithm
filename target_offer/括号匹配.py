# 列出num对括号有多少种正确的组合方式
'''
利用回溯法，列举所有可能，并判断是否匹配
'''


def parentthese1(num):
    if num <= 0:
        return []
    seq = '('*num + ')'*num

    out = {}
    res = []
    for i in range(len(seq)):
        res.append(seq[i])
        core(res, seq[:i]+seq[i+1:], out, 2*num)
        # 注意每次循环都要pop上一个
        res.pop()
    return out.keys()


def core(res, seq, out, num):
    if len(res) == num:
        check(res, out)
        return
    for i in range(len(seq)):
        res.append(seq[i])
        core(res, seq[:i]+seq[i+1:], out, num)
        res.pop()
        # 注意pop
    return

# 利用栈匹配
def check(res, out):
    dq = []
    for each in res:
        if each == '(':
            dq.append(each)
        else:
            try:
                dq.pop()
            except IndexError:
                return
    # 检查栈是否为空
    if not dq:
        out[''.join(res)] = None
    return

# 方法二， 利用（ +1 ） -1， 来验证当长度达到2*num时，是否为0，只有为0才匹配


def parentth2(num):
    if num <= 0:
        return []

    def _core(n, res):
        if len(res) == 2*num:
            # 注意还要判断是否为0，因为之前的递归是随机的。
            if n == 0:
                out.append(''.join(res))
            return
        if n < num:
            res.append('(')
            _core(n+1, res)
            res.pop()
        # 很巧妙，两个if并不是elif，实现了十分精简的回溯
        if n > 0:
            res.append(')')
            _core(n-1, res)
            res.pop()
        return

    out = []
    _core(0, [])
    return out


print(parentth2(3))