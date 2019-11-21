import traceback
from datetime import datetime
import time
from app.log.log_unit import *

def take_log():  # 以日期格式起不重复的日志文件名字并写入日志
	float_time = time.time()  # 当前时间浮点
	date_time = datetime.now().date().isoformat()  # 当前日期
	log_name = date_time + '_' + str(round(float_time)) + '.txt'  # 拼接文件名
	temp = MyLogger("D:\\webdriver\\log\\log_info\\"+log_name, logging.ERROR, logging.DEBUG)  # 实例化MyLogger
	temp.info('''异常信息为：''' + str(traceback.print_exc()))  # 输出异常信息到文件和控制台
	temp.info("测试完毕")