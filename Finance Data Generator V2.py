# Finance Data Generator V2
# Goal: improved structure + reusable functions (work in progress)

import random
import csv
import datetime

def generate_transactions(year: int, month: int):
    """Return a list of rows: (trsnx_id, date, type, category, amount, description)"""
    revenue_cat = ["Product Sales", "Service Revenue", "Other Income"]
    expense_cat = ["Payroll", "Rent", "Utilities", "Marketing", "Logistics", "Travel", "Other"]

    rows = []
    trsnx_id = 1

    # TODO: generate revenue rows
    # TODO: generate expense rows

    return rows

def save_csv(filename: str, rows: list):
    headers = ["trsnx_id", "date", "type", "category", "amount", "description"]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    rows = generate_transactions(year, month)
    save_csv("finance_data_generator_v2.csv", rows)

    print(f"Saved {len(rows)} rows to finance_data_generator_v2.csv")

if __name__ == "__main__":
    main()Finance Data Genarator V2
