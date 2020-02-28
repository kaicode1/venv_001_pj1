from functools import reduce

fruits = ['apple', 'orange', 'banana']

print(reduce(lambda x, y: x + y, fruits))


def plus(x, y):
    return x + y


print(reduce(plus, fruits))
