# coding:utf-8
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC


'''
class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  ## test method names begin 'test*'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()
'''
'''
class test(unittest.TestCase):
    def setUp(self):
        pass  #前置条件 如果没有可以不写或者pass
    def testMin(self):  # test method must begin "test*"
        self.assertEqual((10-5),5)
    def testDivide(self):
        result = 7/2 #实际结果
        hope = 3.5   #期望结果
        self.assertEqual(result,hope)
    def tearDown(self):
        pass 

if __name__== "__main__":
    unittest.main()
'''
#打开aliyun32案例
class Open32(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://aliyun.32.cn")
    def test_32(self):
        time.sleep(3)
        result = EC.title_is(u"商标注册_商标查询_商标交易就在知协网")(self.driver)
        print(result)
        self.assertTrue(result)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

