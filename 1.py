# dirty_list = ['abc', '',['123', '', 0], {'': '123', 'a': '123'}, {}]
#
# def remove_empty(data):
#     if isinstance(data, list):
#         return [remove_empty(x) for x in data if remove_empty(x) or x == 0]
#     elif isinstance(data, dict):
#         return {k: remove_empty(v) for k, v in data.items() if remove_empty(v) or v == 0}
#     elif isinstance(data, set):
#         return {remove_empty(x) for x in data if remove_empty(x) or x == 0}
#     elif isinstance(data, tuple):
#         return [remove_empty(x) for x in data if remove_empty(x) or x == 0]
#     return data
#
# clean_list = [x for x in (remove_empty(i) for i in dirty_list) if x]
# print(clean_list)
# import datetime as d
#
# def simple_decore(fn):
#     def wrapper(*args, **kwargs):
#         n = d.datetime.now()
#         fn()
#         print("After call")
#     return wrapper
#
# @simple_decore
# def first_decor(a):
#     print("Tect function 1", a)
#
# @simple_decore
# def second():
#     print("second function")
from curses.textpad import rectangle


# class Rectangle:
#     default_color = 'green'
#
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     def __str__(self):
#         return f'Rectangle with {self.__width} and height {self.__height} and area {self.area()}'
#
#     def area(self):
#         return self.__width * self.__height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @property
#     def height(self):
#         return self.__height
#
#     @width.setter
#     def width(self, w):
#         if w <= 0:
#             raise Warning("value must be positive!")
#         self.__width = w
#
#     @height.setter
#     def height(self, h):
#         if h <= 0:
#             raise Warning("value must be positive!")
#         self.__height = h
#
#
# rectangle = Rectangle(10, 20)
# print(rectangle.area())
# print(rectangle.width)
# rectangle.width = 20
# print(rectangle.area())

class MyVector:

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__x

    def __str__(self):
        return f""

v1 = MyVector(1, 1, 1)
v2 = MyVector(3, 3, 3)

v_result = v1.dif(v2)
print(v_result.dif(v2))

