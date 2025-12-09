import pandas as pd
import numpy as np

def clean_data(df):
    df = df.copy()

    date_cols = ["Date of Admission", "Discharge Date"]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    str_cols = [
        "Name", "Gender", "Blood Type", "Medical Condition",
        "Doctor", "Hospital", "Insurance Provider",
        "Admission Type", "Medication", "Test Results"
    ]
    for col in str_cols:
        df[col] = (
            df[col]
            .astype("string")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.title()
        )

    df["Gender"] = df["Gender"].str.capitalize()
    df["Blood Type"] = df["Blood Type"].str.upper()
    df["Test Results"] = df["Test Results"].str.capitalize()

    df["Billing Amount"] = pd.to_numeric(df["Billing Amount"], errors="coerce")

    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df.loc[df["Age"] < 0, "Age"] = np.nan

    df["LengthOfStay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days

    df = df.drop_duplicates()

    return df
