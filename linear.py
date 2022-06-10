#Linear Tool

def identity(n):
    retVal = [[0] * n for _ in range(n)]
    for i in range(n):
        retVal[i][i] = 1
    return retVal


def multiply(m, n):
    retVal = [[0] * len(m) for _ in range(len(n[0]))]

    for i in range(len(retVal)):
        for j in range(len(retVal[0])):
            sum = 0
            for x in range(len(m[0])):
                sum += m[i][x]*n[x][j]
            retVal[i][j] = sum

    return retVal


def multiply_intermediate(m, n):
