# Purchasing Power of Poles Analysis (2014–2024)
## 📌 Project Overview

The goal of this project was to conduct a comprehensive end-to-end analysis of macroeconomic trends in Poland using multi-source historical datasets from NBP, GUS, and Eurostat. I focused on transforming raw economic data into a structured, interactive dashboard that evaluates the real purchasing power of Polish wages and measures the direct impact of global inflation on citizens' savings.

## 📊 Interactive Dashboard Preview

The video above demonstrates the interactive features of the dashboard. Detailed descriptions of the charts and pages can be found below.

### 📊 Page 1: Wages & Inflation in Poland

![Wages & Inflation in Poland](images/report_1.png)

This view connects national wage growth with local inflation to uncover the actual change in living standards:
* **The Bread Test:** A custom infographic visualization comparing how many loaves of bread an average salary could buy in 2014 vs. 2024, calculated using real historical price data.
* **Wage vs. Inflation Trend:** A combo chart correlating the sharp rise of Nominal and Real Wages with the HICP Inflation curve over the 10-year period.

### 📊 Page 2: Currency Rates & EU Inflation

![Currency Rates & EU Inflation](images/report_2.png)

This section expands the analysis to a global scale, examining the Polish Zloty's strength and positioning against international standards:
* **Inflation (HICP) vs. Currency Exchange Rates:** A combo chart tracking the average exchange rates of the EUR and USD to evaluate how global crises and domestic inflation influenced the Polish Zloty's value.
* **Global Impact on Savings:** A practical business scenario showing the real-world devaluation of cash savings (e.g., 10,000 PLN) when converted to foreign currencies over the decade.
* **EU Benchmark:** A comparative line chart pitting Poland's HICP inflation directly against the European Union average to highlight local volatility.

## 🛠️ Tech Stack & Tools

* **Power BI Desktop** – Data visualization and report building.
* **Python (Pandas, Requests)** – Automated data extraction via NBP API and end-to-end data cleaning/transformation.
* **Power Query** – Data transformation.
* **DAX (Data Analysis Expressions)** – Created calculated measures.
* **GitHub** – Documentation, version control, and project hosting.

## ⚙️ Data Pipeline & ETL Process

Before building the dashboard, I developed a three-stage data pipeline in Python to automate data ingestion, validate data quality, and transform multi-source datasets into an analytics-ready format:

1. **Extraction (`exchange_rates.py`):** Built a script utilizing the Python `requests` library to fetch historical exchange rates directly from the National Bank of Poland (NBP) API.
2. **Validation (`data_check.py`):** Developed a script to perform exploratory data analysis (EDA), detect missing values, and inspect data structures from various sources (GUS, Eurostat) before transformation.
3. **Transformation (`data_cleaning.py`):** Used `pandas` to clean raw data, filter and select specific columns required for analysis, and translate Polish source headers into English for a standardized schema. I also aligned and standardized date/year formats across all distinct datasets to ensure seamless relationship mapping and star-schema integration inside Power BI, before exporting them as clean, individual CSV files.

*The complete Python code and automated data workflow can be found in the `/data-pipeline` directory, with datasets organized into raw and processed folders.*
