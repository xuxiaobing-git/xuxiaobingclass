from appium import webdriver


def driver_begin():
	desired_caps = {
		'platformName': 'Android',
		'deviceName': '760BBL423AVM',
		'platformVersion': '5.1',
		'appPackage': 'com.netease.newsreader.activity',
		'appActivity': 'com.netease.nr.biz.ad.newAd.AdActivity',
		'noReset': True,
		'resetKeyboard': True, # 将键盘给隐藏起来
		'autoGrantPermissions': True
		# 'unicodeKeyboard': True,# 使用unicodeKeyboard的编码方式来发送字符串
	}
	return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
