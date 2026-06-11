import pandas as pd
from app.models.lead import Lead

REQUIRED_COLUMNS = [
    "full_name",
    "headline",
    "company",
    "industry",
    "location",
    "email",
    "linkedin_url"
]


def read_csv(file):
    df = pd.read_csv(file)

    missing_columns = [
        col
        for col in REQUIRED_COLUMNS
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {', '.join(missing_columns)}"
        )

    return df

def convert_rows_to_leads(df):
    leads = []

    for _, row in df.iterrows():

        lead = Lead(
            full_name=row.get("full_name"),
            headline=row.get("headline"),
            company=row.get("company"),
            industry=row.get("industry"),
            location=row.get("location"),
            email=row.get("email"),
            linkedin_url=row.get("linkedin_url")
        )

        leads.append(lead)

    return leads