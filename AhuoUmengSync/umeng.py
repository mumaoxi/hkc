#!/usr/bin/env pyhton
 # -*- coding: UTF-8 -*-
"""
Umeng客户端的基本操作：登录、获取app等
@version:	1.0
@author:	U{xi.liu<xi.liu@abcomb.com>} 
@contact:	15201280641
"""
import os
import sys
import base64
import httplib
import urllib
import json
import time

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)

#友盟的账户名密码
umeng_account = {'user_name' : '15201280641@qq.com' , 'user_pwd' : 'LiuXi!@#$%'}

#umeng登录的apiurl
umeng_api_url = {'host' : 'api.umeng.com' , 'login' : '/authorize' , 'apps_count' : '/apps/count' , 'apps_list' : '/apps' , 'new_users' : '/new_users'}


"""
将用户的用户名和密码经过特别的算法加密
@param user_name:	umeng登录的账户名
@param user_pwd:	umeng登录的账户密码
@return:	加密过的字符串，登录时需要
@rtype str: 
"""
def encode_base64_char001(user_name,user_pwd):
	print 'user_name\t'+user_name
	print 'user_pwd\t'+user_pwd
	based_str = base64.b64encode(user_name+':'+user_pwd)
	print 'base64_encoded\t'+based_str
	
	encoded_str = '';
	for x in based_str:
		encoded_str += chr((ord(x)+1))

	print 'encoded_str\t'+encoded_str
	return encoded_str


"""
使用用户名和密码登录Umeng客户端
@param user_name:	umeng登录的账户名
@param user_pwd:	umeng登录的账户密码
@return:	返回auth_token
@rtype str: 
"""
def login(user_name,user_pwd):
	auth = encode_base64_char001(user_name,user_pwd)#获取登录的auth

	params = urllib.urlencode({'auth': auth})
	headers = {"Content-type": "application/x-www-form-urlencoded"}

	conn = httplib.HTTPConnection(umeng_api_url['host'])
	conn.request("POST", umeng_api_url['login'], params, headers)

	res = conn.getresponse()
	print "\nlogin\t","POST\t",umeng_api_url['host']+umeng_api_url['login'],"\t"+params,"\n",res.status, res.reason

	#如果数据返回出错，那么return 空
	if res.status != 200:
		print "None"
		conn.close()
		return None

	data = res.read()
	print data

	conn.close()

	#解析返回来的数据
	res_json = json.loads(data)
	auth_token = res_json.get('auth_token')
	print 'auth_token\t'+auth_token

	return auth_token

"""
获取我的应用的总个数
@param auth_token:	登录时获取到的auth_token
@return:	返回此账号拥有的app的数目
@rtype int: 
"""
def apps_count(auth_token):
	url = umeng_api_url['apps_count']+"?"+urllib.urlencode({'auth_token': auth_token})
	headers = {}

	conn = httplib.HTTPConnection(umeng_api_url['host'])
	conn.request("GET", url)

	res = conn.getresponse()
	print "\napps_count\t","GET\t",umeng_api_url['host']+url,"\n",res.status, res.reason

	#如果数据返回出错，那么return 空
	if res.status != 200:
		print "None"
		conn.close()
		return None

	data = res.read()
	print data

	conn.close()

	#解析返回来的数据
	res_json = json.loads(data)
	app_count = res_json.get('count')
	print "apps_count\t" , app_count

	return app_count

"""
获取我的应用列表
@param auth_token:	登录时获取到的auth_token
@return:	返回此账号拥有的app的数目
@rtype int: 
"""
def apps_list(auth_token,apps_count,page=1,per_page=20):
	url = umeng_api_url['apps_list']+"?"+urllib.urlencode({'auth_token': auth_token,'page':page,'per_page':per_page})
	headers = {}

	conn = httplib.HTTPConnection(umeng_api_url['host'])
	conn.request("GET", url)

	res = conn.getresponse()
	print "\napps_list\t","GET\t",umeng_api_url['host']+url,"\n",res.status, res.reason

	#如果数据返回出错，那么return 空
	if res.status != 200:
		print "None"
		conn.close()
		return None

	data = res.read()
	print data

	conn.close()

	#解析返回来的数据
	app_list = json.loads(data)

	#如果当前的总请求数目比软件总数目小，那么要继续请求下一页
	if page * per_page < apps_count :
		app_list.extend(apps_list(auth_token,apps_count,page+1,per_page))

	# print "app_list\t" , app_list

	return app_list


"""
获取应用的新增数目
@param auth_token:	登录时获取到的auth_token
@return:	返回此账号拥有的app的数目
@rtype int: 
"""
def app_new_users(auth_token,appkey,start_date=time.strftime('%Y-%m-01',time.localtime(time.time())),end_date=time.strftime('%Y-%m-%d',time.localtime(time.time()-24*60*60)),period_type='daily'):
	url = umeng_api_url['new_users']+"?"+urllib.urlencode({'auth_token': auth_token,'appkey': appkey,'start_date':start_date,'end_date':end_date,'period_type':period_type})
	
	conn = httplib.HTTPConnection(umeng_api_url['host'])
	conn.request("GET", url)

	res = conn.getresponse()
	print "\napp_new_users\t","GET\t",umeng_api_url['host']+url,"\n",res.status, res.reason

	#如果数据返回出错，那么return 空
	if res.status != 200:
		print "None"
		conn.close()
		return None

	data = res.read()
	# print data

	conn.close()

	#解析返回来的数据
	the_new_user = {}
	newed_user_array = json.loads(data)
	if(len(newed_user_array['dates'])>0):
		x_date_index = 0
		for x_date in newed_user_array['dates']:
			the_new_user[x_date] = newed_user_array['data']['all'][x_date_index]
			x_date_index = x_date_index+1

	# print appkey,the_new_user
	return the_new_user
