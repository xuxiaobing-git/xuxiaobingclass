import time
from datetime import datetime
import os
import random
import re
import threading

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class usb_install_thread(threading.Thread):  # 安装确认
    def __init__(self, driver):
        threading.Thread.__init__(self)
        self.driver = driver

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        usb_install(self.driver)


def usb_install(driver):
    try:
        em = driver.find_element_by_xpath("//android.widget.Button[contains(@text,'继续安装')]")
        if em:
            em.click()
    except:
        pass

    try:
        em = driver.find_element_by_id("android:id/button1")
        em.click
        em = driver.find_element_by_id("com.android.packageinstaller:id/btn_allow_once")
        em.click
        em = driver.find_element_by_id("com.android.packageinstaller:id/ok_button")
        em.click

    except:
        pass

    try:
        em = driver.find_element_by_xpath("//android.widget.Button[contains(@text,'允许')]")
        if em:
            em.click()
    except:
        pass

    try:
        em = driver.find_element_by_xpath("//android.widget.Button[contains(@text,'始终允许')]")
        if em:
            em.click()
    except:
        pass

    try:
        em = driver.find_element_by_xpath("//android.widget.Button[contains(@text,'确认')]")
        if em:
            em.click()
    except:
        pass


lock = threading.RLock()


# 多线程
class DriverThread(threading.Thread):
    def __init__(self, thread_id, name, app_location, app_package='com.foryou.haoyun',
                 app_activity='.entry.EntryActivity', appium_port='4723', device_no=1, mobile='16011111111',
                 monkey_counts=10000000
                 ):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.app_location = app_location
        self.app_package = app_package
        self.app_activity = app_activity
        self.appium_port = appium_port
        self.device_no = device_no
        self.monkey_counts = monkey_counts
        self.mobile = mobile

    def run(self):
        print("开始线程：" + self.name)
        lock.acquire()
        driver, device_id = get_driver(self.app_location, self.app_package, self.app_activity, self.appium_port,
                                       self.device_no)
        login(driver, self.app_package, mobile=self.mobile)
        lock.release()
        time.sleep(5)

        adb_monkey(self.app_package, device_id, counts=self.monkey_counts)
        print("退出线程：" + self.name)


# 获取driver
def get_driver(app_location, app_package, app_activity, appium_port,
               device_no):
    # 测试的包的路径和包名
    # appLocation = " /Users/Downloads/app.apk "

    # 读取设备 id
    read_device_id = list(os.popen('adb devices').readlines())

    # 正则表达式匹配出 id 信息
    device_id = re.findall(r'^\w*\b', read_device_id[device_no])[0]

    # 读取设备名
    device_name = os.popen('adb -s ' + device_id + ' shell getprop ro.product.model').read()

    # 读取设备系统版本号
    device_android_version = list(
        os.popen('adb -s ' + device_id + ' shell getprop ro.build.version.release').readlines())
    device_version = re.findall(r'^\w*\b', device_android_version[0])[0]

    desired_caps = {
        'appPackage': app_package,
        'platformName': 'Android',
        'platformVersion': device_version,
        'deviceName': device_name,
        'app': app_location,
        'appActivity': app_activity,
        'noReset': False,  # true:不重新安装APP，false:重新安装app
        'udid': device_id,
        'newCommandTimeout': 120,  # Appium服务器待appium客户端发送新消息的时间。默认为60秒
        # 让Appium自动确定您的应用所需的权限，并在安装时将其授予应用。默认为false。
        # 如果noReset是true，则此功能不起作用。
        'autoGrantPermissions': True,
        'normalizeTagNames': True
    }

    driver = webdriver.Remote("http://127.0.0.1:" + appium_port + "/wd/hub", desired_caps)
    return driver, device_id


# 登录
def login(driver, app_package='com.foryou.haoyun', mobile='16011111111'):
    if app_package == 'com.foryou.haoyun':
        mobile_loc = 'com.foryou.haoyun:id/account_edit'
        login_btn_loc = 'com.foryou.haoyun:id/login_btn'
        check_code_loc = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.EditText'
    if app_package == 'com.foryou.agent':
        mobile_loc = 'com.foryou.agent:id/account_edit'
        login_btn_loc = 'com.foryou.agent:id/login_btn'
        check_code_loc = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.EditText'
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(mobile_loc)).click()
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(mobile_loc)).send_keys(mobile)
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id(login_btn_loc)).click()
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(check_code_loc + '[1]')).send_keys('1')
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(check_code_loc + '[2]')).send_keys('1')
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(check_code_loc + '[3]')).send_keys('2')
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(check_code_loc + '[4]')).send_keys('3')


# monkey命令
def adb_monkey(app_package, device_id, monkey_seed=str(random.randrange(1, 1000)), counts=10000000):
    log_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
                            'log/' + app_package.split('.')[-1] + '/' + datetime.now().strftime(
                                '%Y-%m-%d-%H:%M:%S') + '.txt')
    # pct-motion :调整动作事件的百分比(动作事件由屏幕上某处的一个down事件、一系列的伪随件机事和一个up事件组成)
    # throttle:设置一个起效的事件发生后时延时。
    # pct-nav:调整“基本”导航事件的百分比(导航事件由来自方向输入设备的up/down/left/right组成)
    # pct-majornav:调整“主要”导航事件的百分比(这些导航事件通常引发图形界面中的动作，如：5-way键盘的中间按键、回退按键、菜单按键)
    # pct-trackball：调整轨迹事件的百分比(轨迹事件由一个或几个随机的移动组成，有时还伴随有点击)
    # pct-syskeys:指定系统按键的百分比，包括HOME、Back、音量等。
    print(datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
    adb_monkey = "adb -s " + device_id + " shell monkey -p %s -s %s -v -v -v --ignore-crashes --pct-touch 30 --throttle 200 --pct-motion 20 --pct-nav 20 --pct-majornav 15 --pct-appswitch 5 --pct-anyevent 5 --pct-trackball 0 --pct-syskeys 0 %s > %s" % (
        app_package, monkey_seed, counts, log_path)
    os.popen(adb_monkey)
    print(adb_monkey)
    print(datetime.now().strftime('%Y-%m-%d-%H:%M:%S'))
