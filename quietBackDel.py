#!/usr/bin/python
#encoding=utf-8
#python bakFiles.py srcDir destDir c            第三个参数不加默认为move，加'c'为copy	第二个参数为d时为快速删除

import os
import sys
import shutil
import datetime
#import threading
import multiprocessing


Max_MultiNums=5

if len(sys.argv) >= 3 and len(sys.argv) <= 4:
        srcDir = sys.argv[1]
        destDir = sys.argv[2]
        if len(sys.argv) == 4:
                flag = sys.argv[3]
        else:
                flag = 'M'
else:
        print "请输入正确的参数: python %s srcDir destDir [c|C]" % sys.argv[0]
        exit()

def quietDelete(sourceDir):
	print "start delete dir "+sourceDir
	for file in os.listdir(sourceDir):
		sourceFile = os.path.join(sourceDir,file)
		if os.path.isfile(sourceFile):
			os.remove(sourceFile)
		else:
			quietDelete(sourceFile)

def bakFiles(sourceDir, targetDir):
        print "start deal "+sourceDir
        pool = multiprocessing.Pool(Max_MultiNums)

        for file in os.listdir(sourceDir):
                sourceFile = os.path.join(sourceDir,file)
                targetFile = os.path.join(targetDir,file)

                if os.path.isfile(sourceFile):
                        if not os.path.exists(targetDir):
                                os.makedirs(targetDir)
                                print "mkdir "+targetDir
                        if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                                if 'C' != flag.upper():
                                        shutil.move(sourceFile, targetFile)
                                else:
                                        #copy_thread = threading.Thread(target=copyFiles, args=(sourceFile, targetFile))
                                        #copy_thread.start()
                                        pool.apply_async(copyFiles, args=(sourceFile, targetFile))
                if os.path.isdir(sourceFile):
                        bakFiles(sourceFile, targetFile)
        pool.close()
        pool.join()


def copyFiles(sourceFile, targetFile):
        try:
                with open(targetFile,'wb') as target_file:
                        with open(sourceFile,'rb') as sorc_file:
                                while True:
                                        filetemp = sorc_file.read(1024)
                                        if filetemp:
                                                target_file.write(filetemp)
                                        else:
                                                break
        except Exception, e:
                print "Exception):\t", str(e)
                print "err"
        finally:
                if sorc_file:
                        sorc_file.close()
                        if target_file:
                                target_file.close()



def get_file_count(dir):
    file_list = list()
    for root, dirs, files in os.walk(dir):
        for f in files:
            file_list.append(f)
    return len(file_list)


def main():
	if sys.argv[2].upper() != 'D':
        srcNums = get_file_count(srcDir)
        print "start deal files , file nums is %d " %srcNums
        starttime = datetime.datetime.now()
        bakFiles(srcDir, destDir)
        dstNums = get_file_count(destDir)
        endtime = datetime.datetime.now()
        print "end deal files , file nums is %d ! Waste time %d secounds !"%(dstNums,(endtime-starttime).seconds)
    else:
    	srcNums = get_file_count(srcDir)
    	quietDelete(srcDir)
    	print "delete success! file nums is %d !"%(srcNums)

if __name__ == '__main__':
        main()

