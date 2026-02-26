# Finance Data Generator V1

## Project Overview
This project generates synthetic finance transaction data using Python.
It simulates revenue and expense activity for FP&A analysis, SQL practice,
and Power BI dashboards.

The script creates:
- Transaction-level finance data
- Monthly financial summary
- CSV datasets ready for analytics

## Features
- Randomized finance transactions
- Revenue and expense categorization
- Monthly profit and margin calculation
- CSV export for Power BI / SQL Server

## Technologies Used
- Python
- CSV data handling
- Random data simulation
- Basic FP&A logic

## Output Files
- finance_data_generator_v1.csv
- monthly_summary_v1.csv

## Author
Samuel Doumbe
Commercial Finance Manager transitioning into Finance Tech & Data.

## Version History

### V1 - Finance Data Generator
  -Procedural script
  -Random finance transactions
  -CSV export
  -Basic financial summary

### V2 - Finance Data Generator (Refactored)
  - Modular architecture with reusable functions
  - generate_transactions()
  - calculate_summary()
  - save_csv()
  - Monthly summary export

## Features
  - Randomized finance transaction generator
  - Revenue and Expense modeling
  - Monthly financial summary calculation
  - CSV export ready for SQL / Power BI
  - Modular Python architecture

## Project Architecture
The application follows a modular structure:

- **main()**
  - Entry point of the program
  - Handles user input (year and month)
  - Orchestrates transaction generation, summary calculation and CSV export

- **generate_transactions(year, month)**
  - Creates randomized revenue and expense records
  - Returns a structured list of finance transactions

- **calculate_summary(rows)**
  - Aggregates totals from generated data
  - Computes revenue, expenses, profit and margin KPIs

- **save_csv(filename, rows)**
  - Exports datasets into CSV format
  - Designed for downstream SQL, Excel or Power BI analysis

  


