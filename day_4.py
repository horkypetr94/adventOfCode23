import re
import numpy as np
delimiters = [":", "|"]
win_arr = []
guess_arr = []

def main():
    with open("data/4") as f:
        lines = f.readlines()

    win_array, gues_array = parse_input(lines)
    counter = find_winning_numbers(win_arr,guess_arr)
    print(counter)


def parse_input(lines):
    for i,line in enumerate(lines):
        line = re.split(r'[:|\n]', line)
        win_line = line[1][1:-1].split(" ")
        guess_line = line[2][1:].split(" ")
        win_arr.append(make_ints(win_line))
        guess_arr.append(make_ints(guess_line))

    return win_arr, guess_arr

def make_ints(line):
    int_arr = []
    for item in line:
        try:
            item = int(item)
            int_arr.append(item)
        except:
            pass

    return int_arr

def find_winning_numbers(win_arr, guess_arr):
    counter = 0
    round_hits = 0
    for i, line in enumerate(win_arr):
        for item in line:
            if item in guess_arr[i]:
               round_hits +=1
        if round_hits >= 1:
            counter += np.power(2, round_hits-1)
            round_hits = 0
    return counter

if __name__ == "__main__":
    main()