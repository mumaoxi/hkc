#!/usr/bin/env python
# -*- coding: UTF-8 -*-   
import os
import sys
import string

base_path = '';

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#找出public.xml中drawable、layout、id、等的最大值
def find_max_value(file_path):
	global public_item_anim
	global public_item_array
	global public_item_attr
	global public_item_bool
	global public_item_color
	global public_item_dimen
	global public_item_drawable
	global public_item_id
	global public_item_layout
	global public_item_raw
	global public_item_string
	global public_item_style
	global public_item_styleable
	try:
			from xml.etree import ElementTree as ET
			public_parse = ET.parse(file_path);
			items = public_parse.findall('public');
			for item in items:
				if cmp(item.attrib['type'],"anim") == 0 and cmp(item.attrib['id'],public_item_anim)>0 :
					public_item_anim = item.attrib['id'];
				if cmp(item.attrib['type'],"array") == 0  and cmp(item.attrib['id'],public_item_array)>0 :
					public_item_array = item.attrib['id'];
				if cmp(item.attrib['type'],"attr") == 0  and cmp(item.attrib['id'],public_item_attr)>0 :
					public_item_attr = item.attrib['id'];
				if cmp(item.attrib['type'],"bool") == 0  and cmp(item.attrib['id'],public_item_bool)>0 :
					public_item_bool = item.attrib['id'];
				if cmp(item.attrib['type'],"color") == 0  and cmp(item.attrib['id'],public_item_color)>0 :
					public_item_color = item.attrib['id'];
				if cmp(item.attrib['type'],"dimen") == 0  and cmp(item.attrib['id'],public_item_dimen)>0 :
					public_item_dimen = item.attrib['id'];
				if cmp(item.attrib['type'],"drawable") == 0  and cmp(item.attrib['id'],public_item_drawable)>0 :
					public_item_drawable = item.attrib['id'];
				if cmp(item.attrib['type'],"id") == 0  and cmp(item.attrib['id'],public_item_id)>0 :
					public_item_id = item.attrib['id'];
				if cmp(item.attrib['type'],"layout") == 0  and cmp(item.attrib['id'],public_item_layout)>0 :
					public_item_layout= item.attrib['id'];
				if cmp(item.attrib['type'],"raw") == 0  and cmp(item.attrib['id'],public_item_raw)>0 :
					public_item_raw = item.attrib['id'];
				if cmp(item.attrib['type'],"string") == 0  and cmp(item.attrib['id'],public_item_string)>0 :
					public_item_string = item.attrib['id'];
				if cmp(item.attrib['type'],"style") == 0  and cmp(item.attrib['id'],public_item_style)>0 :
					public_item_style = item.attrib['id'];
				if cmp(item.attrib['type'],"styleable") == 0  and cmp(item.attrib['id'],public_item_styleable)>0 :
					public_item_styleable = item.attrib['id'];

	except Exception, e:
			print "find_max_value Error "+str(e);


apk_path = sys.argv[1]
file_path = apk_path.replace(".apk","");

public_item_anim = "";
public_item_array = "";
public_item_attr = "";
public_item_bool = "";
public_item_color = "";
public_item_dimen = "";
public_item_drawable = "";
public_item_id = "";
public_item_layout = "";
public_item_raw = "";
public_item_string = "";
public_item_style = "";
public_item_styleable = "";

public_item = '<public type="%s" name="" id="%s" />'

find_max_value(file_path+"/res/values/public.xml")
# print public_item % 'anim' , public_item_anim 
# print public_item % 'array' , public_item_array
# print public_item % 'attr' , public_item_attr
# print public_item % 'bool' , public_item_bool
# print public_item % 'color' , public_item_color
# print public_item % 'dimen' , public_item_dimen
# print public_item % 'drawable' , public_item_drawable
# print public_item % 'id' , public_item_id
# print public_item % 'layout' , public_item_layout
# print public_item % 'raw' , public_item_raw
# print public_item % 'string' , public_item_string
# print public_item % 'style' , public_item_style
# print public_item % 'styleable' , public_item_styleable
print 'anim\t' + public_item_anim 
print 'array\t' + public_item_array
print 'attr\t' + public_item_attr
print 'bool\t' + public_item_bool
print 'color\t' + public_item_color
print 'dimen\t' + public_item_dimen
print 'drawable\t' + public_item_drawable
print 'id\t' + public_item_id
print 'layout\t' + public_item_layout
print 'raw\t' + public_item_raw
print 'string\t' + public_item_string
print 'style\t' + public_item_style
print 'styleable\t' + public_item_styleable