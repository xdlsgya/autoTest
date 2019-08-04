#!/usr/bin/python
# -*- coding:utf-8 -*-


import sys, os
import subprocess, cmd
from collections import defaultdict
import traceback
import re
import time,datetime

dict_lib_scope = defaultdict(list)
list_update = []
match_list = []
match_map = defaultdict(list)
CUR_PATH = "/home/jason/k8s/bm"
SOURCE_PATH = "/home/jason/k8s/bm"

def get_file_list(path):
    cur_files = os.listdir(path)
    all_files_list = []
    for file_name in cur_files:
        full_file_name = os.path.join(path, file_name)
        all_files_list.append(full_file_name)
        if os.path.isdir(full_file_name):
            next_level_files = get_file_list(full_file_name)
            all_files_list.extend(next_level_files)
    print all_files_list
    return all_files_list,cur_files

def get_allfiles(path):
    cur_files = os.listdir(path)
    all_files_list = []
    #all_files = []
    for file_name in cur_files:
        full_file_name = os.path.join(path, file_name)
        all_files_list.append(full_file_name)
        if os.path.isfile(full_file_name):
            list_update.append(full_file_name)
        if os.path.isdir(full_file_name):
            next_level_files = get_allfiles(full_file_name)
            all_files_list.extend(next_level_files)
    print all_files_list
    return all_files_list


def read_config():
    #dict_lib_scope = defaultdict(list)
    files_path = "./filelist/"
    all_files_list , short_filename_list = get_file_list(files_path)
    try:
        file = open("./filelist/lib_list.txt", "r")
        lines = file.read();
        lines = lines.split('\n')
        for line in lines:
            if line == '':
                continue;
            col = line.split('\t')
            if col[0][0] == '#' or  col[0] == '':
                continue;
            else:
                libname = col[0]
                #print "debug:" + libname
                scope_zc = col[1]
                scope_jf = col[2]
                scope_decode = col[3]
                scope_cc = col[4]
                scope_xc = col[5]
                scope_frame = col[6]
                info = libname + '\t' + scope_zc + '\t' + scope_jf+ '\t' + scope_decode + '\t' + scope_cc + '\t' + scope_xc + '\t' + scope_frame + '\t'
                #print("info:" + info)
                if scope_zc == "1":
                    dict_lib_scope[libname].append("zc" + ":lib_list")
                if scope_jf == "1":
                    dict_lib_scope[libname].append("jf:" + "lib_list")
                if scope_decode == "1":
                    dict_lib_scope[libname].append("decode:" + "lib_list")
                if scope_cc == "1":
                    dict_lib_scope[libname].append("cc:" + "lib_list")
                if scope_xc == "1":
                    dict_lib_scope[libname].append("xc" + ":lib_list")
                    dict_lib_scope[libname].append("zc" + ":lib_list" +  ":xc")
                    dict_lib_scope[libname].append("jf" + ":lib_list" +  ":xc")
                    dict_lib_scope[libname].append("decode" + ":lib_list" +  ":xc")
                    dict_lib_scope[libname].append("cc" + ":lib_list" +  ":xc")

                if scope_frame == "1":
                    dict_lib_scope[libname].append("dse" + ":lib_list" + ":frame")
                    dict_lib_scope[libname].append("xc" + ":lib_list" + ":frame")
                    dict_lib_scope[libname].append("zc" + ":lib_list" + ":frame")
                    dict_lib_scope[libname].append("jf" + ":lib_list" + ":frame")
                    dict_lib_scope[libname].append("decode" + ":lib_list" + ":frame")
                    dict_lib_scope[libname].append("cc" + ":lib_list" + ":frame")
                    dict_lib_scope[libname].append("xfer" + ":lib_list" + ":frame")

        print (dict_lib_scope)

        bRet = True
    except Exception, e:
        print 'Exception):\t', str(e)
        bRet = False
        print "err"
    finally:
        if file:
            file.close()


    try:
        file = open("./filelist/bin_list.txt", "r")
        lines = file.read();
        lines = lines.split('\n')
        for line in lines:
            if line == '':
                continue;
            col = line.split('\t')
            if col[0][0] == '#':
                continue;
            else:
                binname = col[0]
                #print "debug:" + libname
                scope_billing_bin = col[1]
                scope_frame_bin = col[2]
                if scope_billing_bin == "1":
                    dict_lib_scope[binname].append("zc" + ":bin_list" + ":billing")
                    dict_lib_scope[binname].append("jf" + ":bin_list" + ":billing")
                    dict_lib_scope[binname].append("decode" + ":bin_list" + ":billing")
                    dict_lib_scope[binname].append("cc" + ":bin_list" + ":billing")
                if scope_frame_bin == "1":
                    dict_lib_scope[binname].append("des" + ":bin_list" + ":frame")
                    dict_lib_scope[binname].append("xc" + ":bin_list" + ":frame")
                    dict_lib_scope[binname].append("zc" + ":bin_list" + ":frame")
                    dict_lib_scope[binname].append("jf" + ":bin_list" + ":frame")
                    dict_lib_scope[binname].append("decode" + ":bin_list" + ":frame")
                    dict_lib_scope[binname].append("cc" + ":bin_list" + ":frame")
                    dict_lib_scope[binname].append("xfer" + ":bin_list" + ":frame")

        print (dict_lib_scope)

        bRet = True
    except Exception, e:
        print 'Exception):\t', str(e)
        bRet = False
        print "err"
    finally:
        if file:
            file.close()

    for other_file in short_filename_list:
        if (re.search("bin_list.txt",other_file) <> None) or  (re.search("lib_list.txt",other_file) <> None):
            #print "do noting fro bin lib list"
            continue
        print other_file
        read_commont_config(other_file)


def read_commont_config(file_name):
    try:
        other_file = open("./filelist/"+file_name, "r")
        other_lines = other_file.read();
        other_lines = other_lines.split('\n')
        for other_line in other_lines:
            print other_line
            if(other_line <> '') :
                dict_lib_scope[other_line].append(file_name)
        print (dict_lib_scope)

        bRet = True
    except Exception, e:
        print 'Exception):\t', str(e)
        bRet = False
        print "err"
    finally:
        if other_file:
            other_file.close()


def unpackage(packageFilelist):
    today_time = time.strftime("%Y%m%d")
    now_time = time.strftime("%Y%m%d%H%M%S")
    packagePath = CUR_PATH + '/package/' + today_time
    if not os.path.exists(packagePath):
        os.mkdir(packagePath)
        print ('mkdir %s' % packagePath)
    source_file = SOURCE_PATH + '/' + packageFilelist + '.tar.gz'
    os.system('cp %s %s' % (source_file, packagePath))
    upgrade_tz = packagePath + '/' + packageFilelist + '.tar.gz'
    print upgrade_tz
    os.system('cd %s;tar -zxvf %s' % (packagePath, upgrade_tz))
    print ('unpack tar.gz:tar -xcvf %s %s' % (upgrade_tz, packagePath))
    os.system('rm %s' % upgrade_tz)
    get_allfiles(packagePath)
    print '######################################'
    print list_update
    print '######################################'
    return upgrade_tz


def match():
    for key in dict_lib_scope.keys():
        for j in range(len(list_update)):
            #print list_update[j],key
            if str(list_update[j]).find(str(key)) == -1:
                continue
            print '**************************************'
            print 'match:',list_update[j], '->',key
            match_list.extend(dict_lib_scope[key])
            match_map[key].extend(dict_lib_scope[key])
            break
            #print '**************************************'
            #print(dict_lib_scope[key])
    print "match_result:",match_list
    print "match_map:", match_map

if __name__ == "__main__":
    packagelist = sys.argv[1]
    read_config()
    unpackage(packagelist)
    match()