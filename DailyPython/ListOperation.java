my_list = [10, 20, 30, 40]
print("Original List:", my_list)

print("First element:", my_list[0])
print("Last element:", my_list[-1])

my_list.append(50)
print("After append:", my_list)

my_list.insert(1, 15)
print("After insert:", my_list)

my_list.extend([60, 70])
print("After extend:", my_list)

my_list[2] = 25
print("After update:", my_list)

my_list.remove(40)
print("After remove:", my_list)

my_list.pop(3)
print("After pop:", my_list)

print("Sliced list:", my_list[1:4])

print("Length:", len(my_list))
print("Max:", max(my_list))
print("Min:", min(my_list))
print("Sum:", sum(my_list))

my_list.sort()
print("Sorted ascending:", my_list)

my_list.sort(reverse=True)
print("Sorted descending:", my_list)

my_list.reverse()
print("Reversed list:", my_list)

print("Is 25 present?", 25 in my_list)
if 25 in my_list:
    print("Index of 25:", my_list.index(25))

for i in my_list:
    print(i)

squares = [x*x for x in range(1, 6)]
print("Squares list:", squares)

my_list.clear()
print("After clear:", my_list)
