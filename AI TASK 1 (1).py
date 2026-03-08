import re

def dynamic_calculator():
    print("Dynamic Calculator")
    print("Type 'exit' to quit")

    while True:
        expr = input("Enter expression: ")

        if expr.lower() == "exit":
            break

        try:
            expr = re.sub(r'(\d)\(', r'\1*(', expr)
            result = eval(expr)
            print("Result:", result)
        except:
            print("Invalid expression")

dynamic_calculator()