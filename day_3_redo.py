import re

answer = 0

# I was trying to read the file into memory one line at a time
# and only keep the 3 lines (previous, current, and next) in memory at a time.
# The much easier way to iterate over these in Python is to use readlines()
# and just read the entire file into a list. This only works if the file is small,
# which it is in this case, but I wanted to try best practices for larger files.

with open("day_3_input.txt") as file:
    symbol_pattern = r"[^\d\.\s]"
    nbr_pattern = r"\d{1,3}"
    previous_line = ""
    line = file.readline()

    for next_line in file:
        part_nbr_matches = re.finditer(nbr_pattern, line)

        # search for surrounding special characters
        for match in part_nbr_matches:
            part_nbr = match[0]
            spec_char = False
            start = match.start()
            end = match.end()
            left = start - 1
            right = end
            right_splice = end + 1
            left_edge = start
            right_edge_splice = end  # Did not realize the end index returned from match object is already +1 from 0-based index

            if previous_line == "":  # first line
                if left_edge == 0:  # first character
                    chars = line[right] + next_line[left_edge:right_splice]
                    spec_char = bool(re.search(symbol_pattern, chars))
                elif end == len(line):  # last character
                    chars = line[left] + next_line[left:right_edge_splice]
                    spec_char = bool(re.search(symbol_pattern, chars))
                else:
                    chars = line[left:right_splice] + next_line[left:right_splice]
                    spec_char = bool(re.search(symbol_pattern, chars))
            else:
                if left_edge == 0:  # first character
                    chars = (
                        previous_line[left_edge:right_splice]
                        + line[right]
                        + next_line[left_edge:right_splice]
                    )
                    spec_char = bool(re.search(symbol_pattern, chars))
                elif end == len(line):  # last character
                    chars = (
                        previous_line[left:right_edge_splice]
                        + line[left]
                        + next_line[left:right_edge_splice]
                    )
                    spec_char = bool(re.search(symbol_pattern, chars))
                else:
                    chars = (
                        previous_line[left:right_splice]
                        + line[left:right_splice]
                        + next_line[left:right_splice]
                    )
                    spec_char = bool(re.search(symbol_pattern, chars))

            if spec_char:
                answer += int(part_nbr)

        previous_line = line
        line = next_line

    # last line
    part_nbr_matches = re.finditer(nbr_pattern, line)
    # search for surrounding special characters
    for match in part_nbr_matches:
        part_nbr = match[0]
        spec_char = False
        start = match.start()
        end = match.end()
        part_nbr = match[0]
        left = start - 1
        right = end
        right_splice = end + 1
        left_edge = start
        right_edge_splice = end

        if left_edge == 0:  # first character
            chars = previous_line[left_edge:right_splice] + line[right]
            spec_char = bool(re.search(symbol_pattern, chars))
        elif end == len(line):  # last character
            chars = previous_line[left:right_edge_splice] + line[left]
            spec_char = bool(re.search(symbol_pattern, chars))
        else:
            chars = previous_line[left:right_splice] + line[left:right_splice]
            spec_char = bool(re.search(symbol_pattern, chars))

        if spec_char:
            answer += int(part_nbr)

print(answer)
