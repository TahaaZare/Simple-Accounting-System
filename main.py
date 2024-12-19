import json
from datetime import datetime

class FinanceManager:
    def __init__(self, filename='finance_data.json'):
        self.filename = filename
        self.data = {
            'income': [],
            'expenses': []
        }
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {'income': [], 'expenses': []}

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def add_income(self, amount, category, description):
        self.data['income'].append({
            'amount': amount,
            'category': category,
            'description': description,
            'date': str(datetime.now())
        })
        self.save_data()

    def add_expense(self, amount, category, description):
        self.data['expenses'].append({
            'amount': amount,
            'category': category,
            'description': description,
            'date': str(datetime.now())
        })
        self.save_data()

    def show_summary(self):
        total_income = sum(item['amount'] for item in self.data['income'])
        total_expense = sum(item['amount'] for item in self.data['expenses'])
        balance = total_income - total_expense
        print(f'Total Income: {total_income}, Total Expenses: {total_expense}, Balance: {balance}')

    def show_data(self):
        print("Income:")
        for income in self.data['income']:
            print(income)
        print("\nExpenses:")
        for expense in self.data['expenses']:
            print(expense)

def main():
    manager = FinanceManager()
    while True:
        action = input("Choose an action (add_income, add_expense, show_summary, show_data, exit): ")
        if action == 'add_income':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            description = input("Enter description: ")
            manager.add_income(amount, category, description)
        elif action == 'add_expense':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            description = input("Enter description: ")
            manager.add_expense(amount, category, description)
        elif action == 'show_summary':
            manager.show_summary()
        elif action == 'show_data':
            manager.show_data()
        elif action == 'exit':
            break

if __name__ == "__main__":
    main()