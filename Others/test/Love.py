#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '6/20/2015-020'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


class i():
    def __init__(self):
        pass

    def meet_you(self, year):
        print("I %s @%s\n%s" % (self.meet_you.__name__, year, '*' * 20))

    def be_with_you(self, u):
        try:
            while (1):
                if u.status == "hungry":
                    print("line.feed(u)")
                    i.feed(u)
                    break
                elif u.status == "tired":
                    print("line.hug(u)")
                    i.hug(u)
                    break
                else:
                    i.say(u, "I love you!")
                    break
        except():
            exit(-1)
            # Until reboot


    def leave_you(self, year):
        print("%s\nI %s @%s\n" % ('*' * 20, self.leave_you.__name__, year), '*' * 20)

    def miss_you(self, year):
        print("I %s @%s\n" % (self.miss_you.__name__, year), '*' * 20)

    def feed(self, u):
        u.change_status("full")

    def hug(self, u):
        u.change_status("relaxed")

    def say(self, u, words):
        print("I say ", words)
        u.change_status("happy")


class u():
    def change_status(self, status):
        self.status = status


i = i()
u = u()
years = list(range(2011, 2016))
i.meet_you(years[0])
for status in ["hungry", "tired", None]:
    u.status = status
    print("when you are", u.status)
    i.be_with_you(u)
    print("so you are ", u.status)
i.leave_you(years[3])
i.miss_you(years[4])

