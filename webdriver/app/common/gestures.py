def swipe_up(driver, t=500, n=1):  # 向上滑
	size = driver.get_window_size()
	x_start = size['width'] * 0.5  # x坐标
	y_start = size['height'] * 0.75  # 起始y坐标
	x_end = size['height'] * 0.25  # 终点y坐标
	for i in range(n):
		driver.swipe(x_start, y_start, x_start, x_end, t)


def swipe_down(driver, t=500, n=1):  # 向下滑
	size = driver.get_window_size()
	x_start = size['width'] * 0.5  # x坐标
	y_start = size['height'] * 0.25  # 起始y坐标
	y_end = size['height'] * 0.75  # 终点y坐标
	for i in range(n):
		driver.swipe(x_start, y_start, x_start, y_end, t)


def swip_left(driver, t=500, n=1):  # 向左滑
	size = driver.get_window_size()
	x_start = size['width'] * 0.75
	y_start = size['height'] * 0.5
	x_end = size['width'] * 0.25
	for i in range(n):
		driver.swipe(x_start, y_start, x_end, y_start, t)


def swip_right(driver, t=500, n=1):  # 向右滑
	size = driver.get_window_size()
	x_start = size['width'] * 0.25
	y_start = size['height'] * 0.5
	x_end = size['width'] * 0.75
	for i in range(n):
		driver.swipe(x_start, y_start, x_end, y_start, t)
