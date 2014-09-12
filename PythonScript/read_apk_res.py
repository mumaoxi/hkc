#!/usr/bin/env python
 # -*- coding: UTF-8 -*- 
import os
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)

import zipfile

z = zipfile.ZipFile("FunshionAphone2.2.0.4_SID_1691_zipalign.apk", "r")

#打印zip文件中的文件列表
for filename in z.namelist(  ):
    print 'File:', filename

#读取zip文件中的第一个文件
first_file_name = 'res/drawable-hdpi/icon.png'
content = z.read(first_file_name)
file_object = open('icon.png', 'w')
file_object.write(content)
file_object.close( )

print first_file_name
# print content