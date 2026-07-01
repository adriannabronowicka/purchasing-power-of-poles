import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

def load_data(file, sep):
    df = pd.read_csv(file, sep=sep)
    print(f"\n=== INSPECTION FOR: {file} ===")
    print("\n--- First rows ---")
    print(df.head())
    print("\n--- Column Names ---")
    print(df.columns)
    print("\n--- Data Structure & Types ---")
    df.info()
    print("\n--- Missing Values Count ---")
    print(df.isnull().sum())
    return df

df_fx = load_data("fx_rates.csv", ",")
df_gus = load_data("poland_wages_gus.csv", ";")
df_hicp = load_data("hicp_eurostat.csv", ",")