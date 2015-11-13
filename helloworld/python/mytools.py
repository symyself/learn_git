#!/bin/env python2.7
#! -*- coding: UTF-8 -*-
def name():
    print 'songy'
    print 'symyself@163.com'

def exec_str(info,cmd):
    print "%30s:%10s = %s" %(info,cmd,str(eval(cmd)))
def convert_func():
    print '常用的内置函数'
    exec_str('int[0,256) to char','chr(48)')
    exec_str('char to int','ord("0")')
    
if __name__ == "__main__":
    convert_func()
