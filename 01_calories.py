# part 1


def run_part_1():
    current_sum = 0
    max_sum = 0

    with open("input_files/problem01.txt", "r") as f:
        for line in f:

            if line == "\n":
                max_sum = max(current_sum, max_sum)
                current_sum = 0
            else:
                print(line)
                current_sum += int(line.replace("\n", ""))
                print(current_sum)

    print(f"answer to part 1 is {max_sum}")


def run_part_2():
    all_sums = []
    current_sum = 0
    with open("input_files/problem01.txt", "r") as f:
        for line in f:

            if line == "\n":
                all_sums.append(current_sum)
                current_sum = 0
            else:
                current_sum += int(line.replace("\n", ""))
    sorted_sums = sorted(all_sums, reverse=True)
    top_3 = sum(sorted_sums[:3])
    print(f"the answer to part 2 is {top_3}")


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