import pandas as pd

def summary_age(df):
    return df["Age"].describe()

def admission_distribution(df):
    return df["Admission Type"].value_counts()

def pathology_top(df, n=10):
    return df["Medical Condition"].value_counts().head(n)

def billing_stats(df):
    return df["Billing Amount"].describe()

def billing_by_condition(df):
    return df.groupby("Medical Condition")["Billing Amount"].mean().sort_values(ascending=False)
