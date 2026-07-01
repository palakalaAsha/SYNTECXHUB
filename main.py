from expense_tracker import (
    create_file,
    add_transaction,
    view_transactions,
    monthly_summary,
    search_category,
)

from charts import (
    generate_pie_chart,
    generate_bar_chart,
)

create_file()

while True:

    print("\n" + "=" * 40)
    print("      EXPENSE TRACKER CLI")
    print("=" * 40)

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Monthly Summary")
    print("5. Search by Category")
    print("6. Generate Pie Chart")
    print("7. Generate Bar Chart")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        category = input("Enter Income Category: ")
        amount = float(input("Enter Amount: "))
        add_transaction("Income", category, amount)

    elif choice == "2":
        category = input("Enter Expense Category: ")
        amount = float(input("Enter Amount: "))
        add_transaction("Expense", category, amount)

    elif choice == "3":
        view_transactions()

    elif choice == "4":
        monthly_summary()

    elif choice == "5":
        category = input("Enter Category: ")
        search_category(category)

    elif choice == "6":
        generate_pie_chart()

    elif choice == "7":
        generate_bar_chart()

    elif choice == "8":
        print("\nThank you for using Expense Tracker!")
        break

    else:
        print("\nInvalid Choice! Please try again.")