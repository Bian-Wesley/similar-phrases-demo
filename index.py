from flask import Flask, request
from joblib import load
import sklearn
from measurements import levenshtein, lcs, gram3, lev_initials
import re
import json

def gen_measures(str1, str2):
    lower1 = str1.lower()
    lower2 = str2.lower()
    return [levenshtein(lower1, lower2), lcs(lower1, lower2), gram3(lower1, lower2), lev_initials(str1, str2)]

def shorter_is_all_caps(str1, str2):
    if len(str1) <= len(str2):
        return str1.isupper()
    else:
        return str2.isupper()

def is_women(team):
    return "W " in team or " W" in team or "(W)" in team

app = Flask(__name__)

@app.route('/')
def home():
    str1 = request.args.get("str1")
    str2 = request.args.get("str2")
    if str1 == None or str2 == None:
        return json.dumps({
            "match": False,
            "status": "Error, invalid input"
        })
    if (is_women(str1) and not is_women(str2)) or (not is_women(str1) and is_women(str2)): 
        #one team is women, other isnt cant be match 
        return json.dumps({
            "match": False,
            "status": "Success, Not a match"
        })
    processed1 = re.sub("[^a-zA-Z\d\s:]", "", str1)
    processed2 = re.sub("[^a-zA-Z\d\s:]", "", str2)
    measures = gen_measures(processed1, processed2)

    short_all_caps = measures[3] if shorter_is_all_caps(str1, str2) else 0
    measures.append(short_all_caps)
    prediction = "unknown"
    model = load("model.joblib")
    outputs = ["Not a match", "Match"]
    signal = model.predict([measures])[0]
    prediction = outputs[signal]

    return json.dumps({
        "match": prediction == "Match",
        "status": "Success, " + prediction
    })
if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = False, host = 8080)
    #netstat -tulpn
#https://stackoverflow.com/questions/24349335/python-flask-application-is-running-after-closing