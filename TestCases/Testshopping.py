from selenium import webdriver
from Utilites.readconfig1file import Getinfoconfig
from Objectref.Newuserregistration import Loginclass
from Objectref.Newuserregistration import Shopping
from Utilites.CustomLogger import Logsetup
import time

class Testshopping:
    Weburl = Getinfoconfig.wedurlget()
    emailaddress = Getinfoconfig.usernameget()
    password = Getinfoconfig.passwordget()
    logger = Logsetup.getlogaddlogin()

    def testshoppage(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.Weburl)
        self.logger.info("Webpage Opening")
        self.Openbrowser.maximize_window()
        loginobject = Loginclass(self.Openbrowser)
        loginobject.signin()
        time.sleep(5)
        loginobject.inputuseremail(self.emailaddress)
        loginobject.inputpassword(self.password)
        loginobject.clicksubmit()
        time.sleep(5)
        shopobject= Shopping(self.Openbrowser)
        shopobject.womenmenu()
        time.sleep(5)
        shopobject.dressmenu()
        time.sleep(5)
        shopobject.addtocart()
        time.sleep(5)
        shopobject.checkout1()
        time.sleep(5)
        shopobject.clickordersummary()
        time.sleep(5)
        shopobject.clickaddresscheckout()
        time.sleep(5)
        shopobject.agreeterms()
        time.sleep(5)
        shopobject.carriercheckout()
        time.sleep(5)
        shopobject.processpayment()
        time.sleep(5)
        shopobject.Iconfirmorder()
        time.sleep(5)
        sucess = shopobject.orderconfirmverify()
        if sucess == True:
            print ("Order placed sucessfully")
            assert True
        elif sucess == False:
            print ("recheck order again")
            assert False
        # bodymessage = self.Openbrowser.find_element_by_tag_name("body").text
        # print(bodymessage)
        # bodymessage = str(bodymessage)
        # textlist = bodymessage.spilt()
        # print(textlist)
