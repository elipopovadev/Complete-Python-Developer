class ValueCannotbeNegativeOrZeroError(Exception):
    pass

def validate_numbers(numbers):
    for num in numbers:
        if num <= 0:
            raise ValueCannotbeNegativeOrZeroError("Please, enter only positive numbers!")
        
numbers = [1, 2, 3, 4, 0]

validate_numbers(numbers)
