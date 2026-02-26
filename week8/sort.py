data = [(1, 3), (4, 1), (2, 5), (3, 2)]
sorted_data = sorted(data, key=lambda x: x[-1])

print("Sorted list of tuples:", sorted_data)