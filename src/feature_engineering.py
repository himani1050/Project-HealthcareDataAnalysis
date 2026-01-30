import pandas as pd

# Load cleaned data
df = pd.read_csv("data/processed/clean_data.csv")

# ✅ Convert to datetime (MANDATORY)
df["scheduledday"] = pd.to_datetime(df["scheduledday"], errors="coerce")
df["appointmentday"] = pd.to_datetime(df["appointmentday"], errors="coerce")

# Drop rows with invalid dates (safety)
df = df.dropna(subset=["scheduledday", "appointmentday"])

# Feature: waiting time in days
df["waiting_days"] = (
    df["appointmentday"] - df["scheduledday"]
).dt.days

# Age groups
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 18, 35, 60, 110],
    labels=["Child", "Young Adult", "Adult", "Senior"]
)

# Save features
df.to_csv("data/processed/features.csv", index=False)

print("✅ Feature engineering completed successfully")
