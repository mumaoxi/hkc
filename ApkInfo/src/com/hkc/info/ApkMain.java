package com.hkc.info;

import com.sinaapp.msdxblog.apkUtil.entity.ApkInfo;
import com.sinaapp.msdxblog.apkUtil.utils.ApkUtil;
import com.sinaapp.msdxblog.apkUtil.utils.IconUtil;

public class ApkMain {

	public static void main(String[] args) {
		try {
			String apkpath = "/Users/Saxer/快盘/app_reverse/缘来一线牵_V4.2.3_C151.apk";
			if (args.length > 0) {
				apkpath = args[0];
			}
			ApkInfo apkInfo = new ApkUtil().getApkInfo(apkpath);
			// 打印获取到的信息
			System.out.println(apkInfo);
			// 获取Icon并保存到指定位置
//			IconUtil.extractFileFromApk(apkpath, apkInfo.getApplicationIcon(), "D:\\DefaultApkTempSaveFolder\\3G安卓市场\\crawler\\icon.png");
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
