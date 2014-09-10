#!/usr/bin/env pyhton
 # -*- coding: UTF-8 -*-

import os
import sys
import umeng
import time
import httplib
import urllib
import platform

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)

#同步数据的api
sync_api_url = {'host':'10.0.1.122:3000' if 'Darwin' in platform.platform() else '10.122.73.115:8080','sync':'/api/v1/platform_statistics'}

#此次同步的渠道名称
sync_channel_name = "广点通_友盟"

"""
只保留数字
"""
def only_num(s,oth=''):
    s2 = s.lower();
    fomart = '0123456789'
    for c in s2:
        if not c in fomart:
            # s = s.replace(c,'');
            return 0 
    return int(s)


"""
格式化我的应用列表
"""
def format_apps_list(apps_list):
	#遍历应用
	for app in apps_list:
		app_name = app['name'];
		app_name_cut = app_name.split('_')

		#爱火广告id
		aihuo_adv_id = only_num(app_name_cut[len(app_name_cut)-1])
		app['aihuo_adv_id'] = aihuo_adv_id 

		print 'app\t',app_name,"\t\taihuo_id\t",app['aihuo_adv_id']

	return apps_list

#同步数据到爱火广告联盟的后台
def sync_data_to_server(adv_content_id,install_count,report_date):
	url = sync_api_url['sync']+"?"+urllib.urlencode({'adv_content_id': adv_content_id,'platform_name':sync_channel_name,'install_count': install_count,'report_date':report_date.replace("-",".")})
	host = sync_api_url['host'];
	conn = httplib.HTTPConnection(host)
	conn.request("GET", url)

	res = conn.getresponse()
	print "\nsync_data_to_server\t","GET\t",host+url,"\n",res.status, res.reason

	#如果数据返回出错，那么return 空
	if res.status != 200:
		conn.close()
		return None

	data = res.read()
	# print data

	conn.close()

"""
根据应用列表，获取每个应用的新增活跃用户
"""
def get_all_aihuoapp_new_users_data(auth_token,apps_list,start_date=time.strftime('%Y-%m-01',time.localtime(time.time())),end_date=time.strftime('%Y-%m-%d',time.localtime(time.time()))):
	for app in apps_list:
		if app['aihuo_adv_id'] > 0:
			the_new_users = umeng.app_new_users(auth_token,app['appkey'],start_date,end_date)
			#TODO:获取到新增用户之后，就可以把这些数据同步到爱火商盟的后台了
			for key in the_new_users.keys():
				data_date = key #新增用户的时间
				data_new_users = the_new_users[key] #新增用户的数据
				#今天
				date_today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
				#昨天
				date_yestday = time.strftime('%Y-%m-%d',time.localtime(time.time()-24*60*60)) 

				#只同步今天或者昨天的数据
				if data_date == date_today or data_date == date_yestday:
					sync_data_to_server(app['aihuo_adv_id'],str(int(the_new_users[key])),key)


#登录
auth_token = umeng.login(umeng.umeng_account.get('user_name'),umeng.umeng_account.get('user_pwd'))

#获取应用总数目
apps_count = umeng.apps_count(auth_token)

#获取应用列表
app_list = umeng.apps_list(auth_token,apps_count)

#格式化应用列表
apps_list = format_apps_list(app_list)

#获取所有的爱火app的新增数据
get_all_aihuoapp_new_users_data(auth_token,apps_list)
