#!/usr/bin/python3
""" recursive Pascal triangle function """
def pascal_triangle(n):
    """ Returns a list of integers representing the Pascal triangle """
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        res = pascal_triangle(n-1)
        last_row = res[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        res.append(new_row)
    return res