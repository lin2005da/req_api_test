#-*-coding:utf-8-*-
# @time     :2019/8/1/001 11:07
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :study_field.py
# @Sofeware :PyCharm Community Edition
# def foo():
#     print("starting...")
#     while True:
#         res= yield 4
#         # ='rwetrywe'
#
#         print("res:",res)
# g = foo()
# print(next(g)) #以while开始，field结束
# print("*"*20)
# print(next(g))#以field开始，res没有返回值，返回none，下一个field结束


# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:",res)
# g = foo()
# print(next(g))#以while开始，field结束
# print("*"*20)
# print(g.send(7))#以field开始，先赋值给res，下一个field结束
