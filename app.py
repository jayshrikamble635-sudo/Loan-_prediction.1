from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.DataFrame({
    "Gender": ["Male", "Female", "Male"]
})

le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])

print(df)
