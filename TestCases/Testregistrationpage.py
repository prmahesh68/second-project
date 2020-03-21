from Utilites.readconfig1file import Getinfoconfig
from Objectref.Newuserregistration import Regitration
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from  Utilites.Randongenerator import RanGen
from Utilites.CustomLogger import Logsetup
import time

class Test_practice:
    Weburl = Getinfoconfig.wedurlget()
    # emailaddress = Getinfoconfig.usernameget()
    emailaddress = RanGen.randomgen() + "@gmail.com"
    firstname=Getinfoconfig.firstnameget()
    lastname=Getinfoconfig.lastnameget()
    password = Getinfoconfig.passwordget()
    company = Getinfoconfig.companyget()
    address1 = Getinfoconfig.address1get()
    address2 = Getinfoconfig.address2get()
    city = Getinfoconfig.cityget()
    state = Getinfoconfig.stateget()
    country = Getinfoconfig.companyget()
    zipcode = Getinfoconfig.zipcodeget()
    dobdays = Getinfoconfig.dobdaysget()
    dobmonth = Getinfoconfig.dobmonthsget()
    dobyear = Getinfoconfig.dobyearsget()
    homeph = Getinfoconfig.homephget()
    mobileph = Getinfoconfig.mobilephget()
    alias = Getinfoconfig.aliasget()
    logger = Logsetup.getlogreg()

    def testpractice(self,web):
        self.Openbrowser= web
        self.Openbrowser.get(self.Weburl)
        self.logger.info("webpage is opening")
        self.Openbrowser.maximize_window()
        regobject=Regitration(self.Openbrowser)
        regobject.signin()
        regobject.setuseremail(self.emailaddress)
        regobject.createaccount()
        time.sleep(15)
        self.logger.info("start input data for registration")
        regobject.inputfirstname(self.firstname)
        regobject.inputlastname(self.lastname)
        regobject.inputpassword(self.password)
        regobject.selectsalu("Mr")
        regobject.selectDOBdays(self.dobdays)
        regobject.selectDOBmonth(self.dobmonth)
        regobject.selectDOByear(self.dobyear)
        regobject.inputcompany(self.company)
        regobject.inputaddess1(self.address1)
        regobject.inputaddress2(self.address2)
        regobject.inputcity(self.city)
        regobject.selectstate(self.state)
        regobject.inputzipcode(self.zipcode)
        regobject.inputhomephone(self.homeph)
        regobject.inputmobileph(self.mobileph)
        regobject.inputaddinfo("testing registration")
        regobject.inputalias(self.alias)
        regobject.clickregister()
        time.sleep(10)
        sucess= regobject.accountloginverify()
        print(sucess)
        if sucess == True:
            self.logger.info("account creation sucessful")
            print (self.emailaddress,"  account created sucessfully")
            assert True
        elif sucess == False:
            self.logger.info("account creation not sucessful")
            print(self.emailaddress, "   account not created")
            assert False














