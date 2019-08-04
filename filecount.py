#encoding=utf-8
#!/usr/bin/python

import os
import sys

def listFileNum(curdir):
    lst_curdir = os.listdir(curdir)
    for line in lst_curdir:
        filepath = os.path.join(curdir, line)
        if os.path.isdir(filepath):
            os.chdir(filepath)
            print '{0:<60}'.format(filepath),len([file for file in os.listdir(filepath) if os.path.isfile(file)])
        else:
            pass

if __name__ == '__main__':
    curdir = os.getcwd()
    listFileNum(curdir)



