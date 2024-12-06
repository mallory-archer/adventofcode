with open('./dec4data_ex.txt', "r") as f:
    data = f.readlines()
data = [x.strip("\n") for x in data]
ncol = len(data)
nrow = len(data[0])

for x in data:
    print(x)

def diag_right_search(nrow, ncol, data):
    # print("diag down and to the right")
    count = 0
    diag_right_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow - (len("MAS")-1)):
        for j in range(ncol - (len("MAS")-1)):
            if data[i][j] == "M":
                if data[i+1][j+1] == "A":
                    if data[i+2][j+2] == "S":
                        count += 1
                        for k, l in zip(range(i, i+len("MAS")), range(j, j+len("MAS"))):
                            diag_right_search[k][l] = True
                            # print(data[k][l])
                        # print("\n")
    print('Diag down and to the right = %d' % (count))
    return diag_right_search, count

def diag_left_search(nrow, ncol, data):
    # print("diag down and to the left")
    count=0
    diag_left_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow - (len("MAS")-1)):
        for j in range(len("MAS") - 1, ncol):
            if data[i][j] == "M":
                if data[i+1][j-1] == "A":
                    if data[i+2][j-2] == "S":
                        count += 1
                        for k, l in zip(range(i, i+len("MAS")), range(j, j-len("MAS"), -1)):
                            diag_left_search[k][l] = True
                            # print(data[k][l])
                        # print("\n")
    print('Diag down and to the left = %d' % (count))
    return diag_left_search, count

# ============

def diag_right_reverse_search(nrow, ncol, data):
    # print("diagonal down to the right reverse (up and to the left)")
    count = 0
    diag_right_reverse_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow - 1, len("MAS")-2, -1):
        for j in range(ncol - 1, len("MAS")-2, -1):
            if data[i][j] == "M":
                if data[i-1][j-1] == "A":
                    if data[i-2][j-2] == "S":
                        
                        count += 1
                        for k, l in zip(range(i, i-len("MAS"), -1), range(j, j-len("MAS"), -1)):
                            diag_right_reverse_search[k][l] = True
                            # print(data[k][l])
                        # print("\n")
    print('Down and to the right reverse (up and to the left) = %d' % (count))
    return diag_right_reverse_search, count

def diag_left_reverse_search(nrow, ncol, data):
    # print("diagonal down and to the left (up and to the right)")
    count = 0
    diag_left_reverse_search = [[False for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow - 1, len("MAS") - 2, -1):
        for j in range(ncol - (len("MAS")-1)):
            if data[i][j] == "M":
                if data[i-1][j+1] == "A":
                    if data[i-2][j+2] == "S":
                        count += 1
                        for k, l in zip(range(i, i-len("MAS"), -1), range(j, j+len("MAS"))):
                            diag_left_reverse_search[k][l] = True
                            # print(data[k][l])
                        # print("\n")
    print('Down and to the left reverse (up and to the right) = %d' % (count))
    return diag_left_reverse_search, count

def mask_data(data, mask, nrow, ncol):
    data_masked = [[None for _ in range(nrow)] for _ in range(ncol)]
    for i in range(nrow):
        for j in range(ncol):
            data_masked[i][j] = data[i][j] if mask[i][j] else "."
    return data_masked

def print_data(data):
    for line in data:
        print(''.join(line))

def create_sub_matrix(data, row_start, row_end, col_start, col_end):
    return [line[col_start:col_end] for line in data[row_start:row_end]]

m3, c3 = diag_right_search(nrow, ncol, data)
m4, c4 = diag_left_search(nrow, ncol, data)
m7, c7 = diag_right_reverse_search(nrow, ncol, data)
m8, c8 = diag_left_reverse_search(nrow, ncol, data)

print("Total number of MAS found: %d" % sum([c3, c4, c7, c8]))

mask_combined = [[False for _ in range(nrow)] for _ in range(ncol)]
for i in range(nrow):
    for j in range(ncol):
        mask_combined[i][j] = any([x[i][j] for x in [m3, m4, m7, m8]])

# print("masked data")
# print_data(mask_data(data, mask_combined, nrow, ncol))

cross_mask = [(0,0), (0,2), (1, 1), (2, 0), (2, 2)]
cross_mask_binary = [[False for _ in range(3)] for _ in range(3)]
for x in cross_mask:
    cross_mask_binary[x[0]][x[1]] = True


x_count = 0
mask_combined_cross = [[False for _ in range(nrow)] for _ in range(ncol)]
# i=129
# j=37
for i in range(ncol - (len("MAS")-1)):  # range(i-3, i+6): #
    for j in range(nrow - (len("MAS") - 1)):    #range(j-3, j+6):    #
        tmat1 = create_sub_matrix(mask_combined, i, i+3, j, j+3)
        tmat2 = create_sub_matrix(data, i, i+3, j, j+3)
        if all([tmat1[x[0]][x[1]] for x in cross_mask]) and (tmat2[1][1] == "A") and (tmat2[0][0] != tmat2[2][2]) and (tmat2[0][2] != tmat2[2][0]) and all([tmat2[x[0]][x[1]] != "A" for x in [(0,0), (0,2), (2,0), (2,2)]]):
            x_count += 1
            for x in cross_mask:
                mask_combined_cross[i + x[0]][j + x[1]] = True
            # print(create_sub_matrix(mask_combined_cross, i, i+3, j, j+3))
            
            print("\n")
            print(i, j)
            print_data(mask_data(create_sub_matrix(data, i, i+3, j, j+3), create_sub_matrix(mask_combined_cross, i, i+3, j, j+3), 3, 3))
        # print_data(mask_data(create_sub_matrix(data, i-3, i+6, j-3, j+6), create_sub_matrix(mask_combined_cross, i-3, i+6, j-3, j+6), 9, 9))
            
            
print("Count of X-MAS (crossed MAS's) = %d" % x_count)
# print("masked crossed data")
# print_data(mask_data(data, mask_combined_cross, nrow, ncol))    