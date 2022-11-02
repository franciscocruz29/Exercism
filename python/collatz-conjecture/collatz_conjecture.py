def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    if number == 1:
        return 0
    
    if number % 2 == 0:
        number = number /2
    else:
        number = 3 * number +1
    
    return 1 + steps(number)
