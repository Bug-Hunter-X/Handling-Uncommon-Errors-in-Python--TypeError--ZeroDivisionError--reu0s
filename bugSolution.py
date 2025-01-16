def function_with_uncommon_error(a, b):
    try:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
          if b == 0:
            raise ZeroDivisionError("Division by zero")
          result = a / b
        else:
          raise TypeError("Unsupported operand type(s) for / ")
    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: ZeroDivisionError: Division by zero
print(function_with_uncommon_error(10, "hello")) # Output: TypeError: Unsupported operand type(s) for / 
print(function_with_uncommon_error(10, [1,2])) # Output: TypeError: Unsupported operand type(s) for / 