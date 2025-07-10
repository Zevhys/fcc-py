from typing import List, Dict


class Category:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.ledger: List[Dict[str, float | str]] = []

    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount: float, category: str) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        return amount <= self.get_balance()

    def __str__(self) -> str:
        title: str = f"{self.name:*^30}\n"
        items: str = ""
        for entry in self.ledger:
            description: str = entry["description"][:23]
            amount: str = f"{entry['amount']:.2f}"[:7]
            items += f"{description:<23}{amount:>7}\n"
        total: str = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories: List[Category]) -> str:
    title: str = "Percentage spent by category\n"
    withdrawals: List[Dict[str, float | str | int]] = []
    total_withdrawals: float = 0

    for category in categories:
        cat_withdraw: float = sum(
            -item["amount"] for item in category.ledger if item["amount"] < 0
        )
        withdrawals.append({"name": category.name, "amount": cat_withdraw})
        total_withdrawals += cat_withdraw

    for w in withdrawals:
        percentage = int((w["amount"] / total_withdrawals) * 100)
        w["percent"] = percentage - (percentage % 10)

    chart: str = title
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for w in withdrawals:
            chart += " o " if w["percent"] >= i else "   "
        chart += " \n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len: int = max(len(category.name) for category in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += f"{category.name[i]}  "
            else:
                line += "   "
        chart += line.rstrip() + "  \n"

    return chart.rstrip("\n")


food = Category("Food")

food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food, "\n")

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
food.withdraw(105.55, "groceries & eating")
food.transfer(50, entertainment)

print(food)
print(create_spend_chart([food, entertainment, business]))

