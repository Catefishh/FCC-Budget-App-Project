# 1. Import the necessary module.
import math

# 2. Defining the Category class.
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # 3. Defining the deposit method.
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # 4. Defining the withdrawal method.
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    # 5. Defining the get_balance method.
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    # 6. Defining the transfer method.
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    # 7. Defining the check_funds method.
    def check_funds(self, amount):
        return amount <= self.get_balance()

    # 8. Defining the __str__method for printing the category.
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


# 10. Defining the create_spend_chart function.
def create_spend_chart(categories):
    # a. Calculation of the total amount spent and how much was spent for each category.
    spent = []
    for cat in categories:
        cat_spent = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent.append(cat_spent)
    total = sum(spent)
    percentages = [int((amount / total) * 100) for amount in spent]

    # b. Creation of the chart header.
    chart = "Percentage spent by category\n"

    # 13: Creation of the chart bars.
    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    # 14: Adding of the horizontal line.
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # 15: Adding the category names in a vertical manner.
    max_name_length = max(len(cat.name) for cat in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart

