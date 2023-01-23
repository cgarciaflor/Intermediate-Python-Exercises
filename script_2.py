def combined_dict(dict1, dict2):
    dict3 = {}
    for key in dict2:
        if key in dict1:
            dict2[key] = dict2[key] + dict1[key]
            dict3.update(dict2)
    print(dict3)

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict(my_dict_1,my_dict_2)