tablet = [['T', 'E', 'N'],
          ['E', 'Y', 'E'],
          ['N', 'E', 'T']]
tablet = [['S', 'A', 'L', 'A', 'S'],
                  ['A', 'R', 'E', 'N', 'A'],
                  ['L', 'E', 'V', 'E', 'L'],
                  ['A', 'R', 'E', 'N', 'A'],
                  ['S', 'A', 'L', 'A', 'S']]

def is_sator_square(tablet):
    A = {''.join(lst) for lst in tablet}
    B = {''.join(lst)[::-1] for lst in tablet}
    C = {''.join(lst) for lst in zip(*tablet)}
    D = {''.join(lst)[::-1] for lst in zip(*tablet)}
    return A == B == C == D

def is_sator_square(tablet):

    left_to_right = {''.join(row) for row in tablet}
    top_to_bottom = {''.join(col) for col in zip(*tablet)}
    right_to_left = {''.join(row[::-1]) for row in tablet}
    bottom_to_top = {''.join(col[::-1]) for col in zip(*tablet)}

    return left_to_right == right_to_left == top_to_bottom == bottom_to_top
def is_sator_square(tablet):
    n=len(tablet)
    for i in range(n):
        for j in range(n):
            if tablet[i][j] != tablet[j][i] or tablet[i][j] != tablet[n - i - 1][n - j - 1]:
                return False
    return True

def is_sator_square(tablet):
    return tablet == [t[::-1] for t in tablet][::-1] == list(map(list, zip(*tablet)))


import numpy as np

def is_sator_square(tablet):
    x = np.array(tablet)
    y = np.array(tablet)
    
    for i in range(4):
        y = np.rot90(y)
        x = x[::-1]
        if not (y==x).all():
            return False
    return True