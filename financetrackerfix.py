import json

expenses = {}
summary = {}
def add_expenses(expenses):
        input("Note: Please avoid duplicates for expense names, as they will be overwritten! Press Enter to continue...")
        expense_name = input("Please name the expense: \n")
        try:
            amount = float(input("Please enter the expense amount: \n"))
            while amount < 0:
                print("This value cannot be 0")
                amount = float(input("Please enter the expense amount: \n"))
            else:
                 pass
        except:
             pass
        category = input("Please input the name of the category you want to store this expense in: \n")
        description = input("Please describe the expense: \n")
        try:
            expenses.update({expense_name: {"amount": amount, "category": [category], "description": description}})
            save_expenses(expenses, filename="expenses.json")

        except UnboundLocalError:
             pass
        #Create an if state for summary where if the category exists, append the amount to it, otherwise create a new category with the amount
        if category in summary:
             summary.update({(category): summary[category] + amount})
             #Produces two strings combined, so it is being read as 2 strings as of now (FIXED)
        else:
             #summary[category].append(category) Chase's code
            try:
                summary.update({category:amount})
            except:
                 print("Please enter a valid integer for amount!")
                 input("Press Enter to continue...")
        
             
             

def view_expenses(expenses):
        if expenses == {}:
            print("There is nothing to display yet!")
            input("Press Enter to continue...")
        else:
            for key, value in expenses.items():
                print(f"{key} was an expense of {value['amount']} dollars, inside the {value["category"]} category, and having a description of: {value["description"]}")
                input("Press Enter to continue...")
def get_summary(expenses):
        if summary == {}:
             print("There is nothing to display!")
             input("Press Enter to continue...")
        else:
            
           
            return(summary)
            #Maybe a for loop where it takes in each category and updates it
def get_top_category(summary):
    if summary == {}:
         return("There is nothing to display!")
    else:
         max = max(summary, value = summary.get)
         return(max)

def save_expenses(expenses, filename="expenses.json"):
     with open('./expenses.json', 'w') as output:
          json.dump(expenses, output)
     #Use a for append instead of w if you want to append instead of overwriting

data = []
def load_expenses(filename="expenses.json"):
     try:
        with open('./expenses.json', 'r') as input:
            data = json.load(input)
        print(data)
     except FileNotFoundError:
          try:
            return(data)
          except:
               print("")
          
    


        


def main():
    load_expenses(filename="expenses.json")
    while True:


        print(f"Welcome to the menu!")
        print(f"Option 1 - Add Expenses")
        print(f"Option 2 - View All Expenses")
        print(f"Option 3 - View Summary")
        print(f"Option 4 - View Top Category")

        print(f"Option 5 - Exit")
        try:
            Chosen_Option = int(input("To choose an option, please enter an value 1-5 \n"))
        
             
            if (Chosen_Option == 1):
                add_expenses(expenses)
            
            elif (Chosen_Option == 2):
                view_expenses(expenses)
            
                


            elif (Chosen_Option == 5):
                print(f"Exitting Program...")
                break
            
            elif (Chosen_Option == 3):
                print(get_summary(expenses))
            elif(Chosen_Option == 4):
                print(get_top_category(summary))
                
                      
            else:
                print("That option is invalid!")
                input("Press Enter to continue...")
        except ValueError:
             print("Make sure to input a valid number!")
             input("Press Enter to continue...")
        

        

main()