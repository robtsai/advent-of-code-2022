import re
import dis
import operator
import sys
import functools

# looks like lcm is a function in 3.9 and higher

class Monkey:
    def __init__(self, number, items, opers, test, if_true, if_false):
        self.number = number
        self.items = items
        self.opers = opers
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    def __repr__(self):
        return f"""
            monkey number: {self.number}
            monkey with items {self.items}
            opers {self.opers}
            test {self.test}
            if_true {self.if_true}
            if_false {self.if_false}
            inspections {self.inspections}
        """


class Game:
    def __init__(self, monkeys, boredom_factor=3):
        self.round = 1
        self.monkeys = monkeys
        self.boredom_factor = boredom_factor

    def play_round(self):
        print(f"playing round: {self.round}")
        total_monkeys = len(self.monkeys)
        print(f" there are {total_monkeys} total monkeys")

        monkey_index = 0

        while monkey_index < total_monkeys:
            print(f"monkey index: {monkey_index}")
            cur_monkey = self.monkeys[monkey_index]
            print(f"current monkey: {cur_monkey}")
            for item in cur_monkey.items:
                cur_monkey.inspections += 1
                worry = cur_monkey.opers(item)
                bored = worry // self.boredom_factor
                the_test = cur_monkey.test(bored)
                if the_test:
                    target = cur_monkey.if_true
                else:
                    target = cur_monkey.if_false 

                self.monkeys[target].items.append(bored)

            cur_monkey.items = []    
            monkey_index += 1
        print(f"finished playing round {self.round}")
        self.round += 1

    def show_inspections(self):
        inspections = {}
        for k, monkey in self.monkeys.items():
            inspections[k] = monkey.inspections 

        print(inspections)
        sorted_inspections = sorted([v for v in inspections.values()], reverse=True)
        print(sorted_inspections)
        return sorted_inspections[0] * sorted_inspections[1]


def get_monkeys():
    monkey_start = re.compile("Monkey (\d+):")
    starting_items = re.compile("  Starting items: (.+)")
    operation = re.compile("  Operation: new = (old.+)")
    test_re = re.compile("  Test: divisible by (\d+)")
    if_true_re = re.compile("  If true: throw to monkey (\d+)")
    if_false_re = re.compile("  If false: throw to monkey (\d+)")


    monkeys = {}

    with open("input_files/problem11.txt", "r") as f:
        totalinput = f.read()
        ops = totalinput.split("\n")
        print(ops)


        current_monkey = None
        current_items = None
        current_op = None
        current_test = None
        target_true = None
        target_false = None

        for op in ops:
            
            if monkey_start.match(op):
                current_monkey = int(monkey_start.match(op).group(1))
            elif starting_items.match(op):
                line_items = starting_items.match(op).group(1).split(",")
                current_items = [int(x) for x in line_items]
            elif operation.match(op):
                rule = operation.match(op).group(1)
                lambda_rule = f"lambda old: {rule}"
                current_op = eval(lambda_rule)
            elif test_re.search(op):
                div_rule = int(test_re.search(op).group(1))
                div_lambda_rule = f"lambda x: x % {div_rule} == 0"
                current_test = eval(div_lambda_rule)
            elif if_true_re.search(op):
                target_true = int(if_true_re.search(op).group(1))
            elif if_false_re.search(op):
                target_false = int(if_false_re.search(op).group(1))

                # create a new monkey
                new_monkey = Monkey(
                    current_monkey,
                    current_items,
                    current_op,
                    current_test,
                    target_true,
                    target_false
                )
                monkeys[new_monkey.number] = new_monkey

                current_monkey = current_items = current_op = current_test = target_true = target_false = None

    return monkeys



def get_argval_from_lambda(lambdafunc):
    # i is a generator object of disassembly of bytecode
    # the argval is the second item in the generator
    i = dis.get_instructions(lambdafunc)
    next(i)
    argval = next(i).argval 
    return argval




def run_part_1():

    monkeys = get_monkeys()

    game = Game(monkeys)
    for r in range(20):
        game.play_round()
    
    result = game.show_inspections()
    print(f"the answer to part 1 is {result}")


def run_part_2():
    monkeys = get_monkeys()

    allargs = []

    for _, monkey in monkeys.items():
        argval = get_argval_from_lambda(monkey.test)
        allargs.append(argval)
    print(allargs)

    product = functools.reduce(operator.mul, allargs)
    print(product)

    game = Game(monkeys, product)
    for r in range(10000):
        game.play_round()

    result = game.show_inspections()
    print("part 2 not working yet")
    print(f"the answer to part 2 is {result}")

        




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
