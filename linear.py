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
    retVal = [""] * len(m) * len(n[0])

    for i in range(len(m)):
        for j in range(len(n[0])):
            sums = "R" + str(i) + " C"+ str(j) +":"
            toAdd = ""
            for x in range(len(m[0])):
                toAdd += " + (" + str(m[i][x]) + " * " + str(n[x][j]) + ")"
            retVal[i*len(m) + j] = sums + toAdd[2:]
    return retVal



def transpose(input):
    num_rows = len(input)
    num_cols = len(input[0])
    x = []
    for i in range(num_cols):
        x += [[input[m][i] for m in range(num_rows)]]

    return x


def guassian_elim()