datasci = {"R","Tableau","SAS","Python","SQL","Git"}
dataeng = {"Java","Scala","Hadoop","Python","SQL","Git"}

# #print(datasci.union(dataeng))
# print(datasci.intersection(dataeng))
# # print(datasci.difference(dataeng))
# # print(dataeng.difference(datasci))
# print(datasci.symmetric_difference(dataeng))

# new_set = {"Java","Scala","Hadoop","Python","SQL","Git","Python","SQL","Git"}
# print(new_set)


a = {1,2,3,4,5}
a.add(6)
print(a)
b = frozenset(a)
b.add(7)
print(b)


# print(list(set(a)))
# b =set(a)
# c =list(set(a))

# print(type(a))
# print(type(b))
# print(type(c))
