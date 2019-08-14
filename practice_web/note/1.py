
#-*-coding:utf-8-*-
# @time     :2019/7/28/028 9:41
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :1.py
# @Sofeware :PyCharm Community Edition
# def singleton0(cls):
#     instances = {}
#
#     def getinstance(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return getinstance
#
#
# @singleton0
# class MyClass:
#     a = 1
#
#
# c1 = MyClass()
# c2 = MyClass()
# print(c1 == c2)  # True
# class Singleton(object):
#     def __new__(cls):
#         # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance
#
#
# obj1 = Singleton()
# obj2 = Singleton()
#
# obj1.attr1 = 'value1'
# print(obj1.attr1, obj2.attr1)
# print(obj1 is obj2)

