name1 = input("Geben Sie den ersten Namen ein: ")
name2 = input("Geben Sie den zweiten Namen ein: ")
name3 = input("Geben Sie den dritten Namen ein: ")

if name1 < name2 and name1 < name3:
    smallest_name = name1
    if name2 < name3:
        middle_name = name2
        largest_name = name3
    else:
        middle_name = name3
        largest_name = name2
elif name2 < name1 and name2 < name3:
    smallest_name = name2
    if name1 < name3:
        middle_name = name1
        largest_name = name3
    else:
        middle_name = name3
        largest_name = name1
else:
    smallest_name = name3
    if name1 < name2:
        middle_name = name1
        largest_name = name2
    else:
        middle_name = name2
        largest_name = name1

print("Die Namen in aufsteigender alphabetischer Reihenfolge sind:")
print(smallest_name)
print(middle_name)
print(largest_name)
