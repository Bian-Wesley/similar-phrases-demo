from similarity.levenshtein import Levenshtein
lev = Levenshtein()
from similarity.longest_common_subsequence import LongestCommonSubsequence
lcs_obj = LongestCommonSubsequence()
from similarity.qgram import QGram
qgram = QGram(3)

#import soundex


def len_diff(str1, str2):
    #if the strings are the same length, 1 ensures no 0 division
    return max(abs(len(str1) - len(str2)), 1)

def normalize_strcast(result, str1, str2):
    #if the difference in string length is large, then the large distance will be scaled down
    return str(result)# / len_diff(str1, str2))

def levenshtein(str1, str2):
    return normalize_strcast(lev.distance(str1, str2), str1, str2)

def lcs(str1, str2): 
    #longest common subsequence, doesn't have to occupy consecutive positions
    #The LCS distance between strings X (of length n) and Y (of length m) is n + m - 2 |LCS(X, Y)| 
    return normalize_strcast(lcs_obj.distance(str1, str2), str1, str2)

def gram3(str1, str2):
    return normalize_strcast(qgram.distance(str1, str2), str1, str2)

#soundex doesn't seem to be useful
def soundex(str1, str2):
    soundex1 = soundex(str1)
    soundex2 = soundex(str2)
    return levenshtein(soundex1, soundex2)

def lev_initials(str1, str2):
    initials1 = ""
    initials2 = ""

    wordlist1 = str1.split(" ")
    wordlist2 = str2.split(" ")

    for word1 in wordlist1:
        if word1.isupper():
            initials1 += word1
        else:
            initials1 += word1[0]

    for word2 in wordlist2:
        if word2.isupper():
            initials2 += word2
        else:
            initials2 += word2[0]
    
    return levenshtein(initials1, initials2)