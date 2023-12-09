import re
import itertools
import numpy as np
delimiters = [":", "|"]
win_arr = []
guess_arr = []


def main():
    with open("data/5") as f:
        lines = [line.rstrip('\n') for line in f]
    dict_map = parse_input(lines)
    seed_vals = dict_map['seeds:'][0]
    locations = []
    del dict_map['seeds:']
    for seed in seed_vals:
        for key, val in dict_map.items():
            seed = create_ranges(int(seed), val)
        locations.append(seed)
    print(f"Result is {min(locations)}")


def create_ranges(seed, val):
    for v in val:
        min_v = int(v[1])
        max_v = int(v[1])+int(v[2])
        if min_v <= seed <= max_v:
           return seed - int(v[1]) + int(v[0])
    return int(seed)


def parse_input(lines):
    dict_map = {}
    split_data = [list(group) for key, group in itertools.groupby(lines, key=lambda x: x == '') if not key]
    for line in split_data:
        item_list = []
        for item in line[1:]:
            item_list.append(re.findall(r'\d+', item))
        dict_map[line[0]] = item_list

    return dict_map


if __name__ == "__main__":
    main()