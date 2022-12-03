# part 1


# ord of a is 97, ord of A is 65

import re
lowercase = re.compile('[a-z]')
uppercase = re.compile('[A-Z]')


def calc_priority(element):
    if lowercase.match(element):
        print('lowercase')
        priority = ord(element) - ord('a') + 1
    elif uppercase.match(element):
        priority = ord(element) - ord('A') + 27
        print('uppercase')
    print(priority)
    return priority


def split_backpack(backpack):
    l = len(backpack)
    middle = l // 2
    first_half = backpack[:middle]
    second_half = backpack[middle:]
    print(first_half, second_half)
    first_set = set([char for char in first_half])
    second_set = set([char for char in second_half])
    print(first_set)
    print(second_set)
    in_both = first_set & second_set
    print(in_both)
    # use tuple unpacking to extract singleton member from set
    (element,) = in_both
    priority = calc_priority(element)
    return priority



def run_part_1():
    total = 0
    with open("input_files/problem03.txt", "r") as f:
        for line in f:
            clean_line = line.replace("\n", "")
            total += split_backpack(clean_line)
    print(f"the answer to part 1: {total}")


def convert_backpack_to_set(backpack):
    return set([char for char in backpack])

def run_part_2():
    # we need to split by groups of 3
    backpacks = []
    with open("input_files/problem03.txt", "r") as f:
        # start with empty backpack
        cur_backpack = []
        for i, line in enumerate(f):
            clean_line = line.replace("\n", "")
            if i % 3 == 2:
                cur_backpack.append(clean_line)
                backpacks.append(cur_backpack)
                cur_backpack = []
            else:
                cur_backpack.append(clean_line)
    
    total = 0
    for triplet in backpacks:
        triplet_sets = [ convert_backpack_to_set(x) for x in triplet]
        a, b, c = triplet_sets
        common_badge = a & b & c 
        print(common_badge)
        (element, ) = common_badge
        total += calc_priority(element)

    print(f"the answer to part 2 is {total}")
        



if __name__ == "__main__":
    while True:
        which_one_to_run = input("which part to run? enter 1 or 2:\n")
        if which_one_to_run in ("1", "2"):
            print("good choice")
            break

    if which_one_to_run == "1":
        run_part_1()
    else:
        run_part_2()