import itertools
import re

equation = input("Enter a Boolean equation (e.g., y = (p^q)^(~r^q)): ")
if '=' in equation:
    lhs, expr = equation.split('=', 1)
    lhs = lhs.strip() 
    expr = expr.strip() 
else:
    lhs = None
    expr = equation.strip()
    
expr = expr.replace('~', ' not ')
tokens = re.findall(r'\b[A-Za-z]+\b', expr)
reserved = {"and", "or", "not", "True", "False"}
variables = sorted(set(token for token in tokens if token not in reserved))

if lhs and lhs in variables:
    variables.remove(lhs)

combinations = list(itertools.product([True, False], repeat=len(variables)))

header = " | ".join(variables)
if lhs:
    header += " | " + lhs
print(header)
print("-" * len(header))

for combo in combinations:
    env = dict(zip(variables, combo))
    try:
        result = eval(expr, {}, env)
        result = bool(result)
    except Exception as e:
        result = f"Error: {e}"
    
    row = " | ".join(str(env[var]) for var in variables)
    if lhs:
        row += " | " + str(result)
    else:
        row += " | " + str(result)
    print(row)
