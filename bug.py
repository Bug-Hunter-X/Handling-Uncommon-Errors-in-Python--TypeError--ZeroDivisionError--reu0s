def function_with_uncommon_error(a, b):
    try:
        result = a / b
    except TypeError:
        print("TypeError: unsupported operand type(s) for /: 'str' and 'int'")
        return None
    except ZeroDivisionError:
        print("ZeroDivisionError: division by zero")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: ZeroDivisionError: division by zero
print(function_with_uncommon_error(10, "hello")) # Output: TypeError: unsupported operand type(s) for /: 'int' and 'str'
print(function_with_uncommon_error(10, [1,2])) # Output: TypeError: unsupported operand type(s) for /: 'int' and 'list'