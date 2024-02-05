import re

answer = 0

# I was trying to read the file into memory one line at a time
# and only keep the 3 lines (previous, current, and next) in memory at a time.
# The much easier way to iterate over these in Python is to use readlines()
# and just read the entire file into a list. This only works if the file is small,
# which it is in this case, but I wanted to try best practices for larger files.

with open("day_3_input.txt") as file:
    previous_line = ""
    line = file.readline()

    for next_line in file:
        enum_line = enumerate(line)
        ##########################################################################################################
        # This section could definitely be optimized to use the regex
        # to just initially grab all the numbers with their indeces
        # Then you could use the index of the match to determine the surrounding chars
        for i, char in enum_line:
            if re.match("\d", char):
                part_nbr = char
                length = 1
                # check for 2-3 digit numbers
                second_element = next(enum_line)
                if re.match("\d", second_element[1]):
                    part_nbr = part_nbr + second_element[1]
                    length += 1
                    third_element = next(enum_line)
                    if re.match("\d", third_element[1]):
                        part_nbr = part_nbr + third_element[1]
                        length += 1
                ############################################################################################################
                # search for surrounding special characters
                spec_char = False

                if previous_line == "":  # first line
                    if i == 0:  # first character
                        chars = line[i + length] + next_line[i : i + length + 1]
                        spec_char = bool(re.search("[^\d\.\s]", chars))
                    elif i + length == len(line):  # last character
                        chars = line[i - 1] + next_line[i - 1 : i + length]
                        spec_char = bool(re.search("[^\d\.\s]", chars))
                    else:
                        chars = (
                            line[i - 1 : i + length + 1]
                            + next_line[i - 1 : i + length + 1]
                        )
                        spec_char = bool(re.search("[^\d\.\s]", chars))
                else:
                    if i == 0:  # first character
                        chars = (
                            previous_line[i : i + length + 1]
                            + line[i + length]
                            + next_line[i : i + length + 1]
                        )
                        spec_char = bool(re.search("[^\d\.\s]", chars))
                    elif i + length == len(line):  # last character
                        chars = (
                            previous_line[i - 1 : i + length]
                            + line[i - 1]
                            + next_line[i - 1 : i + length]
                        )
                        spec_char = bool(re.search("[^\d\.\s]", chars))
                    else:
                        chars = (
                            previous_line[i - 1 : i + length + 1]
                            + line[i - 1 : i + length + 1]
                            + next_line[i - 1 : i + length + 1]
                        )
                        spec_char = bool(re.search("[^\d\.\s]", chars))

                if spec_char:
                    answer += int(part_nbr)

        previous_line = line
        line = next_line

    # last line
    enum_line = enumerate(line)
    ##########################################################################################################
    # This section could definitely be optimized to use the regex
    # to just initially grab all the numbers with their indeces
    # Then you could use the index of the match to determine the surrounding chars
    for i, char in enum_line:
        if re.search("\d", char):
            part_nbr = char
            length = 1
            # check for 2-3 digit numbers
            second_element = next(enum_line)
            if re.search("\d", second_element[1]):
                part_nbr = part_nbr + second_element[1]
                length += 1
                try:
                    third_element = next(enum_line)
                except:
                    third_element = ["", ""]
                if re.search("\d", third_element[1]):
                    part_nbr = part_nbr + third_element[1]
                    length += 1

            spec_char = False

            if i == 0:  # first character
                chars = previous_line[i : i + length + 1] + line[i : i + length + 1]
                spec_char = bool(re.search("[^\d\.\s]", chars))
            elif i + length == len(line):  # last character
                chars = previous_line[i - 1 : i + length] + line[i - 1 : i + length]
                spec_char = bool(re.search("[^\d\.\s]", chars))
            else:
                chars = (
                    previous_line[i - 1 : i + length + 1] + line[i - 1 : i + length + 1]
                )
                spec_char = bool(re.search("[^\d\.\s]", chars))

            if spec_char:
                answer += int(part_nbr)

print(answer)
