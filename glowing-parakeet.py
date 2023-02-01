def square(num):
    return num ** 2


numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, numbers))

print('The squared numbers are: ', squared_numbers)
