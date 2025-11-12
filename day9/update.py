# uid=[101,102,103]
# eid=[104,105,106,107]
# uid.update(eids)
# print(eids)
data=[1,2,3,4]
# dat=[6,7,8]
# data=dat.copy()
# print(data)

dat=data.copy()
print(dat)
print(dat.index(3))


# dt=[1,2,3,4,5]
# i=0;
# while i<=len(dt)-1:
#     if dt[i]==3:
#         continue;
#     print(dt[i])
#     i=i+1

dt = [1, 2, 3, 4, 5]
i = 0
while i <= len(dt) - 1:
    if dt[i] == 3:
        i = i + 1
        continue
    print(dt[i])
    i = i + 1
