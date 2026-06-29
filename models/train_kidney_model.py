import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("datasets/kidney.csv")
df.columns = df.columns.str.strip()

df["classification"] = (
    df["classification"]
    .astype(str)
    .str.strip()
    .str.replace("\t", "", regex=False)
    .replace({"ckd": 1, "notckd": 0, "not ckd": 0})
)

features = [
    "age",
    "bp",
    "sg",
    "al",
    "su",
    "bgr",
    "bu",
    "sc",
    "hemo"
]

X = df[features]
y = df["classification"].astype(int)

X = X.fillna(X.mean(numeric_only=True))

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "models/kidney_model.pkl")

print("✅ Kidney model trained successfully!")