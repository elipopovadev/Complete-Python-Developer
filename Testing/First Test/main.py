def sum(num):
    try:
       return int(num) + 5
    except (ValueError, TypeError) as error:
        return ("Please, enter a number!")
 