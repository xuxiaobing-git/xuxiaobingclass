

from app.common.element_action import action_click, action_send_keys
from app.common.gestures import swipe_down
from app.common.session import driver_begin


# 测试类1
class test:
    def __init__(self):
        self.driver = driver_begin()

    def test_1(self):
        action_click(self.driver, 2, "上面一行", "消息")
        action_click(self.driver, 5, "消息页面返回", "返回")
        action_click(self.driver, 2, "主页搜索", "搜索")
        action_click(self.driver, 2, "搜索框输入", "输入")
        action_send_keys(self.driver, 2,"搜索框输入","输入","嘎嘎嘎嘎嘎过")

    def test_2(self):
        action_click(self.driver, 2, "上面一行", "消息")
















