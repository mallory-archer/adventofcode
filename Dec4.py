with open('./dec4data.txt', "r") as f:
    data = f.readlines()
data = [x.strip("\n") for x in data]
ncol = len(data)
nrow = len(data[0])

for x in data:
    print(x)

def horizontal_search(nrow, ncol, data):
    print('Horizonal')
    horizontal_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    count = 0
    for i in range(nrow):
        for j in range(ncol - (len("XMAS")-1)):
            if data[i][j] == "X":
                if data[i][j+1] == "M":
                    if data[i][j+2] == "A":
                        if data[i][j+3] == "S":
                            count += 1
                            for k in range(j, j+4):
                                # horizontal_search[i][j:j+4] = True
                                horizontal_search[i][k] = True
                                print(i, k)
                                print(data[i][k])
                            print("\n")
    print('Horizontal count = %d' % (count))
    return horizontal_search, count

def vertical_search(nrow, ncol, data):
    print('vertical')
    count = 0
    vertical_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for j in range(ncol):
        for i in range(nrow - (len("XMAS")-1)):
            if data[i][j] == "X":
                if data[i+1][j] == "M":
                    if data[i+2][j] == "A":
                        if data[i+3][j] == "S":
                            count += 1
                            for k in range(i, i+4):
                                # horizontal_search[i][j:j+4] = True
                                vertical_search[k][j] = True
                                print(data[k][j])
                            print("\n")
    print('Vertical count = %d' % (count))
    return vertical_search, count

def diag_right_search(nrow, ncol, data):
    print("diag down and to the right")
    count = 0
    diag_right_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow - (len("XMAS")-1)):
        for j in range(ncol - (len("XMAS")-1)):
            if data[i][j] == "X":
                if data[i+1][j+1] == "M":
                    if data[i+2][j+2] == "A":
                        if data[i+3][j+3] == "S":
                            count += 1
                            for k, l in zip(range(i, i+4), range(j, j+4)):
                                # horizontal_search[i][j:j+4] = True
                                diag_right_search[k][l] = True
                                print(data[k][l])
                            print("\n")
    print('Diag down and to the right = %d' % (count))
    return diag_right_search, count

def diag_left_search(nrow, ncol, data):
    print("diag down and to the left")
    count=0
    diag_left_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow - (len("XMAS")-1)):
        for j in range(len("XMAS") - 1, ncol):
            if data[i][j] == "X":
                if data[i+1][j-1] == "M":
                    if data[i+2][j-2] == "A":
                        if data[i+3][j-3] == "S":
                            count += 1
                            for k, l in zip(range(i, i+4), range(j, j-4, -1)):
                                # horizontal_search[i][j:j+4] = True
                                diag_left_search[k][l] = True
                                print(data[k][l])
                            print("\n")
    print('Diag down and to the left = %d' % (count))
    return diag_left_search, count

# ============
def horizontal_reverse_search(nrow, ncol, data):
    print("horizontal reverse")
    count = 0
    horizontal_reverse_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow):
        for j in range(ncol-1, len("XMAS")-2, -1):
            if data[i][j] == "X":
                if data[i][j-1] == "M":
                    if data[i][j-2] == "A":
                        if data[i][j-3] == "S":
                            count += 1
                            for k in range(j, j-4, -1):
                                # horizontal_search[i][j:j+4] = True
                                horizontal_reverse_search[i][k] = True
                                print(data[i][k])
                            print('\n')
    print('horizontal reverse = %d' % (count))
    return horizontal_reverse_search, count

def vertical_reverse_search(nrow, ncol, data):
    print("vertical reverse")
    count = 0
    vertical_reverse_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for j in range(ncol):
        for i in range(nrow-1, len("XMAS")-2, -1):
            if data[i][j] == "X":
                if data[i-1][j] == "M":
                    if data[i-2][j] == "A":
                        if data[i-3][j] == "S":
                            count += 1
                            for k in range(i, i-4, -1):
                                # horizontal_search[i][j:j+4] = True
                                vertical_reverse_search[k][j] = True
                                print(data[k][j])
                            print("\n")
    print('vertical reverse = %d' % (count))
    return vertical_reverse_search, count

def diag_right_reverse_search(nrow, ncol, data):
    print("diagonal down to the right reverse (up and to the left)")
    count = 0
    diag_right_reverse_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow - 1, len("XMAS")-2, -1):
        for j in range(ncol - 1, len("XMAS")-2, -1):
            if data[i][j] == "X":
                if data[i-1][j-1] == "M":
                    if data[i-2][j-2] == "A":
                        if data[i-3][j-3] == "S":
                            count += 1
                            for k, l in zip(range(i, i-4, -1), range(j, j-4, -1)):
                                # horizontal_search[i][j:j+4] = True
                                diag_right_reverse_search[k][l] = True
                                print(data[k][l])
                            print("\n")
    print('Down and to the right reverse (up and to the left) = %d' % (count))
    return diag_right_reverse_search, count

def diag_left_reverse_search(nrow, ncol, data):
    print("diagonal down and to the left (up and to the right)")
    count = 0
    diag_left_reverse_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow - 1, len("XMAS") - 2, -1):
        for j in range(ncol - (len("XMAS")-1)):
            if data[i][j] == "X":
                if data[i-1][j+1] == "M":
                    if data[i-2][j+2] == "A":
                        if data[i-3][j+3] == "S":
                            count += 1
                            for k, l in zip(range(i, i-4, -1), range(j, j+4)):
                                # horizontal_search[i][j:j+4] = True
                                diag_left_reverse_search[k][l] = True
                                print(data[k][l])
                            print("\n")
    print('Down and to the left reverse (up and to the right) = %d' % (count))
    return diag_left_reverse_search, count

m1, c1 = horizontal_search(nrow, ncol, data)
m2, c2 = vertical_search(nrow, ncol, data)
m3, c3 = diag_right_search(nrow, ncol, data)
m4, c4 = diag_left_search(nrow, ncol, data)
m5, c5 = horizontal_reverse_search(nrow, ncol, data)
m6, c6 = vertical_reverse_search(nrow, ncol, data)
m7, c7 = diag_right_reverse_search(nrow, ncol, data)
m8, c8 = diag_left_reverse_search(nrow, ncol, data)

print("Total number of XMAS found: %d" % sum([c1, c2, c3, c4, c5, c6, c7, c8]))

mask_combined = [[False for _ in range(nrow)] for _ in range(ncol)]
for i in range(nrow):
    for j in range(ncol):
        mask_combined[i][j] = any([x[i][j] for x in [m1, m2, m3, m4, m5, m6, m7, m8]])
        
def mask_data(data, mask, nrow, ncol):
    data_masked = [[None for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow):
        for j in range(ncol):
            data_masked[i][j] = data[i][j] if mask[i][j] else "."
    return data_masked

def print_data(data):
    for line in data:
        print(''.join(line))

# print("masked data")
# print_data(mask_data(data, mask_combined, nrow, ncol))

    