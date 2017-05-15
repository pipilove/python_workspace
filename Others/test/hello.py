# firsr_p.py
import os
import re

origin_strs = [
    '#/home/yancai/Desktop/atomic/LLVM/llvm-3.6.2/build//bin/clang -g  -DUNDEF_THREADS_HACK -c -o chared_err.o chared.c',
    '#/home/yancai/Desktop/atomic/LLVM/llvm-3.6.2/build//bin/clang -g  -DUNDEF_THREADS_HACK -c -o aa chared_err.o chared.c',
    '/home/yancai/Desktop/atomic/LLVM/llvm-3.6.2/build//bin/clang++  -g  -DHAVE_CONFIG_H -D_REENTRANT -D_PTHREADS -DENGINE -DSTORAGE_ENGINE -DNAMESPACE=Nfs -I. -I. -I../../include -I../../include -I../../include -I../../regex -I../../sql -I. -I./TransformLib -O3 -fno-implicit-templates -fno-exceptions -fno-rtti -fimplicit-templates -Wno-invalid-offsetof -fexceptions -MT libhafalcon_a-SQLParse.o -MD -MP -MF .deps/libhafalcon_a-SQLParse.Tpo -c -o libhafalcon_a-SQLParse.o SQLParse.cpp']
dir = 'path'
for origin_str in origin_strs:
    if not re.search('(-o\s+)(\w+\s+)(.*?\.o)', origin_str):
        new_str = re.sub('-c', '-emit-llvm -c', origin_str)
        new_str = re.sub('(-o\s+)(.*?\.o)', r'\1' + os.path.join(dir, r'\2') + '.bc', new_str)
        print(new_str)
