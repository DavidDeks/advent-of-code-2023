import re

i = 0
length = 3
line = "467..114.."
next_line = "...*......"

match = re.search(r"[^(\d\.\s)]", "...*......")
print(f"match: {match}")
spec_char = False
# spec_char = re.search("[^\d\.\s]", next_line)  # next_line[i : i + length + 1],

# bool(re.match("[^\d\.\s]", line[i + length + 1]))
# or

if re.search("[^\d\.\s]", next_line):
    spec_char = True

print(f"spec_char: {spec_char}")
