#encoding=utf-8
import os
import time
import sys


def eachFile(filepath):
	pathDir = os.listdir(filepath) 
	for files in pathDir:
		newDir=os.path.join(filepath,files)
		insert="#encoding=utf-8\n"
		if os.path.isdir(newDir) :
			print("start deal file %s:" % newDir)
			eachFile(newDir)

		else:
			print(newDir)
			with open(newDir,'r+') as f:
				f_read = f.read()
				f.seek(0,0)
				f.write(insert)
				f.write(f_read)
				f.close()

def main():
	eachFile("/Users/duanhonggang/Desktop/乱七八糟/python/Python100天计划/Day16-20")

if __name__ == '__main__':
	main()

