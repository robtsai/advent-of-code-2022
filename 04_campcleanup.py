# part 1

from dataclasses import dataclass



class Pairs:
    def __init__(self, l_low: int, l_high: int, r_low: int, r_high: int):
        self.l_low = l_low
        self.l_high = l_high
        self.r_low = r_low
        self.r_high = r_high


    def one_contains_other(self) -> bool:
        # left contains right
        if self.l_low <= self.r_low and self.l_high >= self.r_high:
            print("left contains right")
            return True
        # right contains left
        elif self.r_low <= self.l_low and self.r_high >= self.l_high:
            print("right contains left")
            return True
        else:
            print("no overlap")
            return False


    def any_overlap(self) -> bool:
        if self.l_high < self.r_low:
            return False
        elif self.r_high < self.l_low:
            return False
        else:
            return True



    def __repr__(self):
        return f"pair: left ({self.l_low}, {self.l_high})\t right: ({self.r_low}, {self.r_high})"


def run_part_1(real_or_sample):
    if real_or_sample == "real":
        filename = "problem04.txt"
    elif real_or_sample == "sample":
        filename = "sample04.txt"

    total = 0
    with open(f"input_files/{filename}", "r") as f:
        for line in f:
            clean_line = line.replace("\n", "")
            left, right = clean_line.split(",")
            print(left, right)
            l_low, l_high = left.split("-")
            r_low, r_high = right.split("-")
            pair = Pairs(int(l_low), int(l_high), int(r_low), int(r_high))
            print(pair)
            contains = pair.one_contains_other()
            print(contains)
            if contains:
                total += 1
                print(total)

            print("--------------------------\n")
            print("\n" * 2)


    print(f"the answer to part 1 is {total}")


def run_part_2():
    total = 0
    with open(f"input_files/problem04.txt", "r") as f:
        for line in f:
            clean_line = line.replace("\n", "")
            left, right = clean_line.split(",")
            print(left, right)
            l_low, l_high = left.split("-")
            r_low, r_high = right.split("-")
            pair = Pairs(int(l_low), int(l_high), int(r_low), int(r_high))
            print(pair)
            overlaps = pair.any_overlap()
            print(overlaps)
            if overlaps:
                total += 1
                print(total)

            print("--------------------------\n")
            print("\n" * 2)


    print(f"the answer to part 2 is {total}")


if __name__ == "__main__":
    while True:
        which_one_to_run = input("which part to run? enter 1 or 2:\n")
        if which_one_to_run in ("1", "2"):
            print("good choice")
            break

    if which_one_to_run == "1":
        run_part_1("real")
    else:
        run_part_2()
