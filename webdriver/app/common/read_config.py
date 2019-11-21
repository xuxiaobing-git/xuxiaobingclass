import configparser


def read_ini(ini_name, config_x, config_y):  # 根据文件读取ini文件
	conf = configparser.ConfigParser()
	conf.read(ini_name, encoding="utf-8-sig")
	temp = conf.get(config_x, config_y)
	return temp
