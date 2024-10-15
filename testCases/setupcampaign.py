import pytest
from pageobjects.Loginpage1 import Loginpage


class TestLogin:
    baseURL = "https://unified-uat.digit.org/workbench-ui/employee/user/login"
    username = "ADMINC"
    password = "eGov@123"
    country_name = "MBAZI HIGHLANDS"  # Replace with the actual country name if needed
    IRSCT_name = "IRS Campaign"  # Replace with the actual campaign name
    countrydrop = "Mozambique"
    provincedrop = "Cabo"
    districtdrop = "HIERARCHYTEST_MO_12_01_CABO DELGADO"
    APdrop = "HIERARCHYTEST_MO_12_01_01_PEMBA"
    

    def test_login(self, setup):
        driver = setup
        driver.get(self.baseURL)
        lp = Loginpage(driver)
        
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.setcountry(self.country_name)
        
        lp.dpp()
        lp.login()
        
        # Ensure successful login
        act_title = driver.title
        assert act_title == "DIGIT", f"Expected title 'DIGIT' but got '{act_title}'"
        
        # Navigate and perform actions on the next page
        lp.get_setup_campaign_element()
        lp.select_campaigntype_from_dropdown(self.IRSCT_name)
        lp.nextbuttonone()
        lp.set_unique_campaign_name()
        lp.submit_campaign()

        lp.countrydropdown(self.countrydrop)
        lp.provincedropdown(self.provincedrop)
        lp.BG1click()
        lp.BG2click()
        lp.districtdropdown(self.districtdrop)
        lp.BG1click()
        lp.APdropdown(self.APdrop)
        lp.submit_boundary1()
        lp.selectStartDate()
        lp.selectEndDate()
        lp.submit_dates1()
        lp.cycle1selectStartDate()
        lp.cycle1selectEndDate()
        lp.submit_dates1()
        lp.submit_dates1()
        lp.upload_Target_excel_file()
        lp.submit_dates1()
        lp.upload_Facility_excel_file()
        lp.submit_dates1()
        lp.upload_User_excel_file()
        lp.submit_dates1()
        lp.createcampaignsuccessfully()
       