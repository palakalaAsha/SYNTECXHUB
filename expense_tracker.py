import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount"])


# Add transaction
def add_transaction(transaction_type, category, amount):

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, transaction_type, category, amount])

    print("\nTransaction Added Successfully!\n")


# View all transactions
def view_transactions():

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n------ All Transactions ------\n")

        for row in reader:
            print("{:<15}{:<12}{:<15}{}".format(*row))


# Monthly Summary
def monthly_summary():

    income = 0
    expense = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Type"].lower() == "income":
                income += float(row["Amount"])

            else:
                expense += float(row["Amount"])

    print("\n------ Monthly Summary ------")

    print(f"Total Income  : ₹{income}")

    print(f"Total Expense : ₹{expense}")

    print(f"Balance       : ₹{income-expense}")


# Search Category
def search_category(category):

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        print()

        for row in reader:

            if row["Category"].lower() == category.lower():
                print(row)
                found = True

    if not found:
        print("No Records Found")