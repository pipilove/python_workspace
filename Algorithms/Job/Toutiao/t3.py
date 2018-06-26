#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '形式化算式'
'
http://discuss.acmcoder.com/topic/58f60f8fa846074f746580d7
今日头条2017校园招聘 技术综合
形式化算式
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
我们有如下形式化的数字，分别表示 1 2 3 4 5 6 7 8 9 0
*    ***   ***   * *   ***   ***   ***   ***   ***   ***
*      *     *   * *   *     *       *   * *   * *   * *
*    ***   ***   ***   ***   ***     *   ***   ***   * *
*    *       *     *     *   * *     *   * *     *   * *
*    ***   ***     *   ***   ***     *   ***   ***   ***

有如下形式化的符号，分别表示 + - * ／ = 小数点
 *        * *    *   ****
***  ***   *    *
 *        * *  *     ****   **
							**
现在将输入一个算式，你要将该算式计算之后按照上述形式化的方式输出
各个数字和符号之间空两格，无法整除则保留两位小数
'
__author__ = 'pipi'
__mtime__ = '4/18/17'
__email__ = 'pipijob@126.com'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓    ┏┓
            ┏━┛┻━━━━┛┻━┓
            ┃     ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃     ┻    ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗━┓┓┏━━┳┓┏━┛
                ┃┫┫  ┃┫┫
                ┗┻┛  ┗┻┛
"""
from __future__ import division


def format_print():
    d = {'1': ('*' * 5),
         '2': ('***', '  *', '***', '*  ', '***'),
         '3': ('***', '  *', '***', '  *', '***'),
         '4': ('* *', '* *', '***', '  *', '  *'),
         '5': ('***', '*  ', '***', '  *', '***'),
         '6': ('***', '*  ', '***', '* *', '***',),
         '7': ('***', '  *', '  *', '  *', '  *',),
         '8': ('***', '* *', '***', '* *', '***',),
         '9': ('***', '* *', '***', '  *', '***',),
         '0': ('***', '* *', '* *', '* *', '***',),
         u'+': ('     ', '  *  ', ' *** ', '  *  ', '     ',),
         u'-': ('     ', '     ', ' *** ', '     ', '     ',),
         u'*': ('     ', ' * * ', '  *  ', ' * * ', '     ',),
         u'/': ('     ', '   * ', '  *  ', ' *   ', '     ',),
         u'.': ('    ', '    ', '    ', ' ** ', ' ** ',),
         u'=': ('      ', ' **** ', '      ', ' **** ', '      ',)}
    a = raw_input()
    answer = eval(a)
    answer = round(answer, 2) if answer - int(answer) != 0 else answer
    # print answer

    a = a.split()
    xs = [d[i] for i in a[0]]  # alm.add(x%10); x=x/10;
    ys = [d[i] for i in a[2]]
    answers = [d[i] for i in str(answer)]

    for line in range(5):
        for x in xs:
            print x[line],
        print d[a[1]][line],  # prefers[1]为operator
        for y in ys:
            print y[line],
        print d['='][line],
        for s in answers:
            print s[line],
        print
        # for line in zip(*xs, d[prefers[1]], *ys, d['='], *answers):
        #     print ''.join(line)


def test():
    import sys, io

    sys.stdin = io.StringIO(u'''10 + 31''')
    format_print()
    print
    sys.stdin = io.StringIO(u'''31 - 19''')
    format_print()
    print
    sys.stdin = io.StringIO(u'''31 * 2''')
    format_print()
    print
    sys.stdin = io.StringIO(u'''31 / 3''')
    format_print()
    print


test()
