import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("datasets/liver.csv")

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# Convert Gender to numeric
df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})

# Target column
# ILPD uses:
# 1 = Liver Disease
# 2 = No Liver Disease
df["Dataset"] = df["Dataset"].replace({
    1: 1,
    2: 0
})

# Features
X = df.drop("Dataset", axis=1)

# Target
y = df["Dataset"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "models/liver_model.pkl")

print("✅ Liver Disease model trained successfully!")