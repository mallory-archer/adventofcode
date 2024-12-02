# data = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9]
# ]

with open("./dec2data.txt", "r") as f:
    data = f.read()
data = [[int(x) for x in r.split(sep=' ')] for r in data.splitlines()]

def increasing_diff(x):
    return x > 0

def decreasing_diff(x):
    return x < 0

def diff_window(x):
    return (abs(x) >= 1) and (abs(x) <= 3)

def diff_list(x:list):
    return [l1 - l0 for l0, l1 in zip(x[:-1], x[1:])]

def check_report(report:list):
    return (all([increasing_diff(diff) for diff in diff_list(report)]) or all([decreasing_diff(diff) for diff in diff_list(report)])) and all([diff_window(diff) for diff in diff_list(report)])

print("The total number of safe reports is %d" % sum([check_report(r) for r in data]))

print("The total number of safe reports with the problem dampener is %d" % sum([any([check_report(r[:l] + r[l+1:]) for l in range(len(r))]) for r in data]))