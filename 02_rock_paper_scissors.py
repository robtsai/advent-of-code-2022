# part 1


play = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}

our_play = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}


win_lose_draw = {
    "AX": "draw",
    "AY": "win",
    "AZ": "lose",
    "BX": "lose",
    "BY": "draw",
    "BZ": "win",
    "CX": "win",
    "CY": "lose",
    "CZ": "draw"
}

game_points = {
    "win": 6,
    "lose": 0,
    "draw": 3
}

shape_points = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

# part 2

what_we_need_to_do = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}


# what_we_throw to win_lose_draw
what_we_throw = {
    "Rock": ("Paper", "Scissors", "Rock"),
    "Paper": ("Scissors", "Rock", "Paper"),
    "Scissors": ("Rock", "Paper", "Scissors")
}

# index positions
win_lose_draw_index = {
    "win": 0,
    "lose": 1,
    "draw": 2
}


def score_round2(hand_list):
    they_threw = play[hand_list[0]]
    we_need_to = what_we_need_to_do[hand_list[1]]
    print(f"they threw: {they_threw}")
    print(f"we need to: {we_need_to}")
    our_choices = what_we_throw[they_threw]
    print(f"our choices to win, lose draw are: {our_choices}")
    we_choose = our_choices[win_lose_draw_index[we_need_to]]
    print(f"we choose: {we_choose}")
    game_score = game_points[we_need_to]
    print(f"we scored for the game: {game_score}") 
    shape_score = shape_points[we_choose]
    print(f"shape score is: {shape_score}")
    print(f"\n"*2)
    return game_score + shape_score



# part 1

def score_round(hand_list):
    hand = ''.join(hand_list)
    if not hand in win_lose_draw:
        raise ValueError("invalid hand")

    opp, us = hand_list
    opp_shape = play[opp]
    our_shape = our_play[us]
    print(f"opp played {opp}, {opp_shape}")
    print(f"we played {us}, {our_shape}")
    res = win_lose_draw[hand]
    game_score = game_points[res]
    shape_score = shape_points[our_shape]
    print(f"result was {res}")
    print(f"game score was: {game_score}")
    print(f"shape score was: {shape_score}")
    total_score = game_score + shape_score
    print(total_score)
    print(f"\n"*2)
    return total_score




def run_part_1():
    running_total = 0
    with open("input_files/problem02.txt", "r") as f:
        for line in f:
            hand_list = line.replace("\n", "").split(" ")
            running_total += score_round(hand_list)
    print(f"the answer to part 1 is {running_total}")


def run_part_2():
    running_total = 0
    with open("input_files/problem02.txt", "r") as f:
        for line in f:
            hand_list = line.replace("\n", "").split(" ")
            running_total += score_round2(hand_list)
    print(f"the answer to part 2 is {running_total}")


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