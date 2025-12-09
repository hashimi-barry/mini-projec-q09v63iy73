import plotly.express as px

def age_distribution(df):
    fig = px.histogram(df, x="Age", nbins=25, title="Distribution de l'âge")
    return fig

def admission_bar(df):
    fig = px.bar(
        df["Admission Type"].value_counts(),
        title="Répartition par type d'admission"
    )
    return fig

def scatter_los_billing(df):
    fig = px.scatter(
        df,
        x="LengthOfStay",
        y="Billing Amount",
        color="Medical Condition",
        title="Durée de séjour vs montant facturé",
        hover_data=["Name", "Hospital"]
    )
    return fig
