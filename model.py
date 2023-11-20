from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("numbers.csv")

x = df.loc[:, ["lev", "lcs", "gram3", "lev_init", "short_all_caps"]]
y = df.loc[:, "similar"]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
logreg = LogisticRegression(solver = "liblinear")
logreg.fit(X_train, y_train)


# Assuming you already have your trained Scikit-learn model
model = logreg  # Your trained Scikit-learn model

from joblib import dump, load
dump(model, 'model.joblib')


y_pred_test = logreg.predict(X_test)
print(accuracy_score(y_pred_test, y_test))


from transform import gen_measures
#manchester united and man utd are equal
#"FC Internazionale", "Inter Milan" not equal, bad
#"Football Club Internazionale Milano", "Inter Milan" are equal
#"New York Yankees", "New York Mets" not equal
#"LAD", "Los Angeles Dodgers" are equal
#"LAA", "Los Angeles Dodgers" are equal, bad
#"Golden Gaming", "GG" are equal
#"Borussia Monchengladbach", "Borussia Dortmund" not equal
#"Hertha Berlin", "Union Berlin" not equal
#"D-backs", "Arizona Diamondbacks" are equal
#"LA Lakers", "Los Angeles Clippers" not equal
#"LA Lakers", "Los Angeles Lakers" equal
#"Koln", "Cologne" not equal, bad
#"Manchester United", "Manchester City" not equal
test_input = gen_measures("Manchester United", "Man Utd") 
test_input.append(0)
test_input = [float(x) for x in test_input]
print(logreg.predict([test_input]))