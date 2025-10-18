import heapq
import copy


def md(b):
    count = 0
    for i in range(3):
        for j in range(3):
            if b[i][j] != 0:
                count += abs(i-pos[b[i][j]][0])+abs(j-pos[b[i][j]][1])
    return count


def isSuccess(b):
    for i in range(3):
        for j in range(3):
            if b[i][j] != ENDSTATE[i][j]:
                return False
    return True


def genSwap(b, x1, y1, x2, y2):
    t = copy.deepcopy(b)
    t[y1][x1], t[y2][x2] = t[y2][x2], t[y1][x1]
    return t


def left(b, t1, t2):
    nb = genSwap(b, t1, t2, t1-1, t2)
    heapq.heappush(Q, (md(nb), nb, t1-1, t2))


def right(b, t1, t2):
    nb = genSwap(b, t1, t2, t1+1, t2)
    heapq.heappush(Q, (md(nb), nb, t1+1, t2))


def up(b, t1, t2):
    nb = genSwap(b, t1, t2, t1, t2-1)
    heapq.heappush(Q, (md(nb), nb, t1, t2-1))


def down(b, t1, t2):
    nb = genSwap(b, t1, t2, t1, t2+1)
    heapq.heappush(Q, (md(nb), nb, t1, t2+1))


def print_puzzle(b):
    print('\n ----------- \n'.join(['  '+' | '.join(map(str, i)) for i in b]), '\n')
    
STARTSTATE = [[1, 2, 0], [4, 6, 3], [7, 5, 8]]
ENDSTATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
Q = []
M = dict()
pos = dict()
for i in range(3):
    for j in range(3):
        pos[ENDSTATE[i][j]] = (i, j)
t1 = t2 = 0
for i in range(3):
    for j in range(3):
        if STARTSTATE[i][j] == 0:
            t2, t1 = i, j
heapq.heapify(Q)
heapq.heappush(Q, (md(STARTSTATE), STARTSTATE, t1, t2))
while Q:
    cur = heapq.heappop(Q)
    b, t1, t2 = cur[1], cur[2], cur[3]
    print_puzzle(b)
    if isSuccess(b):
        break
    if t1 == 0 and t2 == 0:
        right(b, t1, t2)
        down(b, t1, t2)
    elif t1 == 2 and t2 == 0:
        left(b, t1, t2)
        down(b, t1, t2)
    elif t1 == 0 and t2 == 2:
        up(b, t1, t2)
        right(b, t1, t2)
    elif t1 == 2 and t2 == 2:
        up(b, t1, t2)
        left(b, t1, t2)
    elif t1 == 0:
        up(b, t1, t2)
        right(b, t1, t2)
        down(b, t1, t2)
    elif t1 == 2:
        up(b, t1, t2)
        left(b, t1, t2)
        down(b, t1, t2)
    elif t2 == 0:
        left(b, t1, t2)
        down(b, t1, t2)
        right(b, t1, t2)
    elif t2 == 2:
        left(b, t1, t2)
        up(b, t1, t2)
        right(b, t1, t2)
    else:
        up(b, t1, t2)
        down(b, t1, t2)
        right(b, t1, t2)
        left(b, t1, t2)
