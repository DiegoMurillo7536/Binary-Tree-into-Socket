import random


def insert_numbers_in_list() -> list:
    count = 0
    numbers = []
    while count < 10:
        
        number = int(input(f"Ingresa el número {count + 1}: "))
        numbers.append(number)
        count +=1
    return numbers
