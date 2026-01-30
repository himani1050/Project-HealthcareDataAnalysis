import pandas as pd

df = pd.read_csv("data/raw/KaggleV2-May-2016.csv")

df.columns = df.columns.str.lower().str.replace('-', '_')

df['no_show'] = df['no_show'].map({'Yes': 1, 'No': 0})

# Convert datetime columns
df['scheduledday'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

# Remove invalid ages
df = df[(df['age'] >= 0) & (df['age'] <= 110)]

df.to_csv("data/processed/clean_data.csv", index=False)

print("ETL completed successfully")
