import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer, KNNImputer

df = pd.read_csv("./content/water_potability.csv")

X = df[['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity']]
y = df['Potability']

simputer = SimpleImputer(strategy='median')
x_impute = simputer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(x_impute, y, test_size=0.2, random_state=42)

rand_forest = RandomForestClassifier(n_estimators=100, random_state=42)
rand_forest.fit(X_train, y_train)

y_prediction = rand_forest.predict(X_test)

accuracy = rand_forest.score(X_test, y_test)

print(f"Accuracy: {accuracy}")
