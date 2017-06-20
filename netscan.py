#!/usr/bin/python2

import  commands,os
x="192.168.10."

ip_list=[]
for  i   in   range(121)[100:]  :
	check=os.system('ping  -c  1  -i  0.00000000001  '+x+str(i))
	if  check  ==   0 :
		ip_list.append(x+str(i))





print   ip_list



	
