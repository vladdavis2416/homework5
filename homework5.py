immutable_var = 0, 1, "string", 2.5
print(immutable_var)

#immutable_var[0]=200
#print(immutable_var)
#кортежи не поддерживают замену элементов, но при этом элементы из кортежа можно найти по индексу, как и в списках. Если добавить список в кортеж, то его внутри кортежа можно будет изменить, но остальные элементы кортежа изменять не получится

mutable_list =[1, 2, "food", "apple", 4.2]
print(mutable_list)
mutable_list[0]= 200
mutable_list[2]="Britain"
mutable_list[4]=3.1
print(mutable_list)
