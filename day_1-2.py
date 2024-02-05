import re

answer = 0
digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("day_1_input.txt") as file:
    for line in file:
        start = re.search(
            "\d|one|two|three|four|five|six|seven|eight|nine", line
        ).group()

        # Working except for this line. Findall() doesn't work because it doesn't account for overlapping patterns
        # E.g. captures last digit of "two" from "twone" rather than "one"
        # using ()$ fails because it doesn't account for when the match has other characters after it.
        # e.g. oneasdf would throw an error
        # Have to add .* to capture those extra characters, but make it a non-capturing group
        # .* doesn't work because that will capture anything after the match, including more digits
        # e.g.
        # end = re.search(
        #     "(?:\d|one|two|three|four|five|six|seven|eight|nine)+.*(\d|one|two|three|four|five|six|seven|eight|nine).*$",
        #     line,
        # ).group()

        # The below works by using positive lookahead ?=
        # Any valid regular expression can be used inside the lookahead.
        # If it contains capturing groups then those groups will capture as normal and backreferences to them will work normally,
        # even outside the lookahead.
        # The lookahead itself is not a capturing group. It is not included in the count towards numbering the backreferences.
        # If you want to store the match of the regex inside a lookahead, you have to put capturing parentheses around the regex
        # inside the lookahead,
        # like this: (?=(regex)). The other way around will not work, because the lookahead will
        # already have discarded the regex match by the time the capturing group is to store its match.

        # Another option is to use the 3rd party "regex" module which supports overlapping matches.
        # pip install regex
        # e.g.
        # import regex as re
        # end = re.findall(
        #     r"\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True
        # )[-1]

        end = re.findall(
            r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
        )[-1]
        try:
            int(start)
        except:
            start = str(digits[start])
        try:
            int(end)
        except:
            end = str(digits[end])
        start_end = start + end
        answer += int(start_end)

print(answer)
