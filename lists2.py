list_1 = []
list_2 = list()

print(f"List_1: {list_1}")
print(f"List_2: {list_2}")

if list_1 == list_2:
    print(" The Lists are equal!")

print(list("The lists are equal"))


even = [2,4,6,8]
another_even = even
print(another_even is even)
another_even.sort(reverse=True)
print(even)

