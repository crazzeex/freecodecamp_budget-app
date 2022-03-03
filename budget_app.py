import math

class Category:

    def __init__(self, nam):
        self.name = nam
        self.ledger = []
        self.balance = 0
        self.withdrawals = 0
        self.transaction = False

    #use this so that when you print an object, this comes out instead
    def __str__(self):
        self.display = "{:*^30}\n".format(self.name)
        for i in range(len(self.ledger)):
            truncated = self.ledger[i]["description"][:23]
            num = "{:.2f}".format(self.ledger[i]["amount"])
            self.display += "{0:<23}{1:>7}\n".format(truncated, num)
        self.display += "Total: {:.2f}".format(self.balance)
        return (self.display)

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount":amount,"description":desc})
        self.balance += amount

    def withdraw(self, amount, desc=""):
        self.transaction = self.check_funds(amount)
        if self.transaction == True:
            self.ledger.append(({"amount":-abs(amount),"description":desc}))
            self.balance -= amount
            self.withdrawals += amount
        return self.transaction
        
    def get_balance(self):
        return (self.balance)

    def transfer(self, amount, other_category):
        self.transaction = self.check_funds(amount)
        if self.transaction == True:
                desc1 = "Transfer to {0}".format(other_category.name)
                self.ledger.append({"amount":-abs(amount),"description": desc1})
                self.balance -= amount
                self.withdrawals += amount
                
                desc2 = "Transfer from {0}".format(self.name)
                other_category.ledger.append({"amount":amount,"description":desc2})
                other_category.balance += amount
        return self.transaction

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

def create_spend_chart(categories):
    percentage = []
    total = 0
    #calculate total withdrawal
    for i in categories:
        total += i.withdrawals

    #get percentages of the individual withdrawals for the categories
    for i in categories:
        category_withdrawal_perc = (i.withdrawals/total)*100
        rounded_withdrawal_perc = math.floor(category_withdrawal_perc/10)*10
        percentage.append(rounded_withdrawal_perc)
    
    #format the chart
    overall_chart = "Percentage spent by category\n"
    sidebars = ["100|", "90|", "80|", "70|", "60|", "50|", "40|", "30|", "20|", "10|", "0|"]
    for i in range (len(sidebars)):
        overall_chart += "{0:>4}".format(sidebars[i])
        for j in percentage:
            if j == percentage[-1]:
                if j >= int(sidebars[i].rstrip("|")):
                    overall_chart += " o  "
                else:
                    overall_chart += "    "
            else:
                if j >= int(sidebars[i].rstrip("|")):
                    overall_chart += " o "
                else:
                    overall_chart += "   "
        overall_chart += "\n"
    #format the "-"
    overall_chart += "{0:>{1}}\n".format("-"*(3*(len(categories))+1), 3*(len(categories))+5)
    
    #List of actual names of the categories
    category_names = []
    for i in range(len(categories)):
        category_names.append(categories[i].name)
    
    #make each name as long as the longest
    longest_string = max(category_names, key=len)
    for i in range(len(category_names)):
        while len(category_names[i]) < len(longest_string):
            category_names[i] += " "

    #express them vertically
    vert_names = []
    for i in range(len(longest_string)):
        for j in range(len(category_names)):
            vert_names.append(category_names[j][i])
    
    for i in range(len(vert_names)):
        if i %(len(category_names)) == 0:
            overall_chart +=  "    {:^3}".format(vert_names[i])
        elif i%(len(category_names)) == len(category_names) -1:
            if i == len(vert_names) -1:
                overall_chart += " {}  ".format(vert_names[i])
            else:
                overall_chart += " {}  \n".format(vert_names[i])
        else:
            overall_chart += "{:^3}".format(vert_names[i])
            
    return (overall_chart)

# tests
# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# #print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)


# print(food)
# print(clothing)
# print(auto)

# create_spend_chart([food,clothing,auto])


# test2
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")


food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
create_spend_chart([business,food,entertainment])