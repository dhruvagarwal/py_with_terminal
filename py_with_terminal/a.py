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
os.system("mkdir commands")
for x in a:
	os.system("man %s> commands/%s.txt" % (x,x))


