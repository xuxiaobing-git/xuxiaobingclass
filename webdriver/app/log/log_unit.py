import logging


class MyLogger:  # 定制一个log类
	def __init__(self, path, cmd_level=logging.DEBUG, write_level=logging.DEBUG):  # 初始化参数
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
		# 设置CMD日志
		sh = logging.StreamHandler()
		sh.setFormatter(fmt)
		sh.setLevel(cmd_level)
		# 设置文件日志
		fh = logging.FileHandler(path)  # 哪个模块使用文件就存在哪个下面，便于拍错
		fh.setFormatter(fmt)
		fh.setLevel(write_level)
		self.logger.addHandler(sh)
		self.logger.addHandler(fh)

	def debug(self, message):
		self.logger.debug(message)

	def info(self, message):
		self.logger.info(message)

	def warn(self, message):
		self.logger.warning(message)

	def error(self, message):
		self.logger.error(message)

	def cri(self, message):
		self.logger.critical(message)
