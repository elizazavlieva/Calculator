# Calculator
Objective:
  - Create a Python program that acts as a calculator. The program should use functions to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

Requirements:
  - Create a Python function for each of the following arithmetic operations:
    Addition
    Subtraction
    Multiplication
    Division
  - Each function should take two arguments (operands) and return the result of the corresponding operation.
  - Implement a function called main() that will serve as the main entry point of your calculator program. Inside the main() function, provide a user menu to select the operation they want to perform.
  - Display the menu with options to perform the following actions:
    Addition
    Subtraction
    Multiplication
    Division
    Quit the program
  - Allow the user to input their choice (e.g., 1 for addition) and two numbers to perform the selected operation.
  - Call the appropriate function based on the user's choice and display the result.
  - If the user selects the "Quit" option, exit the program gracefully.
Guidelines:
  -  Ensure that each arithmetic operation is implemented in a separate function for modularity.
  -  Handle division by zero error to avoid program crashes.
  -  Use a loop to keep the program running until the user chooses to quit. 
  -  Make sure to validate user input to ensure it's a valid menu choice and numeric input for operands.
  -  Display clear and user-friendly messages and prompts.
Example Output:
  Python Calculator
  Menu:

  1. Addition
  2. Subtraction
  3. Multiplication
  4. Division
  5. Quit

  Enter your choice (1/2/3/4/5): 1

  Enter the first number: 10
  
  Enter the second number: 5
  
  Result: 10 + 5 = 15

  Enter your choice (1/2/3/4/5): 5
  
  Goodbye!
