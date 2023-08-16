#read csv file
#turn each word into ascii arr
#make new row
#write new row

def text_to_ascii(text):
    #ord() turns character into ascii
    output = [ord(c) for c in text]
    #pad up to 30 on right
    padding = [0] * 30
    output += padding
    return output[0:30]

def commafy(arr):
    output = ""
    for c in arr:
        output += str(c)
        output += ","
    return output

def new_row_str(arr1, arr2, areSimilar):
    sim_num = "1" if areSimilar else "0"
    return commafy(arr1) + commafy(arr2) + sim_num + "\n"


with open("phrases.csv", "r") as phrases:
    old_lines = phrases.readlines()
    for old_line in old_lines:
        line_list = old_line.split(",")
        phrase1arr = text_to_ascii(line_list[0])
        phrase2arr = text_to_ascii(line_list[1])
        areSimilar = line_list[2] == "True\n"
        print(new_row_str(phrase1arr, phrase2arr, areSimilar))
    