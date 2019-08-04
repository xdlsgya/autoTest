#!/usr/bin/env python
#  -*- coding:UTF-8 -*-


import os
import time
import sys
import tarfile
import glob
import shutil

file=[]
if len(sys.argv)==1:
        print 'Usage:python backup.py tar_packeges'
        sys.exit()

for tar_file in sys.argv:
        if tar_file==sys.argv[0]:
                continue
        else:
                #print tar_file
                file.append(tar_file)

HOME_dir=os.getenv('HOME')
source=[]
code_dir=HOME_dir+os.sep+'deploy/code'
#print code_dir
for j in file:
        code_file=code_dir+os.sep+j
        tar=tarfile.open(code_file,'r')
        for tarinfo in tar:
                if tarinfo.isfile():
                        #print tarinfo.name
                        source.append(tarinfo.name)
        tar.close()

#print source

source_bak=[]
re_1=HOME_dir+os.sep+'bin'
re_2=HOME_dir+os.sep+'lib'
for k in source:
        all_path=HOME_dir+os.sep+k
        if all_path.find(re_1)==-1 and all_path.find(re_2)==-1:
                re_path=HOME_dir+os.sep+k
        else:
                reg=k.split('.')
                re_path=HOME_dir+os.sep+reg[0]+'*'
        s=glob.glob(re_path)
        for y in s:
                if os.path.islink(y) or (y.find(re_1)==-1 and y.find(re_2)==-1):
                        source_bak.append(y)

#print source_bak


bak_path=HOME_dir+os.sep+'backup_ex'
target='backup_'+time.strftime('%Y%m%d%H%M')+'.tar'
os.chdir(HOME_dir)
tar=tarfile.open(target,'w')
for z in source_bak:
        path_list=z.split('/')[3:]
        tar_path='/'.join(path_list)
        tar.add(tar_path)
tar.close()

if not os.path.exists(bak_path):
        os.mkdir(bak_path)
        print 'create directory %s success' % bak_path
shutil.move(target,bak_path)
backup_file=bak_path+os.sep+target
print 'backup success,the backup file is %s' % backup_file