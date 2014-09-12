#!/usr/bin/env python
 # -*- coding: UTF-8 -*- 
import os
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)

#原文件
src_apk = sys.argv[1]
src_path = src_apk.replace(".apk","") 

#目标文件件
dest_path = sys.argv[2]

#目标apk的名字
dest_apk_name =  sys.argv[3]


#第一步，反编译apk
os.system("java -jar apktool.jar d -f "+src_apk)

#第二步,移动文件到目标文件夹
os.system("python move_hkc_files.py "+src_path+" "+dest_path)

#第三步，打包目标apk
os.system("java -jar apktool.jar b "+dest_path)

#第四步，签名目标文件
os.system("python sign_apk.py "+dest_path+"/dist/"+dest_path+".apk "+dest_apk_name)
