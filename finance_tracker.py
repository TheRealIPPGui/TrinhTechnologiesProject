class Expense:

    def __init__ (self,amount, category, description):
        Amount = self.amount
        Category = self.category
        Description = self.description
    def add_expenses(expenses):
        expense_name = input("Please name the expense: \n")
        amount = input("Please enter the expense amount: \n")
        category = input("Please input the name of the category you want to store this expense in: \n")
        description = input("Please describe the expense: \n")
        expenses.update({expense_name: {"amount":amount, "category":category, "description":description}})
        print("The expense has been added!")
        input("Press Enter to continue...")
    def view_expenses(expenses):
        if expenses == {}:
            print("There is nothing to display yet!")
            input("Press Enter to continue...")
        else:
            for key, value in expenses.items():
                print(f"{key} was an expense of {value['amount']} dollars, inside the {value["category"]} category, and having a description of: {value["description"]}")
    def get_summary(expenses):
        summary = expenses.get("amount")
        print(summary)
        input("Press Enter to continue...")
    def get_top_category(summary):
        pass
        

expenses = {}
def main():
    while True:
        print(f"Welcome to the menu!")
        print(f"Option 1 - Add Expenses")
        print(f"Option 2 - View All Expenses")
        print(f"Option 3 - View Summary")
        print(f"Option 4 - View Top Category")
        print(f"Option 5- Exit")
        Chosen_Option = int(input("To choose an option, please enter an value 1-5 \n"))

        if (Chosen_Option == 1):
           Expense.add_expenses(expenses)
           
        elif (Chosen_Option == 2):
            Expense.view_expenses(expenses)
        
            


        elif (Chosen_Option == 5):
            print(f"Exitting Program...")
            break
        
        elif (Chosen_Option == 3):
            Expense.get_summary(expenses)
        else:
            print("That option is invalid!")
            input("Press Enter to continue...")

main()