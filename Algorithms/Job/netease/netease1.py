#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, io

sys.stdin = io.StringIO(u'''2
19:90:23
23:59:59
''')

import sys

its = int(sys.stdin.readline().strip())
for _ in range(its):
    ai = sys.stdin.readline().strip()
    h, m, s = ai.split(':')
    # validation
    if int(h) > 23:
        h = '0' + str(h)[1]
    if int(m) > 59:
        m = '0' + str(m)[1]
    if int(s) > 59:
        s = '0' + str(s)[1]
    print("{}:{}:{}".format(h, m, s))
