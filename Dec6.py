def print_map(map):
    for row in map:
        print(''.join(row))

def map_path(map, locations_visited, locations_direction, direction_arrow):
    for idx, x in enumerate(locations_visited[:-1]):
        map[x[0]][x[1]] = direction_arrow[locations_direction[idx]]
    return map

def turn_right(current_direction):
    if current_direction == "up":
        return "right"
    if current_direction == "right":
        return "down"
    if current_direction == "down":
        return "left"
    if current_direction == "left":
        return "up"

# get location of barriers
def get_barrier_locations(map):
    nrows = len(map)
    ncols = len(map[0])

    barrier_locations = []
    for i in range(nrows):
        for j in range(ncols):
            if map[i][j] == "#":
                barrier_locations.append((i, j))
    return barrier_locations

def get_guard_info(map):
    nrows = len(map)
    ncols = len(map[0])

    for i in range(nrows):
        for j in range(ncols):
            if map[i][j] == "^":
                current_guard_location = (i, j)
    current_guard_direction = "up"
    return current_guard_location, current_guard_direction
    
# have guard traverse map
def traverse_map(barrier_locations, current_guard_location, current_guard_direction, ncols, nrows, direction_increment):
    guard_on_map = True
    guard_in_loop = False
    locations_visited = [current_guard_location]
    locations_direction = [current_guard_direction]
    location_turns = list()
    # max_steps = ncols * nrows * 4 # infinite loop guard
    while guard_on_map and not guard_in_loop:
        next_guard_location = (current_guard_location[0] + direction_increment[current_guard_direction][0], current_guard_location[1] + direction_increment[current_guard_direction][1])
        if (next_guard_location[0] < 0) or (next_guard_location[0] >= nrows) or (next_guard_location[1] < 0) or (next_guard_location[1] >= ncols):
            guard_on_map = False
        # check for barrier
        if next_guard_location in barrier_locations:
            # if barrier turn right and update current guard direction
            current_guard_direction = turn_right(current_guard_direction)
            if sum([current_guard_location == previous_turn_location for previous_turn_location in location_turns]) > 2:
                guard_in_loop = True
            location_turns.append(current_guard_location)
        else:
            # update location
            current_guard_location = next_guard_location
            locations_visited.append(current_guard_location)
            locations_direction.append(current_guard_direction)

    return locations_visited, guard_in_loop, locations_direction

direction_increment = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
direction_arrow = {"up": "^", "down": "v", "left": "<", "right": ">"}

# -----------

with open("dec6data.txt", "r") as f:
    original_map = f.readlines()
original_map = [[char for char in line.strip("\n")] for line in original_map]

# print_map(original_map)

start_guard_location, start_guard_direction = get_guard_info(original_map)
original_map_ncols = len(original_map)
original_map_nrows = len(original_map[0])

# ---------- part 1
original_barrier_locations = get_barrier_locations(original_map)
locations_visited, _, locations_direction = traverse_map(original_barrier_locations, start_guard_location, start_guard_direction, original_map_ncols, original_map_nrows, direction_increment)

# visualize path (optional)        
# print_map(map_path(original_map, locations_visited, locations_direction, direction_arrow))
    
# print number of locations visited
print("Unique locations visited: %d" % len(set(locations_visited[:-1])))

# ---------- part 2
import copy
guard_loops_TF = []
new_barrier_placement = []
for i in range(original_map_nrows):
    # print("new barrier in i=%d" % (i))
    for j in range(original_map_ncols):
        print("new barrier in i=%d j=%d" % (i, j))
        current_barrier_locations = copy.deepcopy(original_barrier_locations)
        if (i, j) not in current_barrier_locations:
            new_barrier_placement.append((i, j))
            current_barrier_locations.append((i, j))

            _, loop, _ = traverse_map(current_barrier_locations, start_guard_location, start_guard_direction, original_map_ncols, original_map_nrows, direction_increment)
            guard_loops_TF.append(loop)

# print number of locations visited
print("Number of barrier to cause guard loop: %s" % sum(guard_loops_TF))
# print("New barrier placements for loops %s" % ([x for i, x in enumerate(new_barrier_placement) if guard_loops_TF[i]]))

# --- Debugging visualization
# for i, x in enumerate(new_barrier_placement):
#     if guard_loops_TF[i]:
#         new_map = copy.deepcopy(original_map)
#         new_map[x[0]][x[1]] = "O"

        # --- Debugging visualization
        # current_barrier_locations = copy.deepcopy(original_barrier_locations)
        # current_barrier_locations.append(x)
        # locations_visited, loop, locations_direction = traverse_map(current_barrier_locations, start_guard_location, start_guard_direction, original_map_ncols, original_map_nrows, direction_increment)
        # if not loop:
        #     print("Warning double check new barrier %d" % i)

        # --- Debugging visualization
        # new_map = map_path(new_map, locations_visited, locations_direction, direction_arrow)
        # print('For new barrier placed at (%d, %d)' % (x))
        # print_map(new_map)