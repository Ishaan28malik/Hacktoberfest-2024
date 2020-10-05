from selenium import webdriver

pnum = input("Enter phone number:")
amt = int(input("How many times you want to send OTP:"))


# 1> download google chrome webdriver


browser = webdriver.Chrome('D:\\Super Brain\\Automation with python\\Chrome Driver\\chromedriver.exe')

browser.get('https://www.amazon.in/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&switch_account=')

phone = browser.find_element_by_id("ap_email")
phone.send_keys(pnum)

cont = browser.find_element_by_id("continue")
cont.click()

sendOTP = browser.find_element_by_id("continue")
sendOTP.click()

n = amt-1

for i in range(n):
    #click on resend OTP
    r = browser.find_element_by_link_text("Resend OTP")
    r.click()

browser.quit()