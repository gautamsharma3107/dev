"""
MINI PROJECT 2: Expression Evaluator
=====================================
Build a calculator that evaluates mathematical expressions

Features:
1. Support +, -, *, / operations
2. Handle operator precedence (* and / before + and -)
3. Support parentheses
4. Handle negative numbers

This uses TWO stacks:
- One for numbers (operands)
- One for operators
"""

print("=" * 60)
print("MINI PROJECT: EXPRESSION EVALUATOR")
print("=" * 60)

print("""
Examples:
- "2 + 3"        → 5
- "2 + 3 * 4"    → 14 (not 20!)
- "(2 + 3) * 4"  → 20
- "10 - 2 * 3"   → 4
- "100 / 10 / 2" → 5
""")

# ============================================================
# BASIC CALCULATOR (Numbers and +, -, *, /)
# ============================================================

def basic_calculate(expression):
    """
    Evaluate expression with +, -, *, /
    No parentheses in this version
    
    Algorithm:
    1. Process multiplication and division immediately
    2. Store results for addition and subtraction
    3. Sum all stored values at the end
    """
    # TODO: Implement
    pass


# ============================================================
# ADVANCED CALCULATOR (With parentheses)
# ============================================================

def calculate(expression):
    """
    Evaluate expression with +, -, *, / and parentheses
    
    Uses two stacks approach or recursive descent
    """
    # TODO: Implement
    pass


# ============================================================
# HELPER: Tokenize expression
# ============================================================

def tokenize(expression):
    """
    Convert expression string to list of tokens
    
    "2 + 3 * 4" → ['2', '+', '3', '*', '4']
    "(10-2)*3" → ['(', '10', '-', '2', ')', '*', '3']
    """
    tokens = []
    current_number = ""
    
    for char in expression:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                tokens.append(current_number)
                current_number = ""
            if char in "+-*/()":
                tokens.append(char)
    
    if current_number:
        tokens.append(current_number)
    
    return tokens


# ============================================================
# SHUNTING YARD ALGORITHM (Convert Infix to Postfix)
# ============================================================

def infix_to_postfix(expression):
    """
    Convert infix expression to postfix using Shunting Yard algorithm
    
    Infix: "2 + 3 * 4"
    Postfix: "2 3 4 * +"
    
    This handles operator precedence correctly!
    """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []
    
    tokens = tokenize(expression)
    
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token in precedence:
            while (operator_stack and 
                   operator_stack[-1] != '(' and
                   operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # Remove '('
    
    while operator_stack:
        output.append(operator_stack.pop())
    
    return output


def evaluate_postfix(tokens):
    """
    Evaluate postfix expression
    
    "2 3 4 * +" → 14
    """
    stack = []
    
    for token in tokens:
        if token.lstrip('-').isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Integer division
    
    return stack[0] if stack else 0


def evaluate_expression(expression):
    """
    Full expression evaluator using Shunting Yard + Postfix evaluation
    """
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)


# ============================================================
# TEST CASES
# ============================================================

print("\n--- Testing Expression Evaluator ---")

test_cases = [
    ("2 + 3", 5),
    ("10 - 4", 6),
    ("3 * 4", 12),
    ("20 / 4", 5),
    ("2 + 3 * 4", 14),
    ("(2 + 3) * 4", 20),
    ("10 - 2 * 3", 4),
    ("100 / 10 / 2", 5),
    ("1 + 2 * 3 + 4", 11),
    ("(1 + 2) * (3 + 4)", 21),
]

print("\nUsing Shunting Yard Algorithm:")
for expr, expected in test_cases:
    result = evaluate_expression(expr)
    status = "✅" if result == expected else "❌"
    print(f"  {status} '{expr}' = {result} (expected {expected})")


# ============================================================
# INTERACTIVE CALCULATOR
# ============================================================

def run_calculator():
    """Run interactive calculator"""
    print("\n" + "=" * 60)
    print("INTERACTIVE CALCULATOR")
    print("Enter expressions to evaluate (or 'quit' to exit)")
    print("Supports: +, -, *, /, parentheses")
    print("=" * 60)
    
    while True:
        try:
            expr = input("\n> ").strip()
            if expr.lower() in ('quit', 'exit', 'q'):
                print("Goodbye!")
                break
            if not expr:
                continue
            
            result = evaluate_expression(expr)
            print(f"= {result}")
        except Exception as e:
            print(f"Error: {e}")


# Uncomment to run interactive calculator:
# run_calculator()


# ============================================================
# CHALLENGE: Implement your own version
# ============================================================

print("""

=== YOUR CHALLENGE ===

Implement basic_calculate() and calculate() functions above.

Tips:
1. basic_calculate (no parentheses):
   - Use a stack for numbers
   - Process * and / immediately
   - Store + and - results on stack
   - Sum stack at end

2. calculate (with parentheses):
   - Use recursion: when you see '(', recursively evaluate
   - Or use the Shunting Yard approach shown above

Bonus challenges:
- Add support for exponentiation (^)
- Add support for unary minus (-5)
- Add support for functions like sqrt, sin, cos
""")

print("\n" + "=" * 60)
print("Complete the implementation and run the tests!")
print("=" * 60)
