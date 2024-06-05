#!/usr/bin/python3
def pascal_triangle(n):
    matrix = []
    
    if n == 0:
        return matrix
    elif n == 1:
        return matrix[[1]]
    else:
        for i in range(1, n):
            tmp = [1]
            for j in range(len(matrix[i-1])-1):
                curr = matrix[i-1]
                tmp.append(curr[j] + curr[j+1])
        tmp.append(1)
        matrix.append(tmp)
    return matrix    