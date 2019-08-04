#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import sys
from datetime import datetime
import random
import math
import shutil
import tarfile
from ftplib import FTP


# python get_decodebak_file.py 20190703		取 20190703 目录下的话单，否则默认取当天

if len(sys.argv) == 2:
	getdate = sys.argv[1]
else:
	getdate = datetime.now().strftime('%Y%m%d')
# 取话单路径及话单存放路径
decodeDir = '/data1/work/decode/bak'
targetDir = '/data1/work/maintain/duanhg/regression/decode_'+getdate

if not os.path.exists(targetDir):
	os.makedirs(targetDir)
else:
	shutil.rmtree(targetDir)
	os.mkdir(targetDir)
	print "mkdir result dir %s" %targetDir

tarFileDir = targetDir.split('/')[-1]
tarFileName = 'decode_'+getdate+'.tar.gz'
# ftp 传输文件
ftpDistIp = "10.70.139.15"
ftpDistDir = '/data1/work/maintain/duanhg/regression'
userName = 'billing'
passWd = 'Bill@Oo0'

def ftpTarFile(ftpDistIp, ftpDistDir, userName, passWd, tarFileName):
	print "ftp to %s ---------> %s" %(ftpDistIp, ftpDistDir)
	ftp = FTP()
	ftp.connect(ftpDistIp, 21)
	ftp.login(userName, passWd)
	bufsize = 10240
	fp = open(tarFileName, 'rb')
	destFileName = ftpDistDir + '/' + tarFileName
	ftp.storbinary('STOR '+ destFileName, fp, bufsize)
	fp.close()
	ftp.quit()

def get_file_count(dir):
    file_list = list()
    for root, dirs, files in os.walk(dir):
        for f in files:
            file_list.append(f)
    return file_list

# <=50			100%
# 50-200			%30
# 200-1000			%10
# 1000-5000			%5
# >5000 			%2
def randomList(filelist):
	if len(filelist) > 50 and len(filelist) <=200:
		filenums = int(math.ceil(len(filelist)*0.3))
		filelist = random.sample(filelist, filenums)
	elif len(filelist) > 200 and len(filelist) <=1000:
		filenums = int(math.ceil(len(filelist)*0.1))
		filelist = random.sample(filelist, filenums)
	elif len(filelist) > 1000 and len(filelist) <=5000:
		filenums = int(math.ceil(len(filelist)*0.05))
		filelist = random.sample(filelist, filenums)	
	elif len(filelist) > 5000:
		filenums = int(math.ceil(len(filelist)*0.02))
		filelist = random.sample(filelist, filenums)	
	else:
		pass
	return filelist

def getDirs(decodeDir):
	print "start copy files from %s" %decodeDir
	for dirs in os.listdir(decodeDir):
		filedir = os.path.join(decodeDir,dirs)+"/"+getdate
		if os.path.exists(filedir):
			if os.path.isdir(filedir):
				filelist = get_file_count(filedir)
				if len(filelist) > 0:
					filelistNew = randomList(filelist)
					print "copy filenum %s ----------> %d"%(filedir,len(filelistNew))
				else:
					continue
				for files in filelistNew:
					sourceFile = os.path.join(filedir,files)
					targetFile = os.path.join(targetDir,files)
					if os.path.isfile(sourceFile):
						shutil.copy(sourceFile, targetFile)


def tarFiles(tarFileDir):
	print "start tar dir %s" %tarFileDir
	if os.path.exists(tarFileName):
		os.remove(tarFileName)
	tarfil = tarfile.open(tarFileName, 'w:gz')
	for root, dir, files in os.walk(tarFileDir):
		for files in files:
			tarfilAbs = os.path.join(root, files)
			tarfil.add(tarfilAbs)
	tarfil.close()



def main():
	getDirs(decodeDir)
	tarFiles(tarFileDir)
	ftpTarFile(ftpDistIp, ftpDistDir, userName, passWd, tarFileName)

if __name__ == '__main__':
	main()


