import pandas as pd


# fx_rates CLEAN

df_fx = pd.read_csv("fx_rates.csv")

df_fx["date"] = pd.to_datetime(df_fx["date"])

df_fx.to_csv("fx_rates_clean.csv", index=False)
print("Saved: fx_rates_clean.csv")


# hicp_eurostat CLEAN

df_hicp = pd.read_csv("hicp_eurostat.csv")

df_hicp["year_month"] = df_hicp["TIME_PERIOD"]
df_hicp["date"] = pd.to_datetime(df_hicp["TIME_PERIOD"] + "-01")

df_hicp = df_hicp[["date", "year_month", "geo", "OBS_VALUE"]]
df_hicp = df_hicp.rename(columns={"OBS_VALUE": "hicp_yoy"})

df_hicp.to_csv("hicp_eurostat_clean.csv", index=False)
print("Saved: hicp_eurostat_clean.csv")


# poland_wages_gus CLEAN

df_wages = pd.read_csv("poland_wages_gus.csv", sep=";")

df_wages = df_wages[[
    "opis_okres",
    "wartosc",
    "jednostka_terytorialna"
]].copy()


df_wages = df_wages.rename(columns={
    "opis_okres": "year",
    "wartosc": "avg_yearly_gross_wage_pln",
    "jednostka_terytorialna": "country"
})

df_wages["avg_yearly_gross_wage_pln"] = (
    df_wages["avg_yearly_gross_wage_pln"]
    .str.replace(",", ".", regex=False)
    .astype(float)
)

df_wages["date"] = pd.to_datetime(df_wages["year"].astype(str) + "-01-01")

df_wages = df_wages[[
    "date",
    "year",
    "country",
    "avg_yearly_gross_wage_pln"
]]


df_wages.to_csv("poland_wages_gus_clean.csv", index=False)
print("Saved: poland_wages_gus_clean.csv")


print("DONE - all clean files saved.")