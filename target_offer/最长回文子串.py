
'''
最长回文子串，利用dp，从01开始，向外扩展，ij是否能组成回文子串的最外层，取决于i+1，j-1是否是回文子串
这样从最里层开始叠加，然后每次为True后，要实时更新，最长字串的头和尾，这样会记录，最早出现的最长回文子串
如果从string的尾部开始遍历，会找到最后出现的最长回文子串
'''
'''
动态规划
'''


def longest_palindromic_substr(string):
    left = 0
    right = 0
    if string:
        # m*n二维矩阵保存结果
        dp = [[False]*len(string) for i in range(len(string))]
        for i in range(1, len(string)):
            for j in range(i-1, -1, -1):
                # 这里很重要，不要忘记给矩阵的对角线处加True，利于奇数长度的回文子串的判断
                dp[i][i] = True
                # 一般ij的状态是看i-1，j+1的状态，但如果二者差1，就直接看是否相等
                dp[i][j] = string[i] == string[j] and (i-j < 2 or dp[i-1][j+1])
                # 注意更新最长回文子串的范围
                if dp[i][j] and i - j > right - left:
                    right = i
                    left = j
    return string[left:right+1]


print(longest_palindromic_substr('123454321869876554897598464567876849374984549'))