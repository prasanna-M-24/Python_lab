student = {
    "name": "Koushik",
    "age": 18,
    "course": "CSE",
    "year": 2
}

print("Keys:", student.keys())

print("Values:", student.values())

print("Items:", student.items())

removed_value = student.pop("year")
print("After pop():", student)
print("Popped value:", removed_value)

del student["age"]
print("After delete():", student)