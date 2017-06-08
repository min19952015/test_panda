# usr/bin/python
# encoding:utf-8

import time
from appium import webdriver
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        #定义初始化的属性信息
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        # self.desired_caps['platformVersion'] = '4.4.2'
        # self.desired_caps['deviceName'] = 'emulator-5554'
        # self.desired_caps['platformVersion'] = '5.1.1'
        # self.desired_caps['deviceName'] = '6&2b89880e&0&0003'
        self.desired_caps['platformVersion'] = '4.4.4'
        self.desired_caps['deviceName'] = '192.168.48.101:5555'
        self.desired_caps['appPackage'] = 'com.etoppaas.PandaInsure'
        self.desired_caps['appActivity'] = 'com.panda.sdk.activity.MainActivity'
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        self.desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)



        # Switch 切换当前的上下文
        #print self.driver.contexts
        self.driver.switch_to.context('WEBVIEW_0')
        #print self.driver.current_context


       #登陆熊猫账号
    def test_login(self):
        mobileinput = self.driver.find_element_by_xpath('//*[@id="mobile"]')
        mobileinput.send_keys("13511047925")
        # clickyzm = self.driver.find_element_by_xpath('//*[@id="refreshCode"]')
        # clickyzm.click()
        # time.sleep(2)
        yzm = self.driver.find_element_by_xpath('//*[@id="code"]')
        yzm.send_keys("1709")
        loginpwd = self.driver.find_element_by_xpath('//*[@id="loginWithPwdBtn"]')
        loginpwd.click()
        time.sleep(3)


         # Switch 切换当前的上下文
        #print self.driver.contexts
        self.driver.switch_to.context('NATIVE_APP')
        #print self.driver.current_context


        #登陆手势密码
        self.driver.find_element_by_id("textView").click()
        time.sleep(3)

        # Switch 切换当前的上下文
        #print self.driver.contexts
        self.driver.switch_to.context('WEBVIEW_0')
        #print self.driver.current_context

        #车险投保
        submitOrder = self.driver.find_element_by_xpath('//*[@id="byInsurance"]/span')
        submitOrder.click()
        time.sleep(2)

        # Switch 切换当前的上下文
        #print self.driver.contexts
        self.driver.switch_to.context('WEBVIEW_0')
        #print self.driver.current_context

        #证件识别
        self.driver.find_element_by_xpath('//*[@id="nextStep"]').click()
        time.sleep(2)

        #填写基本信息
        self.driver.find_element_by_xpath('//*[@id="indexMain"]/ul/li[2]/div').click()
        self.driver.find_element_by_xpath('//*[@id="buyNow"]').click()
        time.sleep(5)

        # Switch 切换当前的上下文
        #print self.driver.contexts
        self.driver.switch_to.context('WEBVIEW_0')
        #print self.driver.current_context

        # 录入报价信息
        rackNo = self.driver.find_element_by_xpath('//*[@id="rackNo"]')
        rackNo.send_keys("LSLJDFEREDLFJ3434")
        engineNo = self.driver.find_element_by_xpath('//*[@id="engineNo"]')
        engineNo.send_keys("866541")
        brandModel = self.driver.find_element_by_xpath('//*[@id="brandModel"]')
        brandModel.send_keys("SVW71810")
        invoiceNo = self.driver.find_element_by_xpath('//*[@id="invoiceNo"]')
        invoiceNo.send_keys("lfjdlfjdl")
        invoiceDate = self.driver.find_element_by_xpath('//*[@id="invoiceDate"]')
        invoiceDate.click()
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div[3]/div[1]/div').click()
        carOwner = self.driver.find_element_by_xpath('//*[@id="carOwner"]')
        carOwner.send_keys("zhaoqian")
        certNo = self.driver.find_element_by_xpath('//*[@id="certiNo"]')
        certNo.send_keys("340104197408011311")
        nextDo = self.driver.find_element_by_xpath('//*[@id="nextDo"]')
        nextDo.click()
        time.sleep(5)


        # Switch 切换当前的上下文
        #print self.driver.contexts
        self.driver.switch_to.context('WEBVIEW_0')
        #print self.driver.current_context

        #确认车型
        captypelist = self.driver.find_element_by_xpath('//*[@id="carTypeList"]/li[1]/h4')
        captypelist.click()
        time.sleep(10)

        #确认车型信息
        nextBtn = self.driver.find_element_by_xpath('//*[@id="nextBtn"]')
        nextBtn.click()
        time.sleep(5)

        #选择报价公司
        Pingan = self.driver.find_element_by_xpath('//*[@id="p_0"]')
        Pingan.click()
        nextBtn1 = self.driver.find_element_by_xpath('//*[@id="nextBtn"]')
        nextBtn1.click()
        time.sleep(5)

        #车险自定义
        chesunxian = self.driver.find_element_by_xpath('//*[@id="insuranceOptions"]/li[1]/div/div')
        chesunxian.click()
        daoqiangxian = self.driver.find_element_by_xpath('//*[@id="insuranceOptions"]/li[2]/div/div')
        daoqiangxian.click()
        sijixian = self.driver.find_element_by_xpath('//*[@id="insuranceOptions"]/li[3]/div/div')
        sijixian.click()
        chengkexian = self.driver.find_element_by_xpath('//*[@id="insuranceOptions"]/li[4]/div/div')
        chengkexian.click()
        sanzhexian = self.driver.find_element_by_xpath('//*[@id="insuranceOptions"]/li[5]/div')
        sanzhexian.click()
        selectSanzhexian = self.driver.find_element_by_xpath('//*[@id="RC0005Select"]')
        selectSanzhexian.click()
        insureSanzhexian = self.driver.find_element_by_xpath('//*[@id="wSelectWrap"]/div/ul/li[6]')
        insureSanzhexian.click()
        refreshPrice = self.driver.find_element_by_xpath('//*[@id="refreshPriceLi"]')
        refreshPrice.click()
        time.sleep(10)
        insureBuy = self.driver.find_element_by_xpath('//*[@id="buyOrNext"]')
        insureBuy.click()
        time.sleep(25)

        #录入补充信息
        regMobile = self.driver.find_element_by_xpath('//*[@id="regMobile"]')
        regMobile.click()
        regMobile.send_keys("15210036967")
        address = self.driver.find_element_by_xpath('//*[@id="address"]')
        address.click()
        address.send_keys("dlfjdlfjdfjdlldfjldfjldjfldflfj")
        emailItem = self.driver.find_element_by_xpath('//*[@id="emailItem"]/input')
        emailItem.click()
        emailItem.send_keys("2735643625@qq.com")
        insuredIssuer = self.driver.find_element_by_xpath('//*[@id="insuredIssuer"]')
        insuredIssuer.click()
        insuredIssuer.send_keys("beijinggonganju")
        insuredCertiStartDate = self.driver.find_element_by_xpath('//*[@id="insuredCertiStartDate"]')
        insuredCertiStartDate.click()
        CertiStartDate = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[3]/div[1]/div')
        CertiStartDate.click()
        insuredCertiEndDate = self.driver.find_element_by_xpath('//*[@id="insuredCertiEndDate"]')
        insuredCertiEndDate.click()
        CertiEndDate = self.driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[3]/div[1]/div')
        CertiEndDate.click()
        agreeBtn = self.driver.find_element_by_xpath('//*[@id="agreeBtn"]')
        agreeBtn.click()

        #原生型
        #print self.driver.contexts
        self.driver.switch_to.context('NATIVE_APP')
        #print self.driver.current_context

        #请签名
        tablet_ok = self.driver.find_element_by_id('tablet_ok')
        tablet_ok.click()

        self.driver.switch_to.context('WEBVIEW_0')

        #提交订单
        submitOrder = self.driver.find_element_by_xpath('//*[@id="submitOrder"]')
        submitOrder.click()
        time.sleep(5)


    #释放实例, 释放资源
    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    MyTestCase = MyTestCase(3)
    MyTestCase.run()
    unittest.main()






















