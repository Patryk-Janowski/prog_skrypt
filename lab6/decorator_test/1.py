from inspect import signature

# def dec(msg):
#     def logger():
#         print(msg)
#     return logger

# x = dec('a')
# y = dec('b')

# def aaa(*args, **kwargs):
#     print(type(args))
#     print(type(kwargs))
#     print(args)
#     print(kwargs)
# quit
# aaa(1, 2, 3, a=1, v=2)
    
# def sum(a, b):
#     return a+b


# print(len(signature(sum).parameters))

# def a(*args):
#     print(args)
#     print(*args)

# def b(**kwargs):
#     print(kwargs)
#     # print(**kwargs)

# a(1,2,3,4,5)
# b(a=1,b=2,c=3,d=4)

    
l = [x for x in range(100)] 

f = filter(lambda x: x % 5 == 0, l)
print(help(f))