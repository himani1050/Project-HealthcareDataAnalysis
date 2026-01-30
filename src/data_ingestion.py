import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Load cleaned CSV
df = pd.read_csv("data/processed/clean_data.csv")

# Rename columns explicitly
df = df.rename(columns={
    "patientid": "patient_id",
    "appointmentid": "appointment_id",
    "scheduledday": "scheduled_day",
    "appointmentday": "appointment_day",
    "hipertension": "hypertension",
    "handcap": "handicap"
})

# Convert datetimes
df["scheduled_day"] = pd.to_datetime(df["scheduled_day"])
df["appointment_day"] = pd.to_datetime(df["appointment_day"])

# ✅ Explicit column list (CRITICAL)
columns = [
    "appointment_id",
    "patient_id",
    "gender",
    "scheduled_day",
    "appointment_day",
    "age",
    "neighbourhood",
    "scholarship",
    "hypertension",
    "diabetes",
    "alcoholism",
    "handicap",
    "sms_received",
    "no_show"
]

df = df[columns]

# Encode password
password = quote_plus("mySQL@123")

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost/healthcare_analytics"
)

# Insert data
df.to_sql(
    name="appointments",
    con=engine,
    if_exists="append",   # NEVER replace in prod
    index=False,
    chunksize=1000,
    method="multi"
)

print("✅ Data inserted successfully without schema conflicts")
