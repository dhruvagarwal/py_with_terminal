#!/usr/bin/env python
import os
a=["pwd",
"cp",
"ls",
"mkdir",
"mv",
"rm",
"grep",
"head",
"less",
"more",
"tail",
"cal",
"date",
"fsck",
"file",
"ping",
"ftp",
"host",
"ifconfig",
"netstat",
"route",
"telnet",
"sleep",
"pidof",
"ps",
"cat",
"crontab",
"man",
"mount",
"umount",
"fdisk",
"dd",
"df",
"chmod",
"su",
"passwd",
"groupadd",
"groupmod",
"chgrp",
"groupdel"]
fo=raw_input("Enter a desired folder name-")
os.system("mkdir %s" % fo)
for x in a:
	os.system("man %s> %s/%s.txt" % (x,fo,x))


