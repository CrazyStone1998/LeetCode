# if -1:
#     print(1151)
# a = set()
# b = set([1,2,3])
# print(b)
# a.add(b)

# from functools import cmp_to_key

# print(ord('0'))
# print(chr(42))
# def custom_key(x,y):
#     x = str(x)
#     y = str(y)
#     len_x = len(x)
#     len_y = len(y)
#     th = len_x if len_x > len_y else len_y
#
#     x = x+'00000000'
#     y = y+'00000000'
#
#     for i in range(th):
#
#         if int(x[0]) < int(y[0]):
#             return -1
#         elif int(x[0]) > int(y[0]):
#             return 1
#     return 0
# print(sorted([1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],key=cmp_to_key(custom_key)))

# a = -1
# b = 2
# print(bin(a))
# print(bin(b))
# print(bin(a^b))
# print(bin(a&b))

# i = a ^ b
# j = (a & b) << 1
# for k in range(10):
#     i, j = i ^ j, (i & j) << 1
#     print(i)
#     print(j)

# for i in range(1,10,5):
#     print(i)
#
# a= [1,2,3,]
# b = a
# b[0] = 5
# print(a)
#
# a = 5
# for i in range(a):
#     a -=1

# d[2] = []
# d[2].append([['pre'] + k for k in a])
# print(d[2])
#     temp = 6
# print(temp)
# a =[ 1,2,3]
# b = a[1:]
# b[0] = 2
# print(a)
# print(a+b)
# a.insert(1,'#')
# print(a)
#
# a.insert(3,'#')
# print(a)
# a = [1,3,2,3]
# print(a.index(max(a)))
# pre = [1,2,3]
# mid=[]
# mid = pre.copy()
# pre[0] = 5
# print(mid)
# import mathclass Solution:
#     def climbStairs(self, n: int) -> int:
# print(math.log10(15))
#
# num = [1,2,3] * 5
# def fn(n):
#     num = n * 5
#     print(num)
# print(num)
# fn(num)
# print(num)
# n = 1
# def fn():
#     n = 0
# fn()
# print(n)
# str = '123456'
# print()
# board = [[1, 2, 3], [1, 2, 3]]
# print(len(board))
# a = [1,2,3]
# b = [1]
# for i in zip(a,b):
#     print(i)
# a = '123'
# print(a[::-1])
