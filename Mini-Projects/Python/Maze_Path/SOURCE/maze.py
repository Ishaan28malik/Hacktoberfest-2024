from collections import deque
from heapq import heappop, heappush
import optparse


def _idx_dec(row, col):
    return row + col * n


def _idx_enc(index):
    """
    :param index:
    :return row, col:
    """
    return index % n, index // n


def path_backtrack(dp_path, start, goal):
    path = []

    def path_travelsal(s, f):
        nonlocal path
        gx, gy = _idx_enc(f)
        sx, sy = _idx_enc(s)
        if s == f:
            path.append(f)
        else:
            if dp_path[gx][gy] == -1:
                path.append(-1)
            else:
                path_travelsal(s, dp_path[gx][gy])
                path.append(f)

    path_travelsal(start, goal)
    return path


def bfs(graph, start, goal):
    dp_path = [[-1 for _ in range(n)] for _ in range(n)]
    explorered_node = []
    q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    sx, sy = _idx_enc(start)
    q.append(start)
    visited[sx][sy] = True
    time = 0
    while q:
        top = q.popleft()
        time += 1
        explorered_node.append(top)
        tr, tc = _idx_enc(top)
        if top == goal:
            break
        for neighbor in sorted(graph[tr][tc]):
            nr, nc = _idx_enc(neighbor)
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dp_path[nr][nc] = top
                q.append(neighbor)

    path = path_backtrack(dp_path, start, goal)
    return path, explorered_node, time


def ucs(graph, start, goal):
    dp_path = [[-1 for _ in range(n)] for _ in range(n)]
    dist = [[INF for _ in range(n)] for _ in range(n)]
    explorered_node = []
    pq = [(0, start)]
    sx, sy = _idx_enc(start)
    dist[sx][sy] = 0
    time = 0
    while pq:
        pri, top = heappop(pq)
        time += 1
        explorered_node.append(top)
        tr, tc = _idx_enc(top)
        if top == goal:
            break
        for neighbor in sorted(graph[tr][tc]):
            nr, nc = _idx_enc(neighbor)
            if dist[nr][nc] > dist[tr][tc] + 1:
                dist[nr][nc] = dist[tr][tc] + 1
                dp_path[nr][nc] = top
                heappush(pq, (dist[nr][nc], neighbor))

    path = path_backtrack(dp_path, start, goal)
    return path, explorered_node, time


def manhattan_L1_distance(s, f):
    sx, sy = _idx_enc(s)
    fx, fy = _idx_enc(f)
    return abs(sx - fx) + abs(sy - fy)

def gbfs(graph, start, goal):
    dp_path = [[-1 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    explorered_node = []
    pq = [(manhattan_L1_distance(start, goal), start)]
    sx, sy = _idx_enc(start)
    visited[sx][sy] = True
    time = 0
    while pq:
        pri, top = heappop(pq)
        time += 1
        explorered_node.append(top)
        tr, tc = _idx_enc(top)
        if top == goal:
            break
        for neighbor in sorted(graph[tr][tc]):
            nr, nc = _idx_enc(neighbor)
            h = manhattan_L1_distance(neighbor, goal)
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dp_path[nr][nc] = top
                heappush(pq, (h, neighbor))
    path = path_backtrack(dp_path, start, goal)

    return path, explorered_node, time


def dls(graph, start, goal, limit):
    dp_path = [[-1 for _ in range(n)] for _ in range(n)]
    explorered_node = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    cost = 0

    def dls_recusive(_start, _goal, _limit):
        nonlocal explorered_node, cost, dp_path
        sx, sy = _idx_enc(_start)
        explorered_node.append(_start)
        visited[sx][sy] = True
        cost += 1
        if _start == _goal:
            return True
        if _limit == 0:
            return False
        for neighbor in sorted(graph[sx][sy]):
            nr, nc = _idx_enc(neighbor)
            if not visited[nr][nc]:
                ans = dls_recusive(neighbor, _goal, _limit - 1)
                visited[nr][nc] = True
                dp_path[nr][nc] = _start
                if ans:
                    return True
        return False

    res = dls_recusive(start, goal, limit)
    path = path_backtrack(dp_path, start, goal)

    return path, explorered_node, cost, res


def ids(graph, start, goal):
    explorered_node = []
    limit = 0
    total_cost = 0
    preex = []
    while True:
        path, exnode, cost, is_found = dls(graph, start, goal, limit)
        limit += 1
        if preex == exnode:
            break
        explorered_node.append(exnode)
        total_cost += cost
        if is_found:
            break
        preex = exnode
    return path, explorered_node, total_cost


def astar(graph, start, goal):
    dp_path = [[-1 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    dist = [[INF for _ in range(n)] for _ in range(n)]

    explorered_node = []
    pq = [(manhattan_L1_distance(start, goal) + 0, start)]

    sx, sy = _idx_enc(start)
    dist[sx][sy] = 0
    visited[sx][sy] = True
    time = 0
    while pq:
        pri, top = heappop(pq)
        time += 1
        explorered_node.append(top)
        tr, tc = _idx_enc(top)
        # explorered_node.append((top, f"h =  {manhattan_L1_distance(top, goal)}", f"g = {dist[tr][tc]}"))

        if top == goal:
            break
        for neighbor in sorted(graph[tr][tc]):
            nr, nc = _idx_enc(neighbor)
            h = manhattan_L1_distance(neighbor, goal)
            g = dist[nr][nc] = dist[tr][tc] + 1
            if not visited[nr][nc]:
                visited[nr][nc] = True
                dp_path[nr][nc] = top
                heappush(pq, (h + g, neighbor))

    path = path_backtrack(dp_path, start, goal)

    return path, explorered_node, time


def result_view(function, name, _graph, _start_point,
                _exit_point):
    path, exed_node, cost = function(_graph, _start_point, _exit_point)
    if isOutFile:
        O(name+"\n")
        O(f"Start: {_start_point} | Goal: {_exit_point}\n")
        O(str("Path:" + f"{path if path[-1] != -1 else 'No path'}" +
              f"| Cost {(len(path) - 1) if path[-1] != -1 else 0}" + "\n"))
        O("Explored node: " + f"{exed_node} " + f"| Time {cost}" + "\n")
        print(f"Result of {name} saved to", outpath)
    else:
        print(name)
        print(f"Start: {_start_point} | Goal: {_exit_point}")
        print("Path:", path if path[-1] != -1 else "No path",
          f"| Cost {(len(path) - 1) if path[-1] != -1 else 0}")
        print("Explored node:", exed_node, f"| Time {cost}")



if __name__ == "__main__":
    # parser for testing bash + cooler report :)
    import os
    usage = "usage: %prog [option] [argument] | by default, the input and output will be stdin and stdout."
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-i', help='<input file directory>', dest='infile', action='store')
    parser.add_option('-o', help='<out file directory>', dest='outfile', action='store')

    (opts, args) = parser.parse_args()
    isInFile = False
    isOutFile = False
    parent_inpath ,inpath = os.path.split(str(opts.infile))
    inpath = str(os.path.realpath(parent_inpath)) + r"/" + inpath
    parent_outpath ,outpath = os.path.split(str(opts.outfile))
    outpath = str(os.path.realpath(parent_outpath)) + r"/" + outpath
    I = None
    O = None
    if os.path.isfile(inpath):
        fin = open(inpath)
        isInFile = True
        I = fin.readline
    if os.path.isdir(parent_outpath):
        fout = open(outpath, "w")
        isOutFile = True
        O = fout.write
    if isInFile:
        n = int(I())
    else:
        n = int(input())
    start_point = 0
    maze_size = n * n
    graph = [[[] for  _ in range(n)] for _ in range(n)]
    for j in range(n):
        for i in range(n):
            index = _idx_dec(i, j)
            if isInFile:
                adj_list = list(map(int, I().split()))
            else:
                adj_list = list(map(int, input().split()))
            for element in adj_list:
                graph[i][j].append(element)
    if isInFile:
        exit_point = int(I())
    else:
        exit_point = int(input())

    INF = (n * n + 2)
    result_view(function=bfs, name="BFS", _graph=graph,
                _start_point=start_point, _exit_point=exit_point)

    result_view(function=ucs, name="UCS", _graph=graph,
                _start_point=start_point, _exit_point=exit_point)

    result_view(function=gbfs, name="GBFS", _graph=graph,
                _start_point=start_point, _exit_point=exit_point)

    result_view(function=ids, name="IDS", _graph=graph,
                _start_point=start_point, _exit_point=exit_point)

    result_view(function=astar, name="A-star", _graph=graph,
                _start_point=start_point, _exit_point=exit_point)
