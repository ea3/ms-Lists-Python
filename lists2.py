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

even2 = [2,4,6,8]
odd2 = [1,3,5,7,9]

numbers = [even2, odd2]
for numbers_set in numbers:
    print(numbers_set)

    for value in numbers_set:
        print(value)
print(numbers)






























