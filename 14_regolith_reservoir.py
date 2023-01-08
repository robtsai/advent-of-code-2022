import os
import pprint
import math
import copy
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Sand = namedtuple("Sand", ["x", "y"])


filemap = {"sample": "sample14.txt", "real": "problem14.txt"}


def min_max(line):
    """returns min and max x and y as tuple"""
    points = line.split(" -> ")
    min_x = min(int(point.split(",")[0]) for point in points)
    max_x = max(int(point.split(",")[0]) for point in points)
    max_y = max(int(point.split(",")[1]) for point in points)

    return min_x, max_x, max_y


class Waterfall:
    def __init__(self, min_x, max_x, max_y, lines):
        self.min_x = min_x
        self.max_x = max_x
        self.max_y = max_y
        self.lines = lines
        self.linesp = [self.lines_as_points(line) for line in self.lines]
        self.x_size = max_x - min_x + 1
        self.sands = []
        self.rocks = self.get_rocks()
        self.blocked = self.rocks
        self.board = self._build_board()
        self.free = self.get_free()

    def _build_board(self):
        b = [["." for _ in range(self.x_size)] for _ in range(self.max_y + 1)]
        for rock in self.rocks:
            b[rock.y][self.x_offset(rock.x)] = "#"
        for sand in self.sands:
            b[sand.y][self.x_offset(sand.x)] = "o"
        return b
    

    def _update_board(self, sand):
       self.board[sand.y][self.x_offset(sand.x)] = "o"


    def print_board(self):
        headers = self._headers()
        pp = pprint.PrettyPrinter(indent=4)
        header_board = headers + self.board
        pp.pprint(["".join(row) for row in header_board])

    def _headers(self):

        hmap = {
            0: str(self.min_x),
            self.x_size - 1: str(self.max_x),
            500 - self.min_x: str(500),
        }

        headers = []

        for i in range(3):
            header = []
            for j in range(self.x_size):
                if j in hmap:
                    header.append(hmap[j][i])
                else:
                    header.append(" ")
            headers.append(header)

        return headers

    def lines_as_points(self, line):
        entries = line.split(" -> ")
        points = []
        for entry in entries:
            x, y = entry.split(",")
            p = Point(int(x), int(y))
            points.append(p)
        return points

    def fill_points(self, a, b):
        """
        a,b are points - returns list of points endpoint inclusive
        """
        points = []
        if a.x == b.x:
            if a.y <= b.y:
                for j in range(a.y, b.y + 1):
                    p = Point(a.x, j)
                    points.append(p)
            else:
                for j in range(a.y, b.y - 1, -1):
                    p = Point(a.x, j)
                    points.append(p)
        else:
            if a.x <= b.x:
                for i in range(a.x, b.x + 1):
                    p = Point(i, a.y)
                    points.append(p)
            else:
                for i in range(a.x, b.x - 1, -1):
                    p = Point(i, a.y)
                    points.append(p)
        return points

    def get_rocks(self):
        rocks = set()
        for linep in self.linesp:
            index = 0
            while index < len(linep) - 1:
                points = self.fill_points(linep[index], linep[index + 1])
                rocks.update(points)
                index += 1
        return rocks

    def x_offset(self, x):
        return x - self.min_x

    def get_free(self):
        free = set()

        for y in range(self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                p = Point(x, y)
                free.add(p)

        for rock in self.rocks:
            free.remove(rock)

        return free

    def validpoint(self, point):
        if (
            point.x >= self.min_x
            and point.x <= self.max_x
            and point.y >= 0
            and point.y <= self.max_y
        ):
            return True
        return False

    def sandfall(self):
        sand = Point(500, 0)

        # keep falling
        while True:
            down = Point(sand.x, sand.y + 1)
            downleft = Point(sand.x - 1, sand.y + 1)
            downright = Point(sand.x + 1, sand.y + 1)

            if (
                down in self.blocked
                and downleft in self.blocked
                and downright in self.blocked
            ):
                break

            if (
                down in self.free):
                sand = Point(sand.x, sand.y+1)
                # move down one
                continue

            if (down in self.blocked and downleft in self.free):
                sand = downleft
                continue

            if (down in self.blocked and downright in self.free):
                sand = downright
                continue

            if (down in self.blocked) and not self.validpoint(downleft):
                sand = Point(-1, -1)
                break

            if (down in self.blocked) and not self.validpoint(downright):
                sand = Point(-1, -1)
                break

            # other infinite loop
            sand = Point(-1, -1)
            break

        return sand

    def simulate(self, sample_or_real):
        steps = 1
        while True:
            sand = self.sandfall()
            if sand == Point(-1, -1):
                print("reached infinite loop")
                break
            print(f"sand reached {sand} on step {steps}")
            self.sands.append(sand)
            self.free.remove(sand)
            self.blocked.add(sand)
            self._update_board(sand)
            if sample_or_real == "sample":
                self.print_board()

            steps += 1

        print(f"the answer is {steps-1}")





def run_part_1(sample_or_real):
    file = filemap[sample_or_real]
    with open(os.path.join("input_files", file), "r") as f:
        data = f.read()

    lines = data.split("\n")
    min_x = math.inf
    max_x = -math.inf
    max_y = -math.inf
    for line in lines:
        minx, maxx, maxy = min_max(line)
        min_x = min(min_x, minx)
        max_x = max(max_x, maxx)
        max_y = max(max_y, maxy)

    print(min_x, max_x, max_y)
    w = Waterfall(min_x, max_x, max_y, lines)
    if sample_or_real == "sample":
        w.print_board()
    w.simulate(sample_or_real)


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
