# part 1
import os
import re
from collections import deque


line_with_box_index = re.compile(" 1")
box_val = re.compile("\[([A-Z])\]")

instructions = re.compile("move (?P<qty>\d+) from (?P<from>\d{1}) to (?P<to>\d{1})")


def move(stack_dict, qty, m_from, m_to):
    qty = int(qty)
    m_from = int(m_from)
    m_to = int(m_to)
    counter = 0
    while counter < qty:
        pop_from = stack_dict[m_from].pop()
        stack_dict[m_to].append(pop_from)
        counter += 1
    return


def run_part_1(sample_or_real):
    if sample_or_real == "sample":
        whichfile = "sample05.txt"
    elif sample_or_real == "real":
        whichfile = "problem05.txt"
    else:
        raise ValueError("invalid func call param - must be real or sample")
    
    file = os.path.join("input_files", whichfile)

    stacks = {}


    with open(file, "r") as f:
        count_boxes = True

        for line in f:
            if line_with_box_index.match(line):
                count_boxes = False
                continue
            if count_boxes:
                boxes = box_val.finditer(line)
                for box in boxes:
                    indexpos = box.span()[0] // 4 + 1
                    if not indexpos in stacks:
                        newstack = deque()
                        newstack.appendleft(box.group())
                        stacks[indexpos] = newstack
                    else:
                        stacks[indexpos].appendleft(box.group())
                continue

            if instructions.match(line):
                m_qty = instructions.match(line).group("qty")
                m_from = instructions.match(line).group("from")
                m_to = instructions.match(line).group("to")
                print(f"stack is {stacks}")
                print(f"moving {m_qty} from {m_from} to {m_to}")
                move(stacks, m_qty, m_from, m_to)

    print(f"ending stacks: {stacks}")
    numkeys = max(stacks.keys())
    answer_list = []
    for i in range(1, numkeys+1):
        answer_list.append(stacks[i].pop())
    print(answer_list)
    answer = "".join(answer_list)
    print(answer.replace("[","").replace("]",""))

            



def run_part_2():
    pass


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
        run_part_2()