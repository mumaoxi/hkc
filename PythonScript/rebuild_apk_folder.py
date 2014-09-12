#!/usr/bin/env python
 # -*- coding: UTF-8 -*- 
import os
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)

#原文件夹
src_path = sys.argv[1]

#目标apk的名字
dest_apk_name =  sys.argv[2]

#第一步，打包apk
os.system("java -jar apktool.jar b -f "+src_path)

#第二步，签名目标文件
os.system("python sign_apk.py "+src_path+"/dist/"+src_path+".apk "+dest_apk_name)
