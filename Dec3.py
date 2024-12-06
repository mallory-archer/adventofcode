import re
import math

# examples
# string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"    # example string
# string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("./dec3data.txt", "r") as f:
    string = f.read()
# print("String is %s" % string)

# ---- part 1
pattern = r"mul[\(]\d+,\d+[\)]"
# matches = re.findall(pattern, string)
# print(matches)

# ----- part 2
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

# initialize
matches = list()
substring_start = 0
substring_end = 0

while len(string) > 0:
    substring_end = re.search(dont_pattern, string).start() if re.search(dont_pattern, string) is not None else len(string)
    substring = string[:substring_end]        
    matches = matches + re.findall(pattern, substring)
    string = string[substring_end:]
    if  re.search(do_pattern, string) is None:
        break
    substring_start = re.search(do_pattern, string).end()
    string = string[substring_start:]


print("The sum of all the products is %f" %  
      sum([math.prod([float(x) for x in match[re.search(r"mul[\(]", match).end(): re.search(r"[\)]", match).start()].split(',')]) for match in matches])
)



