#Linear Tool

def identity(n):
    retVal = [0] * n * n
    for i in range(n):
        retval[i][i] = 1
    return retVal



def transpose(input):
    num_rows = len(input)
    num_cols = len(input[0])
    x = []
    for i in range(num_cols):
        x += [[input[m][i] for m in range(num_rows)]]

    return x


def guassian_elim()