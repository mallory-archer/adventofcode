import copy

def get_median(obs:list):
    if len(obs) % 2 == 0:
        return None
    else:
       return obs[int(len(obs)/2)] 

def check_updates(updates):
    updates_check = dict()
    for uidx, update in enumerate(updates):
        updates_check.update({uidx: True})
        for page_index, page in enumerate(update):
            try:
                for r in rules[page]:
                    try:
                        if page_index > update.index(r):
                            updates_check.update({uidx: False})
                    except ValueError:
                        pass
            except KeyError:
                pass
    return updates_check

def reorder_updates(updates):
    for _, update in enumerate(updates):
        for page_index, page in enumerate(update):
            try:
                indices_violations = list()
                for r in rules[page]:
                    try:
                        if page_index > update.index(r):
                            indices_violations.append(update.index(r))
                    except ValueError:
                            pass
                if len(indices_violations) > 0:
                    update.remove(page)
                    update.insert(min(indices_violations), page)
            except KeyError:
                    pass
    return updates

with open('./dec5data_rules.txt', "r") as f:
    data_rules = f.readlines()

with open('./dec5data_pages.txt', "r") as f:
    data_pages = f.readlines()

# pre-process rules
data_rules = [rule.strip("\n").split("|") for rule in data_rules]
rules = {int(y): list() for y in set([x[0] for x in data_rules])}
for rule in data_rules:
    rules[int(rule[0])].append(int(rule[1]))
# print(rules)

# pre-process updates
updates = [[int(x) for x in line.strip("\n").split(",")] for line in data_pages]

# Part 1
updates_ok = check_updates(updates)
print("The sum of the valid medians is %d" % sum([get_median(update) for uidx, update in enumerate(updates) if updates_ok[uidx]]))

# Part 2
updates_reordered = reorder_updates([u for i, u in enumerate(copy.deepcopy(updates)) if not updates_ok[i]])
print("The sum of the medians for the reordered updates is %d" % sum([get_median(update) for update in (updates_reordered)]))