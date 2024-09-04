def operAritmetic(val1, val2, operator):
    try:
        if operator == '+':
            return val1 + val2
        elif operator == '-':
            return val1 - val2
        elif operator == '*':
            return val1 * val2
        elif operator == '/':
            if val2 == 0:
                raise ValueError("Cannot divide by zero")
            return val1 / val2
        else:
            raise ValueError("Invalid operator")
    except Exception as e:
        print(f"Error: {e}")
        def calcIva(cifra):
            return cifra * 19/100