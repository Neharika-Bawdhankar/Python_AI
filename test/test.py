import copy

a = [1,2,3,[4,5,6],[1,2,3],7,8,9]
print(dir(a))
# b = a # memory reference. No copy is created
# b = a.copy # shallow copy. top level copy is created

b =  copy.deepcopy(a) # deep copy. all levels are copied

a[3][0] = 0
a[4][1] = 0
a[0] = 0

print(a)
print(b)

