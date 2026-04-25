import json
    




def add_expenses(expenses, summary):
        input("Note: Please avoid duplicates for expense names, as they will be overwritten! Press Enter to continue...")
        expense_name: str = input("Please name the expense: \n")
    #You can't return to a try function once interuppted, so make a loop of some sort
        try:
             amount: float = float(input("Please enter the expense amount: \n"))
             if amount == float:
                    while amount < 0:
                     print("This value cannot be 0")
                     amount = float(input("Please enter the expense amount: \n"))
                
        except ValueError:
            print("Please enter a positive number!")
        #This pass is so that rather than printing a msg, it moves to the next try and except so that it only has to display one print message telling the user to fix their stuff
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
                summary.update({category:   amount})
            except:
                 pass
                 print("Please enter a valid integer for amount!")
                 input("Press Enter to continue...")
        
             
             

def view_expenses(expenses: dict):
        if expenses == {}:
            print("There is nothing to display yet!")
            input("Press Enter to continue...")
        else:
            for key, value in expenses.items():
                print(f"{key} was an expense of {value['amount']} dollars, inside the {value["category"]} category, and having a description of: {value["description"]}")
                input("Press Enter to continue...")
def get_summary(expenses: dict, summary: dict):
        if summary == {}:
             print("There is nothing to display!")
             input("Press Enter to continue...")
        else:
            
            
           
            return(summary)
        
            #Maybe a for loop where it takes in each category and updates it
def get_top_category(summary: dict):
    if summary == {}:
         return("There is nothing to display!")
    else:
         for k, v in summary.items():
              global mv
              if v>   mv:
                
                   mv = v
                   mk = k
         print(f"The top category is {mk} with the total being {mv}")
    #def save_expenses(expenses_dict, new_expense, filename="expenses.json"):

def save_expenses(expenses_dict: dict, filename="expenses.json"):
  # Update the expenses dictionary here before writing to the file
  expenses_dict

  # Open the file as write to rewrite ("a" is append) the entire JSON file after we update the expenses dict
  
  with open(filename, "w") as output:
    #json.dump(expenses, output, indent=2) # indent=2 makes the JSON look nice
        json.dump(expenses_dict, output)
 
#def save_expenses(expenses, filename="expenses.json"):
     #with open('./expenses.json', 'w') as output:
          #json.dump(expenses, output)
          #expenses.write("\n")
     #Use a for append instead of w if you want to append instead of overwriting

def load_expenses(filename="expenses.json"):
     try:

            with open('./expenses.json', 'r') as input:
                data = json.load(input)
            return(data)
            #with open('./expenses.json', 'r') as input:
                #for line in input:
                    #data.append(json.load(input))
                #print(data)

     except FileNotFoundError:
         print("No expense files found, create a new one! \n")




     except FileNotFoundError:
          try:
            return(data)
          except:
               print("")          
    


        


def main():
    expenses: dict = {}
    summary:dict = {}    
    mk = None #Max value
    mv = 0


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
                add_expenses(expenses, summary)
            
            elif (Chosen_Option == 2):
                view_expenses(expenses)
            
                


            elif (Chosen_Option == 5):
                print(f"Exitting Program...")
                break
            
            elif (Chosen_Option == 3):
                print(get_summary(expenses, summary))
           
            elif(Chosen_Option == 4):
                print(get_top_category(summary))
                
                      
            else:
                print("That option is invalid!")
                input("Press Enter to continue...")
        except ValueError:
             print("Make sure to input a valid number!")
             input("Press Enter to continue...")
        

        

main()