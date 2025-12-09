import streamlit as st
import pandas as pd

from scripts.cleaning import clean_data
from scripts.viz import (
    age_distribution,
    admission_bar,
    scatter_los_billing
)

st.set_page_config(page_title="EDA Hospital", layout="wide")

st.title("Mini-Projet : Dashboard Hospitalier (EDA)")


@st.cache_data
def load_and_clean():
    df = pd.read_csv("data/healthcare_dataset.csv")
    df = clean_data(df)
    df.to_csv("data/healthcare_dataset_clean.csv", index=False)
    return df


df = load_and_clean()

st.subheader("Aperçu du dataset")
st.write(df.head())


# --- Visualisations ---
st.subheader("Distribution de l'âge")
fig1 = age_distribution(df)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Répartition par type d'admission")
fig2 = admission_bar(df)
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Durée de séjour vs montant facturé")
fig3 = scatter_los_billing(df)
st.plotly_chart(fig3, use_container_width=True)
