import requests
import pandas as pd
from datetime import timedelta


# CONFIG

START_DATE = "2014-01-01"
END_DATE = "2026-03-31"
MAX_DAYS = 93

CURRENCIES = ["EUR", "USD"]


# FUNCTION: fetch chunk

def fetch_nbp_data(currency, start_date, end_date):
    url = f"https://api.nbp.pl/api/exchangerates/rates/A/{currency}/{start_date}/{end_date}/?format=json"

    r = requests.get(url)

    if r.status_code != 200:
        print(f"Error {currency} {start_date} - {end_date}: {r.status_code}")
        return pd.DataFrame()

    data = r.json()
    df = pd.DataFrame(data["rates"])

    df["currency"] = currency
    df["date"] = pd.to_datetime(df["effectiveDate"])
    df = df.rename(columns={"mid": "rate"})

    return df[["date", "currency", "rate"]]


# FUNCTION: split date range

def generate_chunks(start, end, max_days=93):
    chunks = []

    current = pd.to_datetime(start)
    end = pd.to_datetime(end)

    while current < end:
        chunk_end = current + timedelta(days=max_days)

        if chunk_end > end:
            chunk_end = end

        chunks.append((current.strftime("%Y-%m-%d"),
                       chunk_end.strftime("%Y-%m-%d")))

        current = chunk_end + timedelta(days=1)

    return chunks


# MAIN PROCESS

all_data = []

for currency in CURRENCIES:
    print(f"Fetching {currency}...")

    chunks = generate_chunks(START_DATE, END_DATE)

    for start, end in chunks:
        df_chunk = fetch_nbp_data(currency, start, end)
        all_data.append(df_chunk)


# CONCAT ALL DATA

df = pd.concat(all_data, ignore_index=True)


# FEATURE ENGINEERING

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["year_month"] = df["date"].dt.to_period("M").astype(str)

# monthly average
df_monthly = (
    df.groupby(["year_month", "currency"])["rate"].mean().reset_index().rename(columns={"rate": "avg_rate"})
)

# convert to proper date (Power BI friendly)
df_monthly["date"] = pd.to_datetime(df_monthly["year_month"] + "-01")

# reorder columns
df_monthly = df_monthly[["date", "year_month", "currency", "avg_rate"]]


# SAVE

df_monthly.to_csv("fx_rates.csv", index=False)

print("DONE - file saved: fx_rates.csv")
print(df_monthly.head())