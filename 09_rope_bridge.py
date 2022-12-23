from collections import namedtuple, deque
from typing import Literal, Set
import os

Point = namedtuple("Point", "x y")
Diff = namedtuple("Diff", "x y")


class Rope:
    def __init__(self, head: Point, tail: Point):
        self.head = head
        self.tail = tail
        self.visited: Set[Point] = set()
        self.visited.add(self.tail)

    def __repr__(self):
        return f"rope with head {self.head} and tail {self.tail}"

    def add_tail_to_visited(self):
        self.visited.add(self.tail)


    def dist_between(self):
        x_diff = self.head.x - self.tail.x
        y_diff = self.head.y - self.tail.y
        return Diff(x_diff, y_diff)


    def move(self, inst: Literal["U", "D", "L", "R"]):
        if inst == "R":
            self.head = Point(self.head.x + 1, self.head.y)
        elif inst == "L":
            self.head = Point(self.head.x - 1, self.head.y)
        elif inst == "U":
            self.head = Point(self.head.x, self.head.y + 1)
        elif inst == "D":
            self.head = Point(self.head.x, self.head.y - 1)


        diff = self.dist_between()

        if diff == Diff(0, 0):
            print("no diff")
        elif diff == Diff(2, 0):
            self.tail = Point(self.tail.x + 1, self.tail.y)
        elif diff == Diff(-2, 0):
            self.tail = Point(self.tail.x -1, self.tail.y)
        elif diff == Diff(0, 2):
            self.tail = Point(self.tail.x, self.tail.y + 1)
        elif diff == Diff(0, -2):
            self.tail = Point(self.tail.x, self.tail.y - 1)
        elif diff == Diff(2, 1) or diff == Diff(1, 2):
            self.tail = Point(self.tail.x + 1, self.tail.y + 1)
        elif diff == Diff(-2, 1) or diff == Diff(-1, 2):
            self.tail = Point(self.tail.x - 1, self.tail.y + 1)
        elif diff == Diff(2, -1) or diff == Diff(1, -2):
            self.tail = Point(self.tail.x + 1, self.tail.y - 1)
        elif diff == Diff(-2, -1) or diff == Diff(-1, -2):
            self.tail = Point(self.tail.x - 1, self.tail.y - 1)
        else:
            print("nothing to do")    

        self.add_tail_to_visited()
        return


def generate_instructions(data):
    instructions = data.split("\n")
    # remove trailing empty string
    instructions = instructions[:-1]
    parsed_instructions = [ x.split(" ")[0] * int(x.split(" ")[1]) for x in instructions]
    final_instructions = deque("".join(parsed_instructions))
    return final_instructions



def run_part_1(sample_or_real: Literal["sample", "real"]):
    if sample_or_real == "sample":
        whichfile = "sample09.txt"
    elif sample_or_real == "real":
        whichfile = "problem09.txt"
    else:
        raise ValueError("invalid func call param - must be real or sample")

    file = os.path.join("input_files", whichfile)

    with open(file, "r") as f:
        data = f.read()

    head = Point(0, 0)
    tail = Point(0, 0)

    rope = Rope(head, tail)
    instructions = generate_instructions(data)

    while len(instructions) > 0:
        command = instructions.popleft()
        print(command)
        rope.move(command)

    print(rope.visited)
    num_visited = len(rope.visited)
    print(f"the answer is {num_visited}")

def run_part_2(sample_or_real: Literal["sample", "real"]):
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
        run_part_2("real")
