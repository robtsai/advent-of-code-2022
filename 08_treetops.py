import os
import copy
import pprint
import operator
from functools import reduce

def get_matrix(data):
    rows = data.split("\n")
    # there is a lingering "" at the end of the list
    print(rows)
    clean_rows = rows[:-1]
    print(clean_rows)
    num_rows = len(clean_rows)
    num_cols = len(clean_rows[0])
    print(f"shape of data is rows: {num_rows} by cols: {num_cols}")

    empty_row = [None for _ in range(num_cols)]

    matrix = []
    for i in range(num_rows):
        matrix.append(copy.copy(empty_row))

    visible = copy.deepcopy(matrix)

    score = copy.deepcopy(matrix)

    # populate matrix, and also set visibible matrix to false
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            matrix[i][j] = int(val)
            visible[i][j] = False
            score[i][j] = None

    return matrix, visible, num_rows, num_cols, score



def left_to_right(matrix, visible, num_rows, num_cols):
    for i in range(num_rows):
        highest = -1
        for j in range(num_cols):
            if matrix[i][j] > highest:
                # can see this tree
                visible[i][j] = True
                highest = matrix[i][j]
    return

def right_to_left(matrix, visible, num_rows, num_cols):
    for i in range(num_rows):
        highest = -1
        for j in range(num_cols-1, -1, -1):
            if matrix[i][j] > highest:
                # can see this tree
                visible[i][j] = True
                highest = matrix[i][j]
    return


def top_to_bottom(matrix, visible, num_rows, num_cols):
    for j in range(num_cols):
        highest = -1
        for i in range(num_rows):
            if matrix[i][j] > highest:
                visible[i][j] = True
                highest = matrix[i][j]
    return


def bottom_to_top(matrix, visible, num_rows, num_cols):
    for j in range(num_cols):
        highest = -1
        for i in range(num_rows-1, -1, -1):
            if matrix[i][j] > highest:
                visible[i][j] = True
                highest = matrix[i][j]
    return



def count_vis(matrix, i, j, num_rows, num_cols):
    factors = {
        "left": 0,
        "right": 0,
        "up": 0,
        "down": 0
    }

    curval = matrix[i][j]

    left = j-1
    numleft = 0
    while left >= 0:
        numleft += 1
        if matrix[i][left] >= curval:
            break
        left -= 1
    factors["left"] = numleft

    right = j+1
    numright = 0
    while right < num_cols:
        numright += 1
        if matrix[i][right] >= curval:
            break
        right += 1
    factors["right"] = numright

    up = i-1
    numup = 0
    while up >= 0:
        numup += 1
        if matrix[up][j] >= curval:
            break
        up -= 1
    factors["up"] = numup

    down = i+1
    numdown = 0
    while down < num_rows:
        numdown += 1
        if matrix[down][j] >= curval:
            break
        down += 1
    factors["down"] = numdown

    print(factors)
    factor_vals = list(factors.values())
    print(factor_vals)
    the_score = reduce(operator.mul, factor_vals)
    print(the_score)
    return the_score



def run_part_1(sample_or_real):
    if sample_or_real == "sample":
        whichfile = "sample08.txt"
    elif sample_or_real == "real":
        whichfile = "problem08.txt"
    else:
        raise ValueError("invalid func call param - must be real or sample")
    
    file = os.path.join("input_files", whichfile)

    with open(file, "r") as f:
        data = f.read()

    matrix, visible, num_rows, num_cols, _ = get_matrix(data)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(matrix)
    pp.pprint(visible)

    left_to_right(matrix, visible, num_rows, num_cols)
    pp.pprint(visible)
    
    right_to_left(matrix, visible, num_rows, num_cols)
    pp.pprint(visible)

    top_to_bottom(matrix, visible, num_rows, num_cols)
    pp.pprint(visible)

    bottom_to_top(matrix, visible, num_rows, num_cols)
    pp.pprint(visible)

    counts = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if visible[i][j]:
                counts += 1

    print(f"the answer to part 1 is {counts}")




def run_part_2(sample_or_real):
    if sample_or_real == "sample":
        whichfile = "sample08.txt"
    elif sample_or_real == "real":
        whichfile = "problem08.txt"
    else:
        raise ValueError("invalid func call param - must be real or sample")

    file = os.path.join("input_files", whichfile)
    with open(file, "r") as f:
        data = f.read()

    matrix, visible, num_rows, num_cols, score = get_matrix(data)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(matrix)
    pp.pprint(score)


    highest_score = 0

    for i in range(1, num_rows-1):
        for j in range(1, num_cols-1):
            curval = matrix[i][j]
            the_score = count_vis(matrix, i, j, num_rows, num_cols)
            highest_score = max(highest_score, the_score)

    print(f"the answer to part 2 is {highest_score}")


    


if __name__ == "__main__":
    while True:
        which_one_to_run = input("which part to run? enter 1 or 2:\n")
        if which_one_to_run in ("1", "2"):
            print("good choice")
            break

    if which_one_to_run == "1":
        run_part_1("sample")
        run_part_1("real")
    else:
        run_part_2("sample")
        run_part_2("real")