number = int(input('Insert an integer to decide whether it is even or odd: '))


def determine(even_odd_number):
    if even_odd_number % 2 == 0:
        return True
    else:
        return False


print(determine(number))
