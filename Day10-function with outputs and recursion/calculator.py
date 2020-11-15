from art import logo

#Calculator

#Add
def add(n1, n2):
  return n1 + n2
#Substract
def substract(n1, n2):
  return n1 - n2
#Multiply
def multiply(n1, n2):
  return n1 * n2
#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  for operation in operations:
    print(operation)

  keep_calculate = True
  while keep_calculate:

    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What is the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_answer = input(f"'Y' for continue calculating with {answer}, 'N' for starting a new calculation: ").lower()
    if continue_answer == "y":
      num1 = answer
    else:
      keep_calculate = False
      calculator()

calculator()
