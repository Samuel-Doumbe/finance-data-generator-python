# Finance Data Generator V2
# Goal: improved structure + reusable functions

import random
import csv
import datetime
from calendar import month


def generate_transactions(year: int, month: int):
    """Return a list of rows: (trsnx_id, date, type, category, amount, description)"""
    revenue_cat = ["Product Sales", "Service Revenue", "Other Income"]
    expense_cat = ["Payroll", "Rent", "Utilities", "Marketing", "Logistics", "Travel", "Other"]

    rows = []
    trsnx_id = 1

    # Revenue generation
    for cat in revenue_cat:
        for i in range(random.randint(15, 50)):
            amount = random.randint(50000, 500000)
            day = random.randint(1, 28)
            date_val = datetime.date(year, month, day)

            rows.append((
                trsnx_id,
                date_val.isoformat(),
                "Revenue",
                cat,
                amount,
                "Auto Generated"
            ))

            trsnx_id += 1

    # Expense generation
    for cat in expense_cat:
        for i in range(random.randint(15, 50)):
            amount = random.randint(5000, 150000)
            day = random.randint(1, 28)
            date_val = datetime.date(year, month, day)

            rows.append((
                trsnx_id,
                date_val.isoformat(),
                "Expense",
                cat,
                amount,
                "Auto Generated"
            ))

            trsnx_id += 1

    return rows

def calculate_summary(rows:list):
    """Return total_revenue, total_expenses, profit, profit_margin, transaction_count"""
    total_revenue = 0
    total_expenses = 0
    for row in rows:
        row_type = row[2]
        amount = row[4]
        if row_type == "Revenue":
            total_revenue += amount
        elif row_type == "Expense":
            total_expenses += amount
    profit=total_revenue - total_expenses
    profit_margin = profit/total_revenue if total_revenue > 0 else 0
    transaction_count = len(rows)
    return {
        "total_revenue" : total_revenue,
        "total_expenses" : total_expenses,
        "profit" : profit,
        "profit_margin": profit_margin,
        "transaction_count" : transaction_count
    }

def save_csv(filename: str, rows: list):
    headers = ["trsnx_id", "date", "type", "category", "amount", "description"]
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    period=f"{year}-{month:02d}"

    rows = generate_transactions(year, month)
    save_csv("finance_data_generator_v2.csv", rows)

    print(f"Saved {len(rows)} rows to finance_data_generator_v2.csv")
    print(rows[:3])
    summary=calculate_summary(rows)

    print("\n" + "="*35)
    print(f"====FINANCE DATA GENERATOR V2====")
    print("="*35)

    print(f"Period: {period}")
    print(f"Transactions generated: {summary['transaction_count']}")

    print("\n---Financial Summary:---")
    print(f"Total Revenue: {summary['total_revenue']:,.1f}")
    print(f"Total Expenses: {summary['total_expenses']:,.1f}")
    print(f"Profit: {summary['profit']:,.1f}")
    print(f"Profit Margin: {summary['profit_margin']:.1%}")
    print(f"Transaction Count: {summary['transaction_count']}")

    with open("monthly_summary_v2.csv",'w',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["year","month","total_revenue","total_expenses","profit","profit_margin","transaction_count"])
        writer.writerow([year,month,
                         summary["total_revenue"],
                         summary["total_expenses"],
                         summary["profit"],
                         summary["profit_margin"],
                         summary["transaction_count"]
                         ])
        print(f"\nSaved: finance_data_generator_v2.csv")
        print("Saved: monthly_summary_v2.csv")


if __name__ == "__main__":
    main()
