# coding=gbk
'''
Created on 2014��2��20��

@author: pipi
 '''
# a = {1:23,8:43,3:34,9:28}
# print(a)
# b = zip(a.keys(),a.values())   #����Tuple����ɵ�List

x = [1,23,45]
print(x)
y = [8,43,74]
print(y)
z = [3,34,39]
print(z)
b = list(zip(x,y,z))
print(b)

#����operatorģ���itemgetter����
sorted(b,key = lambda item:item[1])
print(b)

#����operatorģ���itemgetter����
#from operator import itemgetter
#sorted(b, key=itemgetter(1))
