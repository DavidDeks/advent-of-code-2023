import re

answer = 0

with open("day_4_input.txt") as file:
    for line in file:
        win_cnt = 0

        winners_str = line[line.index(":") : line.index("|")]
        mine_str = line[line.index("|") :]

        winners = re.findall("\d+", winners_str)
        mine = re.findall("\d+", mine_str)

        for x in winners:
            if x in mine:
                win_cnt += 1

        if win_cnt:
            answer += 2 ** (win_cnt - 1)

print(answer)
