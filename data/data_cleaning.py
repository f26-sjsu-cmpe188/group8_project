
import pandas as pd
import numpy as np

# 1. Load dataset
rawData = pd.read_csv("data/11_obesity_risk_levels_train.csv")
print("Original dataset:", rawData.shape)
rawData.columns = rawData.columns.str.strip() #stripping whitespace

# 3. Check for missing values
print("\nMissing values:")
print(rawData.isnull().sum())

# 4. Check for and remove duplicates
print("\nDuplicate rows:", rawData.duplicated().sum())
rawData = rawData.drop_duplicates()

# 5. Fix inconsistent text formatting
categorical_cols = [
    "Gender", "family_history_with_overweight",
    "FAVC", "CAEC", "SMOKE", "SCC",
    "CALC", "MTRANS"
]

for col in categorical_cols:
    rawData[col] = rawData[col].apply(
        lambda x: x.strip() if isinstance(x, str) else x
    )

# 6. Check for invalid numerical values
rawData.loc[rawData["Age"] <= 0, "Age"] = np.nan
rawData.loc[rawData["Height"] <= 0, "Height"] = np.nan
rawData.loc[rawData["Weight"] <= 0, "Weight"] = np.nan

# 7. Remove rows with missing target labels
rawData = rawData.dropna(subset=["NObeyesdad"])

# 8. Save cleaned dataset
rawData.to_csv("obesity_cleaned.csv", index=False)

print("\nCleaned dataset:", rawData.shape)
print("Cleaned data saved successfully!")
