#!/usr/bin/env pyhton
 # -*- coding: UTF-8 -*-

import os
import sys
import umeng

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)

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


"""
根据应用列表，获取每个应用的新增活跃用户
"""
def get_all_aihuoapp_new_users_data(auth_token,apps_list,start_date=time.strftime('%Y-%m-01',time.localtime(time.time())),end_date=time.strftime('%Y-%m-%d',time.localtime(time.time()-24*60*60))):
	for app in apps_list:
		if app['aihuo_adv_id'] > 0:
			the_new_users = umeng.app_new_users(auth_token,app['appkey'],start_date,end_date)
			#TODO:获取到新增用户之后，就可以把这些数据同步到爱火商盟的后台了



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
