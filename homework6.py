my_dict = {'Sasha': 1997, 'Petr': 2003, 'Andrey': 2001}
print(my_dict)
print(my_dict['Petr'])
print(my_dict.get('Denis'))
my_dict.update({'Vasya': 1999, 'Lev': 2001})
del my_dict['Petr']
print(my_dict)
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(my_set)
my_set.update({'String', True})
my_set.discard(3)
print(my_set)

