immutable_var = 1, 2, 3, 4, True, "string"
print(immutable_var)
# immutable_var[0] = 5 #Нельзя именить потому что кортеж предназначен для хранения какого-нибудь списка а не для редактирования
# print(immutable_var)

mutable_list = ([1, 2, 3])
mutable_list[0] = 6
print(mutable_list)