#!/usr/bin/env python
#_*_ coding:utf-8 _*_

'''  参数文件格式
#***************mdb***********#
10.70.139.26,mdb,Bill@Oo0,new:routa zwa1,
10.70.139.31,mdb,Bill@Oo0,new:routd zwd1,
10.70.139.27,mdb,Bill@Oo0,new:usera1 rata2,
#***************billing***********#
10.70.139.24,billing,Bill@Oo0,vm01,
10.70.139.25,billing,Bill@Oo0,vm02,
'''

import sys;
import os;
import string;

def cout(d):
        Ks = d.keys();
        Ks.sort();
        print '\n*****************REMOTE MACHINE LIST*****************'
        for key in Ks:
                if d[key][0] == '*':
                        print d[key];
                else:
                        print key,'==>',d[key];
        print '*****************REMOTE MACHINE LIST*****************'
        print 'please select sequence no:';

def is_num_by_except(num):
        try:
                int(num)
                return True
        except ValueError:
                # print "%s ValueError" % num
                return False


filename='/app/billing/maintain/duanhg/'+sys.argv[1]
hostfile=open(filename,'r');
lines=hostfile.read();
lines=lines.split('\n');
seq_no=0
seqno2machine={}
seqno2machineinfo={}
subseqno2machineinfo={}

for line in lines:
        if line == '':
                continue;

        col=line.split(',');

        if col[0][0] =='#':
                continue;

        seq_no=seq_no+1;
        if col[0][0] =='*':
                info=col[0];
                command='';
        else:
                info=col[1]+'@'+col[0]+'\t'+col[3]+'\t'+col[4];
                command='/app/billing/maintain/duanhg/sshpass -p "'+col[2]+'" ssh '+col[1]+'@'+col[0]+' -o StrictHostKeyChecking=no';
        seqno2machine[seq_no]=command
        seqno2machineinfo[seq_no]=info
        #print seq_no,command;
while True:
        if len(subseqno2machineinfo) == 0:
                cout(seqno2machineinfo);
        else:
                cout(subseqno2machineinfo);
        subseqno2machineinfo={};
        seq_no=raw_input('>>');
        if is_num_by_except(seq_no):
                if seqno2machine.has_key(int(seq_no)):
                        print '\n\n\n';
                        print 'connect to '+seqno2machineinfo[int(seq_no)];
                        print '\n\n\n';
                        print os.system(seqno2machine[int(seq_no)]);
        else:
                if 'EXIT'==seq_no.upper() or 'Q'==seq_no.upper() or 'QUIT'==seq_no.upper() or 'BYE'==seq_no.upper():
                        break;
                else:
                        Ks = seqno2machineinfo.keys();
                        for key in Ks:
                                if string.find(seqno2machineinfo[key],seq_no) >= 0:
                                        subseqno2machineinfo[key]=seqno2machineinfo[key];
                        #print '!!input ['+seq_no+'] not in list!!'
