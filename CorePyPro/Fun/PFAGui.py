#!/usr/bin/env python
# coding=gbk
"""
__title__ = '����gui ģ����, ƫ����Ӧ��GUI'
__author__ = 'pi'
__mtime__ = '2014.12.13'
"""
import tkinter
from functools import partial

root = tkinter.Tk()

"""lambda ʵ��"""
mybutton = lambda **x: tkinter.Button(root, bg='green', fg='red', **x)
# print(type(mybutton))   #<type 'function'>
b1 = mybutton(text='button1')
b1.pack()

"""partial ʵ��"""
MyButton = partial(tkinter.Button, root, bg='green', fg='red')
# print(type(mybutton))   #<type 'functools.partial'>
b2 = MyButton(text='button2 of partial')
b2.pack()
qb = MyButton(text='QUIT', bg='red', command=root.quit)
qb.pack(fill=tkinter.X, expand=True)
qb.pack()

root.title('PFAs!')
root.mainloop()
