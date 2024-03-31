"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: Abdul Rahman Hasssan Bangura 
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS

# Define a dictionary of accounts.
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:

def get_account() -> int:

    """
    Get the user's account number.
    """

     # Account number input.
    account_number = input("Please enter your account number: ")

    try:
        # Convert the input string into an integer.
        account_number = int(account_number)
    
    except ValueError:
        # Notify the user and re-raise the exception.
        raise ValueError("Account number must be a whole number.")
    
    # Check if the account number exists in the ACCOUNTS dictionary.
    if account_number not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    
    # Return the valid account number.
    return account_number

def get_amount() -> float:
    """
    Get the transaction amount from the user.
    """
    # Prompt for amount input.
    amount = input("Enter the transaction amount: ")
    
    try:
        # Convert the input string to a float.
        amount = float(amount)

        if amount <= 0:
            raise ValueError("Invalid amount. Please enter a positive number.")
    
    except ValueError as e:
        if "could not convert string to float" in str(e):
            raise ValueError("Invalid amount. Amount must be numeric.") 
        else:
            raise 

    # Return the validated amount as a float.
    return amount

def get_balance(account: int) -> str:
    """
    Get the balance for the given account.
    """
    # Check if the account exists in the ACCOUNTS dictionary.
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    
    balance = ACCOUNTS[account]["balance"]
    return f"Your current balance for account {account} is ${balance:,.2f}."

def make_deposit(account: int, amount: float) -> str:
    """
    Make a deposit into the specified account.
    """
    # Check if the account exists in the ACCOUNTS dictionary.
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    
    if amount <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")
    
    # Update the account balance.
    ACCOUNTS[account]["balance"] += amount

    return f"You have made a deposit of ${amount:,.2f} to account {account}."

def user_selection() -> str:
    """
    Prompt the user to select a task (balance, deposit, or exit).
    """
    selection = input("What would you like to do (balance/deposit/exit)? ")
    
    # Convert input to lowercase.
    selection = selection.lower()
    
    if selection not in VALID_TASKS:
        raise ValueError("Invalid task. Please choose balance, deposit, or exit.")
    
    # Return the valid selection.
    return selection

## GIVEN CHATBOT FUNCTION

def chatbot():
    """
    Main chatbot function to interact with the user.
    """
    print("Welcome! I'm the PiXELL River Financial Chatbot! Let's get chatting!")
    
    while True:
        try:
            # Prompt the user to select a task.
            selection = user_selection()
            
            if selection == "exit":
                print("Thank you for banking with PiXELL River Financial.")
                break
            
            elif selection == "balance":
                # Prompt for the account number.
                while True:
                    try:
                        account = get_account()
                        break
                    except ValueError as e:
                        print(e)
                
                # Retrieve and print the account balance.
                print(get_balance(account))
            
            elif selection == "deposit":
                # Prompt for the account number.
                while True:
                    try:
                        account = get_account()
                        break
                    except ValueError as e:
                        print(e)
                
                # Prompt for the deposit amount.
                while True:
                    try:
                        amount = get_amount()
                        break
                    except ValueError as e:
                        print(e)
                        continue
                
                # Make the deposit and print the result.
                print(make_deposit(account, amount))
        
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    chatbot()