import re
def main():
    result = 0
    result_2 = 0

    with open("data/2") as f:
        lines = f.readlines()
    for game_number, line in enumerate(lines):
        turns_in_line = get_list_from_parser(line.rstrip('\n'))
        list_of_maps = get_color_map(turns_in_line)
        result += check_validity(list_of_maps, game_number+1)

        result_2 += check_least_cubes(list_of_maps)

    print(f'Result 1 is: {result}')
    print(f'Result 2 is: {result_2}')


def get_list_from_parser(line):
    line_split = re.split(":|;", line)
    return [re.split(', ', split) for split in line_split[1:]]


def get_color_map(turn):
    list_of_color_dicts = []
    for sublist in turn:
        color_dict = {}
        for item in sublist:
            number, color = re.findall(r'\d+|\w+', item)
            color_dict[color] = int(number)
        list_of_color_dicts.append(color_dict)

    return list_of_color_dicts


def check_validity(map, game_number):
    for line in map:
        for color, number in line.items():
            if color == "red" and number > 12:
                return 0
            if color == "green" and number > 13:
                return 0
            if color == "blue" and number > 14:
                return 0

    return game_number


def check_least_cubes(map):
    red_c = 0
    green_c = 0
    blue_c = 0
    for line in map:
        for color, number in line.items():
            if color == "red" and number > red_c:
                red_c = number
            if color == "green" and number > green_c:
                green_c = number
            if color == "blue" and number > blue_c:
                blue_c = number
    return red_c*blue_c*green_c


if __name__ == "__main__":
    main()