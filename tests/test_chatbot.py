"""
Description: Test for chatbot application
Author: AbdulRahman Hassan Bangura 
Date: 2024-03-29
Usage: From the console: python src/chatbot.py
"""
# For running tests
import unittest

# For mocking input
from unittest.mock import patch


# For functions and variables from the chatbot module
from src.chatbot import get_account, get_amount, get_balance, make_deposit, user_selection, ACCOUNTS, VALID_TASKS

class ChatbotTests(unittest.TestCase):

     # Test the get_account function with valid account number
    @patch('builtins.input')
    def test_get_account_valid_account(self, mock_input):

        # Mock user input "123456"
        mock_input.side_effect = ["123456"]
        self.assertEqual(get_account(), 123456)

    # Test the get_account function with non-numeric input
    @patch('builtins.input')
    def test_get_account_non_numeric_account(self, mock_input):

        # Mock input non-numeric string
        mock_input.side_effect = ["non_numeric_data"]

        # Expect a ValueError
        with self.assertRaises(ValueError) as context:
            get_account()

        # Check that the exception message
        self.assertEqual(str(context.exception), "Account number must be a whole number.")

    # Test the get_account function with an account number that does not exist
    @patch('builtins.input')
    def test_get_account_account_does_not_exist(self, mock_input):
        
        # Mock input with a non-existing account number
        mock_input.side_effect = ["112233"]

        # Expect a ValueError
        with self.assertRaises(ValueError) as context:
            get_account()

        # Check that the exception message
        self.assertEqual(str(context.exception), "Account number does not exist.")
    
    # Test the get_amount function with valid numeric input
    @patch('builtins.input')
    def test_get_amount_valid_amount(self, mock_input):

        # Mock user input with a valid amount
        mock_input.side_effect = ["500.01"]
        self.assertEqual(get_amount(), 500.01)

    # Test the get_amount function with non-numeric input
    @patch('builtins.input')
    def test_get_amount_non_numeric(self, mock_input):

        # Mock input as a non-numeric string
        mock_input.side_effect = ["non_numeric_data"]

        # Expect a ValueError
        with self.assertRaises(ValueError) as context:
            get_amount()
        
        # Check that the exception message
        self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")

    # Test the get_amount function with a negative input
    @patch('builtins.input')
    def test_get_amount_negative(self, mock_input):

        # Mock user input with a negative number
        mock_input.side_effect = ["-1"]

        # Expect a ValueError
        with self.assertRaises(ValueError) as context:
            get_amount()
        
        # Check that the exception message
        self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")

    # Test the get_balance function with a valid account number
    def test_get_balance_correct(self):

        # Define a valid account number
        account_number = 123456
        expected_output = "Your current balance for account 123456 is $1,000.00."
        self.assertEqual(get_balance(account_number), expected_output)


    # Test the get_balance function with a non-existing account number
    def test_get_balance_account_does_not_exist(self):

        # Define a non-existing account number

        account_number = 112233

        # Expect a ValueError
        with self.assertRaises(ValueError) as context:
            get_balance(account_number)

        # Check that the exception message
        self.assertEqual(str(context.exception), "Account number does not exist.")

    # Test the make_deposit function with a valid account number and deposit amount
    def test_make_deposit_correct_balance(self):

        # Define a valid account number
        account_number = 123456

        # Define a valid deposit amount
        amount = 1500.01
        make_deposit(account_number, amount)
        self.assertEqual(ACCOUNTS[account_number]["balance"], 2500.01)

    # Test the make_deposit function for correct success message
    def test_make_deposit_correct_output(self):

        # Define a valid account number
        account_number = 123456

        # Define the deposit amount
        amount = 1500.01
        expected_output = "You have made a deposit of $1,500.01 to account 123456."
        self.assertEqual(make_deposit(account_number, amount), expected_output)

    # Test the make_deposit function when the account does not exist
    def test_make_deposit_account_does_not_exist(self):
        
        # Define a non-existing account number
        account_number = 112233
        
        # Define a deposit amount
        amount = 1500.01
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, amount)
        
        # Check that the exception message
        self.assertEqual(str(context.exception), "Account number does not exist.")

    # Test the make_deposit function with a negative deposit amount
    def test_make_deposit_negative(self):

        # Define a non-existing account number
        account_number = 123456

        # Define a deposit amount
        amount = -50.01
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, amount)
        
        # Check that the exception message
        self.assertEqual(str(context.exception), "Invalid Amount. Amount must be positive.")

    # Test the user_selection function with a valid task in lowercase
    @patch('builtins.input')
    def test_user_selection_valid_lowercase(self, mock_input):

        # Mock user input as "balance"
        mock_input.side_effect = ["balance"]
        self.assertEqual(user_selection(), "balance")

     # Test the user_selection function with valid input but in uppercase
    @patch('builtins.input')
    def test_user_selection_valid_wrong_case(self, mock_input):

        # Mock user input in uppercase
        mock_input.side_effect = ["DEPOSIT"]
        self.assertEqual(user_selection(), "deposit")

    # Test the user_selection function with an invalid task
    @patch('builtins.input')
    def test_user_selection_invalid(self, mock_input):

        # Mock an invalid user input
        mock_input.side_effect = ["invalid_selection"]
        with self.assertRaises(ValueError) as context:
            user_selection()
        
        # Check that the exception message
        self.assertEqual(str(context.exception), "Invalid task. Please choose balance, deposit, or exit.")

# Execute all the test cases in the ChatbotTests class.
if __name__ == '__main__':
    unittest.main()

