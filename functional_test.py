from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitor(unittest.TestCase):
    def setUp(self):
        """执行设置操作"""
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """在运行测试后，执行清除操作"""
        self.browser.quit()

    def test_can_start_a_list_and_interactive_it_later(self):
        """测试部分必须test开头"""
        # 头部和标题都包括'To-Do'
        self.browser.get('http://localhost:8000')
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # 邀请他输入待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        # 她在文本框输入了做鱼饵
        inputbox.send_keys(Keys.ENTER)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1:Buy peacock feathers' for row in rows),
                        'New to-do item did not appear in table')
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
