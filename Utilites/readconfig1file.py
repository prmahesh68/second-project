import configparser

config=configparser.ConfigParser()
config.read('Configfolder/config1.ini')


class Getinfoconfig:
    @staticmethod
    def wedurlget():
        Weburl=config.get("common info","Weburl")
        return  Weburl

    @staticmethod
    def usernameget():
        emailaddress = config.get("common info","emailaddress")
        return emailaddress

    @staticmethod
    def passwordget():
        password = config.get("common info", "password")
        return password

    @staticmethod
    def firstnameget():
        firstname = config.get("common info", "firstname")
        return firstname

    @staticmethod
    def lastnameget():
        lastname = config.get("common info", "lastname")
        return lastname

    @staticmethod
    def companyget():
        company = config.get("common info", "company")
        return company

    @staticmethod
    def address1get():
        address1 = config.get("common info", "address1")
        return address1

    @staticmethod
    def address2get():
        address2 = config.get("common info", "address1")
        return address2

    @staticmethod
    def cityget():
        city = config.get("common info", "address1")
        return city

    @staticmethod
    def stateget():
        state = config.get("common info", "state")
        return state

    @staticmethod
    def countryget():
        country = config.get("common info", "country")
        return country

    @staticmethod
    def zipcodeget():
        zipcode = config.get("common info", "zipcode")
        return zipcode

    @staticmethod
    def dobdaysget():
        DOB_days = config.get("common info", "DOB_days")
        return DOB_days

    @staticmethod
    def dobmonthsget():
        DOB_months = config.get("common info", "DOB_months")
        return DOB_months

    @staticmethod
    def dobyearsget():
        DOB_years = config.get("common info", "DOB_years")
        return DOB_years

    @staticmethod
    def homephget():
        Home_ph = config.get("common info", "Home_ph")
        return Home_ph

    @staticmethod
    def mobilephget():
        Mobile_ph = config.get("common info", "Mobile_ph")
        return Mobile_ph

    @staticmethod
    def aliasget():
        alias = config.get("common info", "alias")
        return alias