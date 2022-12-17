import os


def run_part_1():
    file = os.path.join("input_files", "problem06.txt")
    with open(file, "r") as f:
        data = f.read()
    length = len(data)
    end_index = 3
    print(data)

    while end_index < length:
        the_slice = data[end_index-3: end_index+1]
        print(the_slice)
        if len(set(the_slice)) == 4:
            print("we have 4 distinct chars in the slice")
            print(the_slice)
            print(end_index)
            print(f"the answer to part 1 is {end_index+1}")
            break
        end_index += 1


def run_part_2():
    file = os.path.join("input_files", "problem06.txt")
    with open(file, "r") as f:
        data = f.read()
    length = len(data)
    end_index = 13
    print(data)

    while end_index < length:
        the_slice = data[end_index-13: end_index+1]
        print(the_slice)
        if len(set(the_slice)) == 14:
            print("we have 14 distinct chars in the slice")
            print(the_slice)
            print(end_index)
            print(f"the answer to part 1 is {end_index+1}")
            break
        end_index += 1



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