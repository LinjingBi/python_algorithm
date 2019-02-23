
# 岛屿问题，一个二维数组，全是0，1， 1代表小岛，0代表水，
# 两个1直线相连，就变成一片陆地
# [[0,0,1,0,0],
#  [0,1,0,0,0],
#  [0,1,1,0,0],
#  [0,0,0,0,0]]
# 有2个小岛
'''
依次遍历，遇到为1的就进行DFS，小岛数+1，并将DFS中的1都变为0，消灭与之相连的岛群。
'''

def find_island(array):
    count = 0
    if array:
        for i in range(len(array)):
            for j in range(len(array[0])):
                # 从左上角卡开始，如果有1，就开始进行DFS，然后把DFS找到的1全部变成0，
                # 由于这些用DFS找到的都属于ij，所以只在开头计数就可以了
                # 依次扫描全表，确认每个1群都被技计数并消除
                if array[i][j] == 1:
                    count += 1
                    island_core(array, i, j)
    return count


def island_core(array, i, j):
    # 不超边界并且为1，就说明群还可以扩大
    # 为0直接返回，说明到这个1群的某一个边界
    if boundary_check(array, i, j) and array[i][j] == 1:
        array[i][j] = 0
        # 继续与1联通的其他1
        island_core(array, i+1, j)
        island_core(array, i-1, j)
        island_core(array, i, j+1)
        island_core(array, i, j-1)
    return


def boundary_check(array, i, j):
    return True if 0 <= i < len(array) and 0 <= j < len(array[0]) else False


# print(find_island([[0,0,1,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,0,0,0]]))


# O->X, 一个二维数组，全是X和O，当多个O被X包围时，这一群O就被吃掉，变为X，
# 边界上的O不会被吃掉，与边界上的O以直线形式相连的O群也不会被吃掉

'''
首先找到边界上的O，然后BFS这些O，将由边界产生的O群标志为*，*代表安全O
边界扫描完毕后，开始全表扫描，此时遇见的O就可以直接变成x，同时把*变回O。
'''


def o_to_x(array):
    if not array:
        return array
    x = -1
    while x+1 < len(array[0]):
        x += 1
        if array[0][x] == 'O':
            DFS(array, 0, x)

    y = 0
    while y+1 < len(array):
        y += 1
        if array[y][x] == 'O':
            DFS(array, y, x)
    if y > 1 and x > 0:
        while x-1 > -1:
            if array[y][x-1] == '0':
                DFS(array, y, x-1)
            x -= 1

        while y-1 > 0:
            if array[y-1][x+1] == 'O':
                DFS(array, y-1, x+1)
            y -= 1

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 'O':
                array[i][j] = 'X'
            elif array[i][j] == '*':
                array[i][j] = 'O'
    return array


def DFS(array, i, j):
    if boundary_check(array, i, j) and array[i][j] == 'O':
        array[i][j] = '*'
        DFS(array, i-1, j)
        DFS(array, i+1, j)
        DFS(array, i, j-1)
        DFS(array, i, j+1)
    return

# print(o_to_x([['X'],['X'],['X'],['O']]))
#               # ['O','O','X','X'],
#               # ['X','O','O','X'],
#               # ['X','X','X','X']]))


# 机器人最多能进入的格子个数，一个m*n的矩阵，当m和n每一位相加大于obstacle时，机器人不准进入该格
'''
机器人从00出发，然后用DFS从四个方向深入，因为要统计能到达的个数还要有一个数组存放已遍历过的坐标，
每次得到新的坐标都要判断，是否越界,是否已经访问过，是否和超过obstacle，都满足才能继续累加以及DFS
'''


def reachable_count(array, obstacle):
    count = 0
    if array and obstacle > -1:
        visited = [None]*len(array)*len(array[0])
        count = reachable_core(array, 0, 0, visited, count, obstacle)
    return count


def reachable_core(array, i, j, visited, count, ob):
    if _check(array, i, j, ob) and visited[i*len(array[0]+j)] is None:
        visited[i*len(array[0]+j)] = True
        count += 1
        count = reachable_core(array, i+1, j, visited, count, ob)
        count = reachable_core(array, i-1, j, visited, count, ob)
        count = reachable_core(array, i, j-1, visited, count, ob)
        count = reachable_core(array, i, j+1, visited, count, ob)
    return count


def _check(array, i, j, ob):
    res = False
    if 0 <= i < len(array) and 0 <= j < len(array[0]):
        sm = 0
        while i > 0:
            sm += i % 10
            i //= 10
        while j > 0:
            sm += j % 10
            j //= 10
        if sm <= ob:
            res = True
    return res








