#!/usr/bin/python

import  cgi,os,commands,time,sys,cgitb

cgitb.enable()

print   "content-type:text/html"
print   ""

#  this is  for  rec data from  cloudX  
recv=cgi.FieldStorage()
user=recv.getvalue('u')
password=recv.getvalue('p')

if  user  ==  'root'  and  password  ==   'redhat1'  :
	print   "Login  Done"
	print    "<br/>"
	print    "<br/>"
	print   "<a href='http://192.168.10.121/cloudX/services.html'>"
	print   "click here  to  Access  CLoudX"
	print   "</a>"

else  :
	print  "bad Auth  "
	print  "<a  href='http://192.168.10.121/cloudX/'>"
	print   "Click here to try  again"
	print   "</a>"


