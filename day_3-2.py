import re

answer = 0
iterations = 0


def adjacent_next_line(match_1, match_2):
    # Determines if match on first line overlaps with match on second line
    adjacent = False
    # Indeces of the start and end of each match
    start_1 = match_1.start()
    end_1 = match_1.end() - 1
    start_2 = match_2.start()
    end_2 = match_2.end() - 1

    if (start_1 - 1 <= start_2 and start_2 <= end_1 + 1) or (
        start_1 - 1 <= end_2 and end_2 <= end_1 + 1
    ):
        adjacent = True

    return adjacent


with open("day_3_input.txt") as file:
    first_line = file.readline()
    second_line = file.readline()
    pattern = r"\d{1,3}|\*"

    # Scan first_line for all part numbers and gears
    matches = re.finditer(pattern, first_line)
    line_matches = list(matches)
    # Scan second_line
    matches = re.finditer(pattern, second_line)
    second_line_matches = list(matches)

    for line in file:
        # Scan third_line
        matches = re.finditer(pattern, line)
        third_line_matches = list(matches)

        for i, match in enumerate(line_matches):
            start = match.start()
            end = match.end()

            # Check if match is a gear or part_nbr
            if match[0] == "*":
                # Check for part_nbr immediately to right
                if i + 1 < len(line_matches):
                    next_match = line_matches[i + 1]
                    if next_match.start() == end and next_match[0] != "*":
                        # Check for adjacent part_nbr on the next line
                        for second_line_match in second_line_matches:
                            if second_line_match[0] != "*" and adjacent_next_line(
                                match, second_line_match
                            ):
                                answer += int(next_match[0]) * int(second_line_match[0])
                # Check for case where two numbers are on left and right on next line
                # Check for left part_nbr
                for j, second_line_match in enumerate(second_line_matches):
                    if start == second_line_match.end() and second_line_match[0] != "*":
                        # Check for right part_nbr
                        if j + 1 < len(second_line_matches):
                            if (
                                end == second_line_matches[j + 1].start()
                                and second_line_matches[j + 1][0] != "*"
                            ):
                                answer += int(second_line_match[0]) * int(
                                    second_line_matches[j + 1][0]
                                )

            else:  # It's a part_nbr
                part_nbr = int(match[0])
                # Check for gear immediately to right
                if i + 1 < len(line_matches):
                    next_match = line_matches[i + 1]
                    if next_match.start() == end and next_match[0] == "*":
                        # Check for part_nbr immediately to right
                        if i + 2 < len(line_matches):
                            match_2 = line_matches[i + 2]
                            if (
                                match_2.start() == next_match.end()
                                and match_2[0] != "*"
                            ):
                                answer += part_nbr * int(match_2[0])
                        # Check if adjacent to part_nbr on the next line
                        for second_line_match in second_line_matches:
                            if second_line_match[0] != "*" and adjacent_next_line(
                                next_match, second_line_match
                            ):
                                answer += part_nbr * int(second_line_match[0])
                # Check for adjacent gear on next line
                for j, second_line_match in enumerate(second_line_matches):
                    if second_line_match[0] == "*" and adjacent_next_line(
                        match, second_line_match
                    ):
                        # Check for part_nbr to right on previous line
                        if i + 1 < len(line_matches):
                            match_2 = line_matches[i + 1]
                            if (
                                match_2.start() == second_line_match.end()
                                and match_2[0] != "*"
                            ):
                                answer += part_nbr * int(match_2[0])
                        # Check for part_nbr immediately to left
                        if j > 0:
                            match_2 = second_line_matches[j - 1]
                            if (
                                match_2.end() == second_line_match.start()
                                and match_2[0] != "*"
                            ):
                                answer += part_nbr * int(match_2[0])
                        # Check for part_nbr immediately to right
                        if j + 1 < len(second_line_matches):
                            match_2 = second_line_matches[j + 1]
                            if (
                                match_2.start() == second_line_match.end()
                                and match_2[0] != "*"
                            ):
                                answer += part_nbr * int(match_2[0])
                        # Check for adjacent part_nbr on second line
                        for third_line_match in third_line_matches:
                            if third_line_match[0] != "*" and adjacent_next_line(
                                second_line_match, third_line_match
                            ):
                                answer += part_nbr * int(third_line_match[0])

        # Shift line matches for next pass
        line_matches = second_line_matches
        second_line_matches = third_line_matches

    # 2nd to last line
    for i, match in enumerate(line_matches):
        start = match.start()
        end = match.end()

        # Gonna have to add a bunch of try-except-finally statements or conditionals to avoid out-of-bounds index errors
        # Check if match is a gear or part_nbr
        if match[0] == "*":
            # Check for part_nbr immediately to right
            if i + 1 < len(line_matches):
                next_match = line_matches[i + 1]
                if next_match.start() == end and next_match[0] != "*":
                    # Check for adjacent part_nbr on the next line
                    for second_line_match in second_line_matches:
                        if second_line_match[0] != "*" and adjacent_next_line(
                            match, second_line_match
                        ):
                            answer += part_nbr * int(second_line_match[0])
            # Check for case where two numbers are on left and right on next line
            # Check for left part_nbr
            for j, second_line_match in enumerate(second_line_matches):
                if start == second_line_match.end() and second_line_match[0] != "*":
                    # Check for right part_nbr
                    if j + 1 < len(second_line_matches):
                        if (
                            end == second_line_matches[j + 1].start()
                            and second_line_matches[j + 1][0] != "*"
                        ):
                            answer += int(second_line_match[0]) * int(
                                second_line_matches[j + 1][0]
                            )
        else:  # It's a part_nbr
            part_nbr = int(match[0])
            # Check for gear immediately to right
            if i + 1 < len(line_matches):
                next_match = line_matches[i + 1]
                if (
                    i + 2 < len(line_matches)
                    and next_match.start() == end
                    and next_match[0] == "*"
                ):
                    # Check for part_nbr immediately to right
                    match_2 = line_matches[i + 2]
                    if match_2.start() == next_match.end() and match_2[0] != "*":
                        answer += part_nbr * int(match_2[0])
                # Check if adjacent to part_nbr on the next line
                for second_line_match in second_line_matches:
                    if second_line_match[0] != "*" and adjacent_next_line(
                        match, second_line_match
                    ):  # part_nbr overlaps the gear
                        answer += part_nbr * int(second_line_match[0])
            # Check for adjacent gear on next line
            for j, second_line_match in enumerate(second_line_matches):
                if second_line_match[0] == "*" and adjacent_next_line(
                    match, second_line_match
                ):
                    # Check for part_nbr to right on previous line
                    if i + 1 < len(line_matches):
                        match_2 = line_matches[i + 1]
                        if (
                            match_2.start() == second_line_match.end()
                            and match_2[0] != "*"
                        ):
                            answer += part_nbr * int(match_2[0])
                    # Check for part_nbr immediately to left
                    if j > 0:
                        match_2 = second_line_matches[j - 1]
                        if (
                            match_2.end() == second_line_match.start()
                            and match_2[0] != "*"
                        ):
                            answer += part_nbr * int(match_2[0])
                        # Check for part_nbr immediately to right
                        match_2 = second_line_matches[j + 1]
                        if (
                            match_2.start() == second_line_match.end()
                            and match_2[0] != "*"
                        ):
                            answer += part_nbr * int(match_2[0])

    # Shift line matches for final pass
    line_matches = second_line_matches

    # Last line
    for i, match in enumerate(line_matches):
        start = match.start()
        end = match.end()

        # Gonna have to add a bunch of try-except-finally statements or conditionals to avoid out-of-bounds index errors
        # Check if match is a part_nbr
        if len(line_matches) > 2:
            if match[0] != "*":
                part_nbr = int(match[0])
                # Check for gear immediately to right
                if i + 2 < len(line_matches):
                    next_match = line_matches[i + 1]
                    if next_match.start() == end and next_match[0] == "*":
                        # Check for part_nbr immediately to right
                        match_2 = line_matches[i + 2]
                        if match_2.start() == next_match.end() and match_2[0] != "*":
                            answer += part_nbr * int(match_2[0])

print(answer)
# 1st attempt: 78102807 too low
# 2nd attampt: 81789587 still too low
# Learned that gears touch exactly 2 numbers, so any gears touching 3+ nbrs should be thrown out.
# However, I don't see any cases with 3+ in my input. Besides, my answer is too low anyway.
# I don't see any edge cases I'm missing, so I figured it must be the final lines that are messing up, but I don't see any issues there either.
# Had a + sign rather than a * in one of my gear ratios. That took forever to find and debug.
# 3rd attempt: 84399773
