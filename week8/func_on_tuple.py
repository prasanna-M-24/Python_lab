from functools import reduce
tup = (1,2,3,4,5)
tup_map = map(lambda x:x*x,tup)
print(list(tup_map))

tup_fltr = filter(lambda x:x % 2 == 0, tup)
print(list(tup_fltr))

tup_reduce = reduce(lambda x, y: x + y, tup)
print("Sum of elements: ",tup_reduce)
