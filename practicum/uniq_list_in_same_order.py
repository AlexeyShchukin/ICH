my_list = [3, 5, 2, 3, 8, 5, 1]
unique_list = list(dict.fromkeys(my_list))
print(unique_list)  # Вывод: [3, 5, 2, 8, 1]