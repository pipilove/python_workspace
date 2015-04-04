# coding=gbk
'''
Created on 2014年2月20日

@author: pipi
 '''
# a = {1:23,8:43,3:34,9:28}
# print(a)
# b = zip(a.keys(),a.values())   #拉成Tuple对组成的List

x = [1,23,45]
print(x)
y = [8,43,74]
print(y)
z = [3,34,39]
print(z)
b = list(zip(x,y,z))
print(b)

#采用operator模块的itemgetter函数
sorted(b,key = lambda item:item[1])
print(b)

#采用operator模块的itemgetter函数
#from operator import itemgetter
#sorted(b, key=itemgetter(1))
