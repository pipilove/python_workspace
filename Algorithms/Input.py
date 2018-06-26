#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, io

# sys.stdin = io.StringIO('''4,6
sys.stdin = io.StringIO(u'''4
1 2 3 4
''')

import re, sys

a = []
ai = sys.stdin.readline().strip()
while ai:
    a.append([int(i) for i in re.split('\s|,', ai)])
    ai = sys.stdin.readline().strip()
print(a)

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
    a = [int(i) for i in ai.split(':')]
    print(a)
