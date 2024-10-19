def find_largest(number):
    biggest_number = number[0]
    for number in number:
        if number> biggest_number:
            biggest_number = number
    return biggest_number