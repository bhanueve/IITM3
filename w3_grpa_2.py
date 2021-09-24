import sys
def converter(S):
    """
    takes in a alphanumeric string and returns a list of numeric values converted to float 

    Eg: input: "2 3 1 * + 9 -"
        output: [2.0, 3.0, 1.0, "*", "+", 9.0, "-"]

    """
    S = S.split()

    converted_list = []
    for i in S:
        try: 
            converted_list.append(float(i))
        except:
            converted_list.append(i)
    return converted_list

def calculate(f1, f2, C):
    """
    takes in two floats and an operator char or string and performs the corresponding operation on the numbers
    
    Eg: input: 2.0, 3.0, '+'
        output: 5.0
    """
    if C == '+':
        return f1 + f2
    elif C == '-':
        return f1 - f2
    elif C == '*':
        return f1 * f2
    elif C == '/':
        return f1 / f2
    elif C == "**":
        return f1 ** f2
    else:
        print("Incorrect calculation operator given. ")
        sys.exit()

def EvaluateExpression(exp):
    """
    takes in a arithmetic expression postfix form string and uses a stack

    to evaluate the expression and returns the result
    Eg: input: "2 3 1 * + 9 -"
        output: -4.0

    """
    operator_list = ["+", "-", "*", "/", "**"]
    converted_list = converter(exp)
    stack = []
    for i in converted_list:
        if i not in operator_list:
            stack.insert(0, i)
        else:
            value2 = stack.pop(0)
            value1 = stack.pop(0)
            result = calculate(value1, value2, i)
            stack.insert(0, result)
    return stack[0]
        