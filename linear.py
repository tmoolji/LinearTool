# Linear Tool

# parameters: size, n
# returns: an identity matrix of size n
def identity(n):
    retVal = [[0] * n for _ in range(n)]
    for i in range(n):
        retVal[i][i] = 1
    return retVal


# parameters: two matricies m, n to be multiplied.
# returns: the result of multipling m and n
# Must be the case that len(m[0]) == len(n)
def multiply(m, n):
    retVal = [[0] * len(m) for _ in range(len(n[0]))]

    for i in range(len(retVal)):
        for j in range(len(retVal[0])):
            sum = 0
            for x in range(len(m[0])):
                sum += m[i][x]*n[x][j]
            retVal[i][j] = sum

    return retVal

# parameters: two matricies m, n to be multiplied.
# returns: a 1D array that lists the sums in each cell
# Must be the case that len(m[0]) == len(n)
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


# parameters: input matrix, "input"
# returns: tranpose of input matrix
def transpose(input):
    num_rows = len(input)
    num_cols = len(input[0])
    tranposed_matrix = []
    for col_num in range(num_cols):
        tranposed_matrix += [[input[row_num][col_num] for row_num in range(num_rows)]]

    return tranposed_matrix

# parameters: input matrix, "input"
#            row to be added, "n"
#            row you are adding to, and storing new values in, "m"
#            scalar that each element in n is multiplied by before adding to m, "scalar"
# returns: modified input array
def add_row(input, n, m, scalar):
    for i in range(len(input[0])):
        input[m][i] += scalar*input[n][i]

    return input



def gaussian_elim_down(input, solution, n):
    for i in range(n+1, len(input)):
        divisor = input[n][n] /
        for j in range (n, len(input[0])):

# parameters: input matrix in row echelon form back substituted from len-1 to n, "input"
#             solution matrix in row echelon form back substituted from len-1 to n, "output"
#             row to be added, "n"
# returns: modified input and output such that they are in row echelon form back substituted from len-1 to n-1
def gaussian_elim_up(input, output, n):
    for i in range(len(input)-1, n-2):
        scalar = input[n-1][i]/input[i][i]
        input = add_row(input, i, n-1, scalar)
        output = add_row(output, i, n-1, scalar)

    return input, output



def guassian_elim():
