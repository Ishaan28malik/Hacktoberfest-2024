def definition(args):
    list_patterns, list_range = [], range(4)
    for i in list_range:
        for j in list_range:
            list_patterns.append([args[i][j], args[i][j+1], args[i][j+2],
                                  args[i+1][j+1], args[i+2][j], args[i+2][j+1], args[i+2][j+2]])
    return list_patterns


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = max([sum(list_patt) for list_patt in definition(arr)])
    print(result)
