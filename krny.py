#1
from idlelib.macosx import setupApp


# registr  = {}
#
# def my_decorator(func):
#     registr[func.__name__] = 0
#     def wrapper(*args, **kwargs):
#         registr[func.__name__] += 1
#
#         print(f'Функция {func.__name__} вызвана {registr[func.__name__]} раз')
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @my_decorator
# def hello(name):
#     return f"Hello {name}!"
#
# hello('ann')
# hello('masha')
# hello('petya')
# hello('olua')
# print(registr)

#2
# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, b + a
#
# f = fib()
# for _ in range(10):
#     print(next(f))
# print(f)

#3

def partition(arr, s, e):
    p = s
    x = arr[e - 1]
    for i in range(s, e - 1):
        if arr[i] <= x:
            arr[i], arr[p] = arr[p], arr[i]
            p = p + 1
    arr[p], arr[e - 1] = arr[e - 1], arr[p]
    return p

def quick_sort(arr, s, e):
    if e - s > 1:
        p = partition(arr, s, e)
        quick_sort(arr, s, p)
        quick_sort(arr, p + 1, e)


my_array = [29, 10, 14, 37, 13, 25, 1, 8]

print("Исходный массив:", my_array)

quick_sort(my_array, 0, len(my_array))

print("Отсортированный массив:", my_array)

