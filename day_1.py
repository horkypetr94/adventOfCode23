import re

data = []
total_count = 0

with open("data/1") as f:
    lines = f.readlines()

for i,line in enumerate(lines):
    number_str = ""
    for char in line:
        if char.isdigit():
            number_str = number_str + char
    number_str = number_str[0] + number_str[-1]
    total_count = total_count + int(number_str)

print(f'result1: {total_count}')

total_count = 0
pattern = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)')
reverse_pattern = re.compile(r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|1|2|3|4|5|6|7|8|9)')

for i, line in enumerate(lines):
    reversed_line = line[::-1]
    reversed_match = reverse_pattern.findall(reversed_line)[0]
    last = reversed_match[::-1]

    first = pattern.findall(line)[0]

    number = first+last
    number = number.replace("one", "1")
    number = number.replace("two", "2")
    number = number.replace("three", "3")
    number = number.replace("four", "4")
    number = number.replace("five", "5")
    number = number.replace("six", "6")
    number = number.replace("seven", "7")
    number = number.replace("eight", "8")
    number = number.replace("nine", "9")

    print(i+1, "  ", number)
    total_count = total_count + int(number)

print(f'result2: {total_count}')
