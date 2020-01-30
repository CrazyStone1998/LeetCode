# 字符串反转
s = 'asdfs'
s = s[::-1]
# range 倒序
for i in range(10,-1,-1):
    print(i)
# sum 参数是一个一维数组，多维不行
s = [[1, 2, 3], [4, 5, 6]]
s = sum([sum(i) for i in s])
