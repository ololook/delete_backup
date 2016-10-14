#!/usr/bin/python
from datetime import datetime
import time,datetime
import sys, os, subprocess, tarfile
import socket
import re
import shlex
import string
backupdir="/data/mysqldump/"


def DELETE_OVERDU_BACKUP():
    filelist=[]
    filelist=os.listdir(backupdir)
    for i in  filelist:
        backupset=backupdir+i
        ftl =time.strftime('%Y-%m-%d',time.gmtime(os.stat(backupdir+i).st_mtime))
        year,month,day=ftl.split('-')
        ftll=datetime.datetime(int(year),int(month),int(day))
        year,month,day=time.strftime('%Y-%m-%d',time.gmtime()).split('-')
        localtll=datetime.datetime(int(year),int(month),int(day))
        days=(localtll-ftll).days
        if days>=60:
           try:
                os.remove(backupdir+i)
           except:
                print "delete overdue backup failed"
        else:
           pass
def  main():
    DELETE_OVERDU_BACKUP()
if __name__ == '__main__':
    main()
