lst = [2,12,15,18,19,25]
lst2 = [x for x in lst if x > 15]
print("Elements greater than 15:", lst2)

dct = {"pen": 10, "pencil": 5, "eraser": 6,"sharpner":7,"scale":11}
dct.update({k: v + 3 for k, v in dct.items()})
print("Dictionary after updating:", dct)
