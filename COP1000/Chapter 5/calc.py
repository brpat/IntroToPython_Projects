# Create a calc, with 4 opperands.
#4 variables, two operands, operator, and result.

operand1 = int(input("Enter first operand: "))
operator = str(input("Enter operator: "))
operand2 = int(input("Enter second operand: "))
result = int

if(operator == "+"):
    result = operand1 + operand2
    print("Result", result)

if(operator == "-"):
    result = operand1 - operand2
    print("Result", result)

if(operator == "*"):
    result = operand1 * operand2
    print("Result", result)

if(operator == "/"):
    result = operand1 / operand2
    print("Result", result)

