# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Safely divide two numbers, handling errors for invalid inputs and division by zero."""
    try:
        # Try converting inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Try performing the division
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
