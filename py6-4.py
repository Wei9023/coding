class Fib(object):
    def __init__(self, num):
        def f(n, L):
            if n < 2:
                return n;
            else:
                return L[n-1] + L[n-2]

        #f(1,2) = 1;
        #a = f(1,2);

        L = []
        for n in range(num):
            L.append(f(n, L))
        self.numbers = L

    def __str__(self):
        return str(self.numbers)
    __repr__ = __str__
    def __len__(self):
        return len(self.numbers)


f = Fib(10)
print f
print len(f)



# class Fib(object):
#
#     def __init__(self, num):
#         f = []
#         for n in range(num):
#             def cal(n):
#                 if n <= 1:
#                     return n;
#                 else:
#                     return f[n-1] + f[n-2]
#             f.append(cal(n))
#         self.numbers = f
#         print(f)
#     def __str__(self):
#         return str(self.numbers)
#
#     __repr__ = __str__
#
#     def __len__(self):
#         return len(self.numbers)
#
# f = Fib(10)
# print f
#
