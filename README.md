# Finance Data Generator (Python)

## Project Overview
Python Finance Data Generator designed for FP&A simulation, SQL analytics testing and Power BI dashboard prototyping.

This project generates synthetic finance transaction data using Python.
It simulates revenue and expense activity for analytics workflows and creates:

- Transaction-level finance datasets
- Monthly financial KPI summaries
- CSV outputs ready for SQL, Excel and Power BI

---

## Key Features
- Randomized finance transaction generator
- Revenue and Expense modeling
- Monthly financial summary calculation
- CSV export ready for SQL / Power BI
- Modular Python architecture (V2)

---

## Technologies Used
- Python
- CSV data handling
- Random data simulation
- Basic FP&A logic

---

## Output Files
### Version 1
- `finance_data_generator_v1.csv`
- `monthly_summary_v1.csv`

### Version 2
- `finance_data_generator_v2.csv`
- `monthly_summary_v2.csv`

---

## Project Architecture
The application follows a modular structure:

### **main()**
- Entry point of the program
- Handles user input (year and month)
- Orchestrates transaction generation, summary calculation and CSV export

### **generate_transactions(year, month)**
- Creates randomized revenue and expense records
- Returns a structured list of finance transactions

### **calculate_summary(rows)**
- Aggregates totals from generated data
- Computes revenue, expenses, profit and margin KPIs

### **save_csv(filename, rows)**
- Exports datasets into CSV format
- Designed for downstream SQL, Excel or Power BI analysis

---

## Version History

### V1 — Finance Data Generator
- Procedural Python script
- Random finance transactions
- CSV export
- Basic financial summary

### V2 — Finance Data Generator (Refactored)
- Modular architecture with reusable functions
- `generate_transactions()`
- `calculate_summary()`
- `save_csv()`
- Monthly summary export

---

## Use Cases
- FP&A scenario modeling
- Synthetic datasets for SQL practice
- Power BI dashboard prototyping
- Financial KPI simulations

---

## Author
**Samuel Doumbe**  
Commercial Finance Manager transitioning into Finance Tech & Data.

  


