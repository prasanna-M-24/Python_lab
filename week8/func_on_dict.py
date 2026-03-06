from functools import reduce

dct = {"pen":20, "pencil":10, "eraser":5, "sharpner":7,"scale":12}

dct1 = dict(map(lambda item: (item[0], item[1] + 4), dct.items()))
print("Values after adding 4:",dct1)

dct2 = dict(filter(lambda item: item[1] > 5, dct.items()))
print("Values greater than 5:", dct2)

dct3 = reduce(lambda x, y: x + y, dct.values())
print("Sum of values of dictionay:", dct3)

