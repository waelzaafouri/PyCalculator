# PyCalculator - Simple Calculator

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {e}"

# Main Program
github_link = "https://github.com/waelzaafouri"  # Your GitHub link
print("="*50)
print("Hello, I'm PyCalculator! Developed by @waelzaafouri")
print("="*50)

while True:
    # Get user input for the expression
    expression = input("Enter your expression: ")

    # Validate and evaluate the expression
    result = evaluate_expression(expression)

    # Display the result with some space before it
    print("\n" + "="*50)
    print(f"Result: {result}")
    print("="*50)

    # Ask if the user wants to perform another calculation
    continue_calculating = input("\ncontinue (yes/no): ").strip().lower()

    # Check if the input is a variation of yes or no
    if continue_calculating in ['yes', 'y']:
        print("\n" + "-"*50)  # Visual separator for next iteration
        continue  # Continue the loop if 'yes' or 'y' is entered
    elif continue_calculating in ['no', 'n']:
        print("\n" + "="*50)
        print(f"Goodbye! Thanks for using PyCalculator.\nVisit my GitHub: {github_link}")
        print("="*50)
        break  # Exit the loop if 'no' or 'n' is entered
    else:
        print("Invalid input! Please enter 'yes' or 'no'.\n")
