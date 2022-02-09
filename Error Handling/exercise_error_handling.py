while True:
    try:
        age = int(input("What is your age?"))
        10 / age
    except ValueError as error:
        raise error
    except ZeroDivisionError as error:
        raise error
    else: 
        print("Thank you")
    finally:
        print("I am finally done!") 
    print("Complete!")
        