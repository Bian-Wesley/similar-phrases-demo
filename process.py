import random

def all_possible_combinations(row):
    output = []
    for first_ind in range(len(row)):
        for second_ind in range(first_ind + 1, len(row)):
            output.append(row[first_ind] + "," + row[second_ind] + ",True\n")
    return output

def pick_rand(arr, cantbe=None):
    rand_ind = random.randint(0, len(arr) - 1)
    #recursively call pick_rand until a valid rand_ind is generated
    if rand_ind == cantbe:
        return pick_rand(arr, cantbe=cantbe)
    else:
        return arr[rand_ind]

def build_false(input1, input2):
    rand_num = random.random()
    if rand_num < 0.5:
        return input1 + "," + input2 + ",False\n"
    else:
        return input2 + "," + input1 + ",False\n"

def remove_newlines(rows):
    output = []
    for row in rows:
        if row[-1] == "\n":
            row = row[:-1]
        output.append(row)
    return output

with open("nhl.csv", "r") as teams_raw:
    rows = teams_raw.readlines()
    rows = remove_newlines(rows)
    table = []
    for row in rows:
        split_row = row.split(",")
        table.append(split_row)
    #now table is in the form 
    # [
    #   ["phrase", "phrase", "phrase"],
    #   ["phrase", "phrase"],
    #   ......
    # ]
    with open("nhl_phrases.csv", "a") as phrases:
        table_ind = 0
        for row in table:
            combo_list = all_possible_combinations(row)
            #all cells on the same row are similar phrases
            for combo in combo_list:
                phrases.write(combo)
            #need a 50/50 split of True and False in the column named similar
            #the following takes a random phrase from this row, picks a random element from another row, and makes a new false entry
            for i in range(len(combo_list)):
                from_this_row = pick_rand(row)
                different_row = pick_rand(table, cantbe=table_ind)
                from_diff_row = pick_rand(different_row)
                to_write = build_false(from_this_row, from_diff_row)
                phrases.write(to_write)
            table_ind += 1


