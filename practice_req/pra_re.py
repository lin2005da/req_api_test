#-*-coding:utf-8-*-
# @time     :2019/7/16/016 15:50
# @Author   :python13_marimo
# @Email    :2670622242@qq.com
# @File     :pra_re.py
# @Sofeware :PyCharm Community Edition
import re
# 使用search  从任意位置匹配
# admin_user='15823652145'
# admin_pwd='123456'
# s='{"mobilephone":"${admin_user}","pwd":"${admin_pwd"}}'
# q='\$\{admin_user}'
# w=re.search(q,s)
# print(w)
# p='\$\{(.*?)}'
#
# m=re.search(p,s)
# print(m)

# 使用match  从头匹配
admin_user='15823652145'
admin_pwd='123456'
s='{"mobilephone":"${admin_user}","pwd":"${admin_pwd"}}'
p='\$\{(.*?)}'
# r = re.match("(?P<n1>p)(?P<n2>\w+)", s)
r=re.search(p,s)
x=r.group()

print(r)
print(x)
y=r.group(1)
print(1)
# s=re.sub(p,'123456',s,count=1)
print(s)

l=re.findall(p,s)
print(l)
s=re.sub(p,'123456',s,count=1)
# print(s)