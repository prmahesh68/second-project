from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class Regitration:
    click_Signin_xpath="//a[@class='login']"
    inputbox_email_xpath="//input[@id='email_create']"
    click_createaccount="//form[@id='create-account_form']//span[1]"
    RadiobuttonMr_xpath="//input[@id='id_gender1']"
    RadiobuttonMrs_xpath="//input[@id='id_gender2']"
    textbox_firstname_xpath="/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div[1]/div[2]/input[1]"
    # textbox_firstname_name="customer_firstname"
    textbox_lastname_xpath="//input[@id='customer_lastname']"
    textbox_password_xpath="//input[@id='passwd']"
    select_DOB_days_name="days"
    select_DOB_months_name="months"
    select_DOB_years_name="years"
    tick_newsletter_xpath="//input[@id='newsletter']"
    tick_specialoffer_xpath="//input[@id='optin']"
    textbox_addressfirstname_name="firstname"
    textbox_addresslastname_name="lastname"
    textbox_company_name="company"
    textbox_address1_name="address1"
    textbox_address2_name="address2"
    textbox_city_name="city"
    select_state_name="id_state"
    select_county_name="id_country"
    intbox_zipcode_name="postcode"
    textbox_addtionalinfo_name="other"
    intbox_homeph_name="phone"
    intbox_mobileph_name="phone_mobile"
    textbox_alias_name="alias"
    click_register_xpath="//span[contains(text(),'Register')]"


    def __init__(self,Openbrowser):
        self.Openbrowser=Openbrowser
        #self.useform = self.Openbrowser.find_element_by_tag_name("form")
    def setuseremail(self,useremail):
       self.Openbrowser.find_element_by_xpath(self.inputbox_email_xpath).send_keys(useremail)
    def signin(self):
       self.Openbrowser.find_element_by_xpath(self.click_Signin_xpath).click()
    def createaccount(self):
        self.Openbrowser.find_element_by_xpath(self.click_createaccount).click()
    def selectsalu(self,sal):
        if sal=="Mr":
            self.Openbrowser.find_element_by_xpath(self.RadiobuttonMr_xpath).click()
        elif sal=="Mrs":
            self.Openbrowser.find_element_by_xpath(self.RadiobuttonMrs_xpath)
        else:
            self.Openbrowser.find_element_by_xpath(self.RadiobuttonMr_xpath).click()
    def inputfirstname(self,firstname):
        self.Openbrowser.find_element_by_xpath(self.textbox_firstname_xpath).send_keys(firstname)
    def inputlastname(self,lastname):
        self.Openbrowser.find_element_by_xpath(self.textbox_lastname_xpath).send_keys(lastname)
    def inputpassword(self,password):
        self.Openbrowser.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)
    def selectDOBdays(self,days):
        self.Openbrowser.find_element_by_name(self.select_DOB_days_name).send_keys(days)
    def selectDOBmonth(self, months):
        self.Openbrowser.find_element_by_name(self.select_DOB_months_name).send_keys(months)
    def selectDOByear(self, year):
        self.Openbrowser.find_element_by_name(self.select_DOB_years_name).send_keys(year)
    def inputcompany(self,company):
        self.Openbrowser.find_element_by_name(self.textbox_company_name).send_keys(company)
    def inputhomephone (self,homeph):
        self.Openbrowser.find_element_by_name(self.intbox_homeph_name).send_keys(homeph)
    def inputmobileph (self,mobileph):
        self.Openbrowser.find_element_by_name(self.intbox_mobileph_name).send_keys(mobileph)
    def inputalias (self,alias):
        self.Openbrowser.find_element_by_name(self.textbox_alias_name).send_keys(alias)
    def ticknewsletter(self,newsletter):
        if newsletter == "yes":
            self.Openbrowser.find_element_by_xpath(self.tick_newsletter_xpath).click()
    def tickspecialoffer(self,offers):
        if offers == "yes":
            self.Openbrowser.find_element_by_xpath(self.tick_specialoffer_xpath).click()
    def inputaddfirstname(self,firstname):
        self.Openbrowser.find_element_by_name(self.textbox_addressfirstname_name).send_keys(firstname)
    def inputaddlastname(self,lastname):
        self.Openbrowser.find_element_by_name(self.textbox_addresslastname_name).send_keys(lastname)
    def inputaddess1(self,address1):
        self.Openbrowser.find_element_by_name(self.textbox_address1_name).send_keys(address1)
    def inputaddress2(self,address2):
        self.Openbrowser.find_element_by_name(self.textbox_address2_name).send_keys(address2)
    def inputcity(self,city):
        self.Openbrowser.find_element_by_name(self.textbox_city_name).send_keys(city)
    def selectstate(self,state):
        self.Openbrowser.find_element_by_name(self.select_state_name).send_keys(state)
    def inputzipcode(self,zip):
        self.Openbrowser.find_element_by_name(self.intbox_zipcode_name).send_keys(zip)
    def inputaddinfo(self,addinfo):
        self.Openbrowser.find_element_by_name(self.textbox_addtionalinfo_name).send_keys(addinfo)
    def clickregister(self):
        self.Openbrowser.find_element_by_xpath(self.click_register_xpath).click()
    def accountloginverify(self):
        self.msg = self.Openbrowser.find_element_by_tag_name("body").text
        if "Welcome to your account. Here you can manage all of your personal information and orders." in self.msg:
            return True
        else:
            return False
class Loginclass:
    click_Signin_xpath="//a[@class='login']"
    input_emailaddress_name= "email"
    input_password_name="passwd"
    click_submit_name="SubmitLogin"

    def __init__(self,Openbrowser):
        self.Openbrowser=Openbrowser
    def signin(self):
       self.Openbrowser.find_element_by_xpath(self.click_Signin_xpath).click()
    def inputuseremail(self,useremail):
       self.Openbrowser.find_element_by_name(self.input_emailaddress_name).send_keys(useremail)
    def inputpassword(self,password):
        self.Openbrowser.find_element_by_name(self.input_password_name).send_keys(password)
    def clicksubmit(self):
        self.Openbrowser.find_element_by_name(self.click_submit_name).click()

    def accountloginverify(self):
        self.msg = self.Openbrowser.find_element_by_tag_name("body").text
        if "Welcome to your account. Here you can manage all of your personal information and orders." in self.msg:
            return True
        else:
            return False

class Shopping:
    click_women_menu_xpath = "//*[@id='block_top_menu']/ul/li[1]/a"
    click_dress_menu_xpath ="//*[@id='subcategories']/ul/li[2]/div[1]/a"
    Hover_over_dress ="//*[@id='center_column']/ul/li[2]"
    click_addtocart_link="//*[@id='center_column']/ul/li[2]/div/div[2]/div[2]/a[1]/span"
    click_proceedtocheckout_link = "//*[@id='layer_cart']/div[1]/div[2]/div[4]/a"
    check_instock_label_xpath ="//*[@id='product_4_16_0_288748']/td[3]/span"
    check_totalprice_id="total_price"
    click_ordersummarycheckout_xpath="//*[@id='center_column']/p[2]/a[1]"
    click_addresscheckout_name="processAddress"
    click_carriercheckout_name="processCarrier"
    click_agreecarrierterm_name="cgv"
    click_processpaymentbywire_xpath="//*[@id='HOOK_PAYMENT']/div[1]/div/p/a"
    click_confirorder="//*[@id='cart_navigation']/button"
    msg ="Your order on My Store is complete"
    click_backtoorder_xpath="//*[@id='center_column']/p/a"
    msg1="Your order on My Store is complete."
    test1="Do not forget to insert your order reference SVSZBITMA in the subject of your bank wire."
    table_id_id="order-list"

    def __init__(self, Openbrowser):
        self.Openbrowser = Openbrowser
    def womenmenu(self):
        self.Openbrowser.find_element_by_xpath(self.click_women_menu_xpath).click()
    def dressmenu(self):
        self.Openbrowser.find_element_by_xpath(self.click_dress_menu_xpath).click()
    def addtocart(self):
        self.Openbrowser.find_element_by_xpath(self.Hover_over_dress).click()
        time.sleep(3)
        self.Openbrowser.find_element_by_xpath(self.click_addtocart_link).click()
        # dress=self.Openbrowser.find_element_by_xpath(self.Hover_over_dress)
        # add =self.Openbrowser.find_element_by_xpath(self.click_addtocard_link)
        # takeaction = ActionChains(self.Openbrowser)
        # takeaction.move_to_element(dress).move_to_element(add).click().perform()
        # self.Openbrowser.find_element_by_xpath(self.click_addtocard_link).click()
    def checkout1(self):
        self.Openbrowser.find_element_by_xpath(self.click_proceedtocheckout_link).click()
    def clickordersummary(self):
        self.Openbrowser.find_element_by_xpath(self.click_ordersummarycheckout_xpath).click()
    def clickaddresscheckout(self):
        self.Openbrowser.find_element_by_name(self.click_addresscheckout_name).click()
    def agreeterms(self):
        self.Openbrowser.find_element_by_name(self.click_agreecarrierterm_name).click()
    def carriercheckout(self):
        self.Openbrowser.find_element_by_name(self.click_carriercheckout_name).click()
    def processpayment(self):
        self.Openbrowser.find_element_by_xpath(self.click_processpaymentbywire_xpath).click()
    def Iconfirmorder(self):
        self.Openbrowser.find_element_by_xpath(self.click_confirorder).click()
    def orderconfirmverify(self):
        self.msg = self.Openbrowser.find_element_by_tag_name("body").text
        if "Your order on My Store is complete" in self.msg:
            return True
        else:
            return False
    def backtoorder(self):
        self.Openbrowser.find_element_by_xpath(self.click_backtoorder_xpath).click()
    def tableread(self):
        elements = WebDriverWait(self.Openbrowser, 10).until(EC.presence_of_all_elements_located(
            (By.XPATH, "//table[@class = 'dadosAgencia']//tr")))
