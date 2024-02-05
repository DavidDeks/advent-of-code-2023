import re

answer = 0

with open("day_2_input.txt") as file:
    for line in file:
        game = re.search("Game (\d+):", line).group(1)
        red = re.findall("(\d+) red", line)
        green = re.findall("(\d+) green", line)
        blue = re.findall("(\d+) blue", line)

        red_max, green_max, blue_max = 0, 0, 0

        # find max of each color to get the minimum needed of each
        for cube in red:
            if int(cube) > red_max:
                red_max = int(cube)
        for cube in green:
            if int(cube) > green_max:
                green_max = int(cube)
        for cube in blue:
            if int(cube) > blue_max:
                blue_max = int(cube)

        power = red_max * green_max * blue_max

        answer += power

print(answer)
