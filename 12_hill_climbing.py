import os
import pprint
import math
import copy

filemap = {"sample": "sample12.txt", "real": "problem12.txt"}


# djykstra's algorithm
# mark all unvisited nodes as max


class Board:
    def __init__(self, rows):
        self.rows = rows
        self.board = []
        self.start = (None, None)
        self.end = (None, None)
        self.distances = []
        self._initialize_board()
        self._initialize_distances()
        self.elevations = copy.deepcopy(self.board)
        self.elevations[self.start[0]][self.start[1]] = 'a'
        self.elevations[self.end[0]][self.end[1]] = 'z'
        self.visited = set()
        self.current = self.start
        self.numrows = len(self.board)
        self.numcols = len(self.board[0])
        self.visited.add(self.start)
        self.to_consider = {}


    def elevation(self):
        return self.elevations[self.current[0]][self.current[1]]

    def height_diff(self, point_a, point_b):
        elevation_a = self.elevations[point_a[0]][point_a[1]]
        elevation_b = self.elevations[point_b[0]][point_b[1]]
        return ord(elevation_a) - ord(elevation_b)


    def _initialize_board(self):
        numcols = len(self.rows[0])
        for i, row in enumerate(self.rows):
            newrow = []
            for j, char in enumerate(row):
                if char == "S":
                    self.start = (i, j)
                elif char == "E":
                    self.end = (i, j)
                newrow.append(char)
            self.board.append(newrow)

    def _initialize_distances(self):
        numcols = len(self.rows[0])
        for i, row in enumerate(self.rows):
            newrow = []
            for j, char in enumerate(row):
                newrow.append(math.inf)
            self.distances.append(newrow)
        self.distances[self.start[0]][self.start[1]] = 0

    def adjacent(self):
        """finds adjacent vertices - adds them to unvisited dict, with cost to get there
        """
        right = (self.current[0], self.current[1] + 1)
        left = (self.current[0], self.current[1] - 1)
        up = (self.current[0] - 1, self.current[1])
        down = (self.current[0] + 1, self.current[1])
        l = [right, left, up, down]
        filtered_l = [
            point
            for point in l
            if point[0] >= 0
            and point[0] < self.numrows
            and point[1] >= 0
            and point[1] < self.numcols
        ]
        not_visited = [x for x in filtered_l if not x in self.visited]
        for node in not_visited:
            if self.height_diff(node, self.current) <= 1:
                self.to_consider[node] = min(self.to_consider.get(node, math.inf), self.distances[self.current[0]][self.current[1]]+1)




    def run(self):
        while True:
            # find adjacent nodes and add to to_consider
            self.adjacent()

            closest = math.inf 
            which_node = None
            
            if not self.to_consider:
                raise ValueError("no other nodes to visit")
            # find node to visit next
            for node in self.to_consider:
                if self.to_consider[node] <= closest:
                    closest = self.to_consider[node]
                    which_node = node

            if which_node == self.end:
                print('reached the end node')
                break

            print(f"visiting this node: {which_node}")
            self.visited.add(which_node)
            self.distances[which_node[0]][which_node[1]] = closest
            del self.to_consider[which_node]
            self.current = which_node


        # end node is in the to_consider with the cost to get there
        print(f"the cost to get to the end node is {self.to_consider[self.end]}")









    def pretty_print(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.board)
        print(f"start is {self.start}. end is {self.end}")
        pp.pprint(self.distances)
        print(f"currently at {self.current}")
        print(f"adjacent are {self.adjacent()}")
        print(f"you are at elevation {self.elevation()}")
        pp.pprint(self.elevations)






def run_part_1(sample_or_real):
    pp = pprint.PrettyPrinter(indent=4)
    file = os.path.join("input_files", filemap[sample_or_real])
    with open(file, "r") as f:
        data = f.read()
    rows = data.split("\n")
    board = Board(rows)
    board.pretty_print()
    board.run()


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
