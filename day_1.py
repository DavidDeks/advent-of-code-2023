import re

answer = 0

with open("day_1_input.txt") as file:
    for line in file:
        start = re.search("\d", line).group()
        end = re.findall("\d", line)[-1]
        start_end = start + end
        answer += int(start_end)

print(answer)
