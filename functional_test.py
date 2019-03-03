from selenium import webdriver
import unittest


class NewVisitor(unittest.TestCase):
    def setUp(self):
        """执行设置操作"""
        self.brower = webdriver.Chrome()
        self.brower.implicitly_wait(3)

    def tearDown(self):
        """在运行测试后，执行清除操作"""
        self.brower.quit()

    def test_can_start_a_list_and_interactive_it_later(self):
        """测试部分必须test开头"""
        self.brower.get('http://127.0.0.1')
        self.assertIn('To-Do', self.brower.title)  # 断言
        self.fail('Finsih the test!')


if __name__ == '__main__':
    unittest.main()
