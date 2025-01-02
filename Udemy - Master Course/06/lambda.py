a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]

# x = filter(lambda x: x%5==0, a)
# print(list(x))

# for i in a:
#     if i %5==0:
#         print(i)
        
# z = [i for i in a if i%5==0]
# print(z)

# y = (i for i in a if i%5==0)
# print(next(y))


from functools import reduce
b = [1,2,3,4,5,6]

z = reduce(lambda x,y: x*y, b)
print(z)

