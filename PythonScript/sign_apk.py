#!/usr/bin/env python
# -*- coding: UTF-8 -*-   
import os
import sys
import pexpect

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

input_apk_path = sys.argv[1];
output_apk_path = sys.argv[2];

jarsigner = pexpect.spawn("jarsigner -verbose -keystore hellokittycat.keystore -signedjar "+output_apk_path+".apk "+input_apk_path+" hellokittycat");
jarsigner.expect(".*:*");
jarsigner.sendline("hellokittycat");
jarsigner.expect(pexpect.EOF);

os.system("zipalign -f -v 4 "+output_apk_path +".apk "+output_apk_path+"_zipaligned.apk");