parrot_list = ["non pinin", "no more ", "a stiff", "bereft of life"]
parrot_list.append("A Norwegian Blue ")
for state in parrot_list:
    print("This parrot is " + state)


even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
sorted_numbers = sorted(numbers)
print(sorted_numbers)
if numbers == sorted_numbers:
    print("THe lists are equal")
else:
    print("THey are not equal")

