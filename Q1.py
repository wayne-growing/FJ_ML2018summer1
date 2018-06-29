# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 14:01:11 2018

@author: leezheng
"""
import os

file_loc = input('Input your file location')
os.chdir(file_loc)

txt_data= open("words.txt", "r")
contain_test = txt_data.read().split(' ')
#print (contain_test)
a=[]
b=[]
num=0
count=0
for i in contain_test:
	if i not in b:
		b.append(i)
		new_contain=contain_test[count]+' '+str(num)+' '+ str(contain_test.count(i))
		a.append(new_contain)
		num+=1
	count+=1

ans= open("Q1.txt","w+")
for j in range(len(a)):
    ans.write("%s\n" % a[j])
ans.close()
