#!/usr/bin/python

import  cgi,cgitb,os,commands,time

cgitb.enable()


print   "content-type:text/html"
print   ""

data=cgi.FieldStorage()
#  recv software name from  services.html    
software=data.getvalue('soft')

if  software   ==   'firefox' :
	print   "wait for  firefox  "
	print  "<a href='http://192.168.10.121/cgi-bin/firefox.py'>"
	print   "click to get  firefox "
	print    "</a>"
	
elif  software  ==   'gedit' :
	print   "wait for  texteditor  "
	print  "<a href='http://192.168.10.121/gedit.sh'>"
	print   "click to get  gedit "
	print   "</a>"

elif  software  ==   'vlc' :
	print   "wait for  media player  "

elif  software  ==   'calc' :
	print   "wait for  calcccc  "



