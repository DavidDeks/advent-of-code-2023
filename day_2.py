import re

answer = 0

with open("day_2_input.txt") as file:
    red_max, green_max, blue_max = 12, 13, 14

    for line in file:
        game = re.search("Game (\d+):", line).group(1)
        red = re.findall("(\d+) red", line)
        green = re.findall("(\d+) green", line)
        blue = re.findall("(\d+) blue", line)

        possible = True
        while possible:
            for cube in red:
                if int(cube) > red_max:
                    possible = False
            for cube in green:
                if int(cube) > green_max:
                    possible = False
            for cube in blue:
                if int(cube) > blue_max:
                    possible = False
            break

        if possible:
            answer += int(game)

print(answer)
