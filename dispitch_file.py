#!/usr/bin/python
# -*- coding:utf-8 -*-


import sys
import os
import shutil


if len(sys.argv) == 4 and sys.argv[3].upper() == 'C':
	flag = 'C'
elif len(sys.argv) == 3:
	flag = 'M'
else:
	print "请输入正确的参数: python %s monitorFileName decodeFileDir [m|c]" % sys.argv[0]
	exit()

monitorFile = sys.argv[1]
decodeFileDir = sys.argv[2]


def dispitchFile(fileName):
	print "start dispitch file"
	with open(fileName,'r') as monitor:
		lines=monitor.read().splitlines()
		for line in lines:
			srcFile = os.path.join(decodeFileDir, line.split(':')[0])
			destDir = line.split(':')[1]
			if os.path.exists(srcFile):
				if 'M'==flag.upper():
					print "move %s to %s" %(srcFile, destDir)
					shutil.move(srcFile, destDir)
				else:
					print "copy %s to %s" %(srcFile, destDir)
					shutil.copy(srcFile, destDir)

def main():
	dispitchFile(monitorFile)

if __name__ == '__main__':
	main()
