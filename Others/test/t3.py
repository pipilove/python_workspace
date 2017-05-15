origin_strs = [
    '#/home/yancai/Desktop/atomic/LLVM/llvm-3.6.2/build//bin/clang -g  -DUNDEF_THREADS_HACK -c -o chared_err.o chared.c',
    '#/home/yancai/Desktop/atomic/LLVM/llvm-3.6.2/build//bin/clang -g  -DUNDEF_THREADS_HACK -c -o aa chared_err.o chared.c',
    '/home/yancai/Desktop/atomic/LLVM/llvm-3.6.2/build//bin/clang++  -g  -DHAVE_CONFIG_H -D_REENTRANT -D_PTHREADS -DENGINE -DSTORAGE_ENGINE -DNAMESPACE=Nfs -I. -I. -I../../include -I../../include -I../../include -I../../regex -I../../sql -I. -I./TransformLib -O3 -fno-implicit-templates -fno-exceptions -fno-rtti -fimplicit-templates -Wno-invalid-offsetof -fexceptions -MT libhafalcon_a-SQLParse.o -MD -MP -MF .deps/libhafalcon_a-SQLParse.Tpo -c -o libhafalcon_a-SQLParse.o SQLParse.cpp']


def argparse_test(s):
    import argparse, re, os, traceback
    dir = 'path'

    parser = argparse.ArgumentParser(description='Process clang args')
    parser.error = lambda errmsg: exec('raise(Exception(errmsg))')

    parameters = ['-g', '-I', '-c', '-o']
    parser.add_argument(parameters[0], dest=parameters[0], action='store', required=True, nargs='+')
    parser.add_argument(parameters[1], dest=parameters[1], action='store_true', required=True)
    parser.add_argument(parameters[2], dest=parameters[2], action='store_true', required=True)
    parser.add_argument(parameters[3], dest=parameters[3], nargs=2)

    try:
        args = vars(parser.parse_args(s.split()[1:]))
    except Exception as  e:
        # print('{} has invalid args!!!\n{}\n'.format(s, traceback.format_exc()))
        print('{} has invalid args!!!\n{}\n'.format(s, e))
        return
    new_str = s.split()[0]
    for p in parameters:
        if args.get(p):
            if type(args.get(p)) is list:
                args[p] = ' '.join(args.get(p))
            if p is '-c':
                args[p] = ' -emit-llvm -c'
            elif p is '-o':
                args[p] = ' -o ' + re.sub('(\w+\.o)', os.path.join(dir, r'\1') + '.bc', args[p])
            else:
                args[p] = ' '.join([p, args.get(p)]) if type(args.get(p)) is not bool else ' ' + p
            new_str += args.get(p)

    print("{} \n ====> \n {}\n".format(s, new_str))


for s in origin_strs:
    argparse_test(s)


def re_test():
    import os
    import re

    origin_str = '#/home/yancai/Desktop/atomic/LLVM/llvm-3.6.2/build//bin/clang -g  -DUNDEF_THREADS_HACK -c -o aa chared_err.o chared.c'
    dir = 'path'
    new_str = re.sub('-c', '-emit-llvm -c', origin_str)
    new_str = re.sub('(-o\s*)(.*?\s+)(.*?\.o)', r'\1' + os.path.join(dir, r'\3') + '.bc', new_str)
    print(new_str)

    # /home/yancai/Desktop/atomic/LLVM/llvm-3.6.2/build//bin/clang -g  -DUNDEF_THREADS_HACK -emit-llvm -c -o chared.o.bc chared.c
