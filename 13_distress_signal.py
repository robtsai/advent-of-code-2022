import os
import pprint
import math
import copy

filemap = {"sample": "sample13.txt", "real": "problem13.txt"}

# we use a booleanstack 1 is True, -1 is False
# so we can keep track of if we ever saw a True or False
# in our stack of comparisons, and we can 
# return out of our comparison function early
# and if we don't see either True or False, ie maybe
# we return out of the recursive call but without setting
# true or false in the stack

class Pair():
    def __init__(self, left, right):
        self.left = left
        self.right = right


    def compare(self, booleanstack):
        if 1 in booleanstack:
            return True
        elif -1 in booleanstack:
            return False
        elif isinstance(self.left, int) and isinstance(self.right, int):
            if self.left < self.right:
                booleanstack.append(1)
                return True
            elif self.left > self.right:
                booleanstack.append(-1)
                return False
            else:
                # we could add a zero here to indicate a tie but it's unnecessary
                booleanstack.append(0)    
                return
        elif isinstance(self.left, list) and isinstance(self.right, list):
            print("both are lists")
            if len(self.left) == 0 and len(self.right) == 0:
                return
            elif len(self.left) == 0:
                print("left finished first, true")
                booleanstack.append(1)
                return True
            elif len(self.right) == 0:
                print("right finished first, false)")
                booleanstack.append(-1)
                return False
            l = self.left[0]
            r = self.right[0]
            lremain = self.left[1:] if len(self.left) > 1 else []
            rremain = self.right[1:] if len(self.right) > 1 else []
            print(f"newleft {l}, newright{r} and {lremain}, {rremain}")
            headpair = Pair(l, r)
            tailpair = Pair(lremain, rremain)

            headpair.compare(booleanstack)
            if 1 in booleanstack:
                return True
            elif -1 in booleanstack:
                return False

            tailpair.compare(booleanstack)
            if 1 in booleanstack:
                return True
            elif -1 in booleanstack:
                return False

        elif isinstance(self.left, int) and isinstance(self.right, list):
            newleft = [self.left]
            newpair = Pair(newleft, self.right)

            newpair.compare(booleanstack)
            if 1 in booleanstack:
                return True
            elif -1 in booleanstack:
                return False
        elif isinstance(self.right, int) and isinstance(self.left, list):
            newright = [self.right]
            newpair = Pair(self.left, newright)
            newpair.compare(booleanstack)
            if 1 in booleanstack:
                return True
            elif -1 in booleanstack:
                return False



    def __repr__(self):
        return f"left: {self.left};\t right: {self.right}"



def run_part_1(sample_or_real):
    file = os.path.join("input_files", filemap[sample_or_real])
    with open(file, "r") as f:
        data = f.read()
    firstsplit = data.split("\n\n")
    allpairs = []
    for entry in firstsplit:
        left, right = entry.split("\n")
        evalleft = eval(left)
        evalright = eval(right)
        pair = Pair(evalleft, evalright)
        allpairs.append(pair)

    print(allpairs)
    right_order = []
    for i, pair in enumerate(allpairs, start=1):
        print(f"comparing index {i} pair {pair}")
        if pair.compare(booleanstack=[]):
            print(f"index {i} in good order with pair {pair}")
            right_order.append(i)

    print(right_order)
    print(sum(right_order))


def run_part_2(sample_or_real):
    with open(file, "r") as f:
        data = f.read()
    print(data)


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
        # run_part_2("real")
