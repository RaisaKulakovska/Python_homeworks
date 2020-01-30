# with open ("list_hw.py", "w") as list_homework:
#     list_homework.write(

#-----------1v------------
list1 = [2,1,17,65,3,85,14,]
print(list1)
min_v = min(list1)
max_v = max(list1)
print(min_v)
print(max_v)
max_ind = list1.index(max_v)
print(max_ind)
min_ind = list1.index(min_v)
print(min_ind)
temp = list1[min_ind]
list1[min_v] = max_v
list1[max_ind] = temp
print(list1)

#-----------3v------------
list3 = list(range(1,11))
print(list3)

list_total = [
    list3[::2],
    list3[1::2]
]
list_new = []
i = 0
while i < len(list_total[0]):        
    list_new.append(list_total[1][i])
    list_new.append(list_total[0][i])
    i += 1
    
print(list_new)

# -----------4v------------
list4 = list(range(3,22))
list4_new = []
len4 = len(list4)
print(list4)
# print(len4)
index_last1 = int(len4/2)-1
# print(index_last1)
item_last1 = list4[index_last1]
# print(item_last1)
index_first2 = index_last1+1
item_first2 = list4[index_first2]
# print(item_first2)
index_last1_next = index_last1 +1
list4_1 = list4[:index_last1_next]
# print(list4_1)
list4_2 = list4[index_first2:]
# print(list4_1)
# print(list4_2)
list4_new.extend(list4_2)
list4_new.extend(list4_1)
print(list4_new)


# )

