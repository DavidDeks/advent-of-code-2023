import re

answer = 0

filename = "day_4_input.txt"
file_length = 0

# Get nbr of lines in file
with open(filename) as file:
    file_length = len(file.readlines())

with open(filename) as file:
    # Create list with 1 initial copy count for each card
    copy_count = []
    for x in range(file_length):
        copy_count.append(1)
    # Get winning and my numbers lists
    for i, line in enumerate(file):
        winners_str = line[line.index(":") : line.index("|")]
        mine_str = line[line.index("|") :]

        winners = re.findall("\d+", winners_str)
        mine = re.findall("\d+", mine_str)

        # Calculate wins
        win_cnt = 0
        for x in winners:
            if x in mine:
                win_cnt += 1

        # Add to the win_cnt following rows the amount of copies of current card
        for j in range(win_cnt):
            copy_count[i + 1 + j] += copy_count[i]

    # Sum total cards
    for x in copy_count:
        answer += x

print(answer)
