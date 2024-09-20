
''' --> Sem recursividade '''
# def fatorial(n):
#     fat = 1
#     for i in range(n):
#         fat *= (n - i)
#     return fat
#
# print(fatorial(5))

''' --> Com recursividade '''
# def fatorial(n):
#     if (n < 2):
#         return 1
#
#     return n * fatorial(n - 1)
#
# print(fatorial(1000))



''' --> Sem recursividade '''
# def fibonacci(n):
#     a = 0
#     b = 1
#
#     if (n == 1):
#         return 0
#     if (n == 2):
#         return 1
#
#     while (n > 2):
#         a, b = b, a + b
#         n -= 1
#
#     return b
#
# print(fibonacci(7))

def fibonacci(n):
    if (n == 1):
        return 0
    if (n == 2):
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))