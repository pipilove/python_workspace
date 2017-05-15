#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'color settings'
__author__ = 'pi'
__mtime__ = '12/30/2014-030'
# code is far away from bugs with the god animal protecting
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
"""
将此文件放入python3.4.2\Lib文件夹中
To use code like this, you can do something like:
from Colors import *
print(REDH,"it's red highlight",'\n', RED,"it's red")
print(GREENH,"it's green highlight\n", GREEN,"it's green")
print(WHITEH,"it's white highlight"*5,'\n', WHITE,"it's white"*5)
调用输出字体颜色
随时通过修改project>external lib>python3.4.2>lib>colors增删颜色值

color设置格式说明：

color = \033[code;前景色;背景色m

code:
0 off
1 高亮显示
4 underline
5 闪烁
7 反白显示
8 不可见

前景  背景  颜色
30      40  黑色
31      41  红色
32      42  绿色
33      43  黄色
34      44  蓝色
35      45  紫红色
36      46  青蓝色
37      47  白色
1       1   透明色
"""

"""
#METHOD 2
class fcolors:
    RED = '\033[91m'       #RED
    DEFAULT = '\033[0m'
    #...
    def disable(self):
        self.RED = ''
        self.DEFAULT = ''
        #...
print(fcolors.RED + "Warning: ... Continue?")
print(fcolors.DEFAULT)
"""

#font style
DEFAULT = '\033[0m' # DEFAULT = '\033[0;0m'
BOLD = '033[1m'
DISABLE = '\033[02m'
UNDERLINE = '\033[04m'
REVERSE = '\033[07m'
STRIKETHROUGH = '\033[09m'
INVISIBLE = '\033[08m'

#light color
DARKGREY = '\033[90m'
REDL = '\033[91m'    #<=> '\033[91;1m' <=> '\033[1;91;1m'  lightred
GREENL = '\033[0;92;1m'
YELLOWL = '\033[0;93;1m'
BLUEL = '\033[0;94;1m'
PINKL = '\033[0;95;1m'
WHITEL = '\033[0;97m'    #?

#highlight light color
REDHL = '\033[1;91m'
GREENHL = '\033[1;92;1m'
YELLOWHL = '\033[1;93;1m'
BLUEHL = '\033[1;94;1m'
PINKHL = '\033[1;95;1m'
WHITEHL = '\033[1;97m'

# highlight color
REDH = '\033[1;31m' #REDH = '\033[1;31;1m'
GREENH = '\033[1;32;1m'
YELLOWH = '\033[1;33;1m'
BLUEH = '\033[1;34;1m'
PURPLEH = '\033[1;35;1m'
WHITEH = '\033[1;37m'

# color
BLACK ='\033[30m'
RED = '\033[0;31;1m'
GREEN = '\033[0;32;1m'
ORANGE = '\033[0;33;1m'
BLUE = '\033[0;34;1m'
PURPLE = '\033[0;35;1m'
CYAN = '\033[36m'
WHITE = '\033[0;37m'
LIGHTGREY = '\033[37m'
