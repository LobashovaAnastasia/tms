list_1 = [1, 2, 3]
list_2 = [1, 2, 3, 4, 5]
new_list = [i * j for i in list_1 for j in list_2]
new_list_2 = [(i, j) for i in list_1 for j in list_2]
print(new_list)
print(new_list_2)
