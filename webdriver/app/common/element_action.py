from app.common.read_config import *
from app.data.base_data import *
from selenium.webdriver.support.wait import WebDriverWait
from app.log.push_log import take_log


def is_element_exist(driver, ini_name, config_x, config_y):  # 判断是否存在此元素
	"""ini_name:配置文件的路径"""
	ele = read_ini(ini_name, config_x, config_y)
	source = driver.page_source
	if ele in source:
		return True
	else:
		return False


def element(driver, ele_type, page, index):  # 根据元素类型进行不同的元素定位
	"""ele_type:元素类型"""
	# try:
	if ele_type == 1:  # class_name
		the_index = read_ini(class_path, page, index)
		return WebDriverWait(driver, 30).until(lambda x: x.find_element_by_class_name(the_index))
	if ele_type == 2:  # id
		the_index1 = read_ini(id_path, page, index)
		return WebDriverWait(driver, 30).until(lambda x: x.find_element_by_id(the_index1))
	if ele_type == 3:  # tap
		the_index2 = read_ini(location_path, page, index)
		return WebDriverWait(driver, 30).until(lambda x: x.tap(the_index2, 1000))
	if ele_type == 4:  # class_names
		the_index3 = read_ini(class_path, page, index)
		return WebDriverWait(driver, 15).until(lambda x: x.find_elements_by_class_name(the_index3))
	if ele_type == 5:  # xpath
		the_index4 = read_ini(xpath_path, page, index)
		return WebDriverWait(driver, 15).until(lambda x: x.find_element_by_xpath(the_index4))
	# except TypeError:
	# 	print("抱歉，找不到元素")
	# 	take_log()
	# except TimeoutError:
	# 	print("超时，请检查代码")
	# 	take_log()
	# finally:
	# 	take_log()


def action_click(driver, ele_type, page, index):  # 点击
	element(driver, ele_type, page, index).click()


def action_send_keys(driver, ele_type, page, index, txt):  # 输入内容
	element(driver, ele_type, page, index).send_keys(txt)


def action_tap(driver, ele_type, page, index):  # 点击
	element(driver, ele_type, page, index)