#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, io

# sys.stdin = io.StringIO('''4,6
sys.stdin = io.StringIO(u'''4,6
8 9 6 5
9,7
8,5
8,4
9,3
7,3
7,2
''')

import re, sys

a = []
ai = sys.stdin.readline().strip()
while ai:
    a.append([int(i) for i in re.split('\s|,', ai)])
    ai = sys.stdin.readline().strip()
print(a)
