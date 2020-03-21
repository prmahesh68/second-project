from selenium import webdriver
from Utilites.readconfig1file import Getinfoconfig
from Objectref.Newuserregistration import Loginclass
from Utilites.CustomLogger import Logsetup
import time

class TestLogin:
    Weburl = Getinfoconfig.wedurlget()
    emailaddress = Getinfoconfig.usernameget()
    password = Getinfoconfig.passwordget()
    logger = Logsetup.getlogaddlogin()

    def testloginpage(self,web):
        self.Openbrowser = web
        self.Openbrowser.get(self.Weburl)
        self.logger.info("Webpage Opening")
        self.Openbrowser.maximize_window()
        regobject = Loginclass(self.Openbrowser)
        regobject.signin()
        time.sleep(10)
        regobject.inputuseremail(self.emailaddress)
        regobject.inputpassword(self.password)
        regobject.clicksubmit()
        time.sleep(10)
        sucess=regobject.accountloginverify()
        if sucess == True:
            print("Login Sucessful")
            self.logger.info("Login sucessful")
            assert True
        elif sucess == False:
            print ("Login not sucessful")
            self.logger.info("Login unsucessful")
            assert False
