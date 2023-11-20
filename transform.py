from measurements import levenshtein, lcs, lev_initials, gram3
import re

def gen_measures(str1, str2):
    lower1 = str1.lower()
    lower2 = str2.lower()
    return [levenshtein(lower1, lower2), lcs(lower1, lower2), gram3(lower1, lower2), lev_initials(str1, str2)]

def arr_to_str(arr):
    output = ""
    for el in arr:
        output += el
        output += ","
    output = output[:-1] + "\n"
    return output

def shorter_is_all_caps(str1, str2):
    if len(str1) <= len(str2):
        return str1.isupper()
    else:
        return str2.isupper()

new_file_str = "phrase1,phrase2,lev,lcs,gram3,lev_init,short_all_caps,similar\n"
#read phrases.csv
'''
with open("nfl_phrases.csv", "r") as phrases:
    rows = phrases.readlines()
    for row in rows:
        cols = row.split(",")
        (str1, str2, similar) =  (cols[0], cols[1], cols[2][:-1])
        if similar != "True" and similar != "False":
            continue
        #generate new columns with measurements
        new_row_arr = [str1, str2]

        processed1 = re.sub("[^a-zA-Z\d\s:]", "", str1)
        processed2 = re.sub("[^a-zA-Z\d\s:]", "", str2)
        curr_measures = gen_measures(processed1, processed2)
        new_row_arr.extend(curr_measures)

        short_all_caps = curr_measures[3] if shorter_is_all_caps(str1, str2) else "0"
        new_row_arr.append(short_all_caps)

        similar_int = "0" if similar == "False" else "1"
        new_row_arr.append(similar_int)
        
        new_file_str += arr_to_str(new_row_arr)

with open("numbers.csv", "a") as outfile:
    outfile.write(new_file_str)
#write file to csv
'''