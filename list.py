# mylist = [2,5,6,7,8,9]
# mylist.reverse()
# print(mylist)
# print(mylist[::2])
# print(mylist[::-1])

# mystr = "kiran"
# print(len(mystr))

# l1 = [1,2,3,4]
# l2 = [9,6,7,8]
# l1.extend(l2)
# print(l1)
# print(l2)

# mylist = iter(["kiran" ,"maurya","uddc"])
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# #print(next(mylist))

l1 = [1,12,3,4]
# l2 = l1.copy()
# print(id(l2))
# print(id(l1))
# print(l1.index(1)) # 0
# print(l1.pop()) #4
# l1.reverse()
# print(l1)
# l1.sort()
# print(l1)

l2 = l1
print(l2)
l2[1]=13
print(l1,l2)

l3 = l1.copy()
l3[1]=14
print(l1,l3)
print(l3)



