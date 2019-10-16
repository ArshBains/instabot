from selenium import webdriver
import time

e_mail = input("Enter email: ")
full_name = input("Fullname: ")
user_name = input("Username: ")
pass_word = input("Password: ")
print("NOTE-Target account should be open")
target = input("Target account handle >> ")



# connect google chrome with chromedriver
options = webdriver.ChromeOptions()
options.binary_location = "F:\Google\Chrome\Application\chrome.exe"     # Replace this location with location of chrome.exe on your machine
chrome_driver_binary = "C:\Windows\chromedriver.exe"    # Replace this location with location of chromedriver.exe
driver = webdriver.Chrome(executable_path=chrome_driver_binary, chrome_options=options)

driver.get('https://www.instagram.com')
time.sleep(5)

# Grab css elements and send data to the input fields
email = driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(4) > div > label > input')
email.send_keys(e_mail)
fullname = driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(5) > div > label > input')
fullname.send_keys(full_name)
username = driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(6) > div > label > input')
username.send_keys(user_name)
password = driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(7) > div > label > input')
password.send_keys(pass_word)

# hit signup button
sign_up= driver.find_element_by_css_selector('#react-root > section > main > article > div.rgFsT > div:nth-child(1) > div > form > div:nth-child(8) > div > button')
sign_up.click()

time.sleep(5)
# pop genrated and click not now
notnow = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow.click()

# Search for account in search bar
searchbar = driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input')
searchbar.send_keys(target)
time.sleep(5)

# select first item in list
prof = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
prof.click()
time.sleep(5)


# check if already following if not then follow user
if driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').text == "Follow":
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').click()
time.sleep(5)

# Go to your profile and logout
driver.get('https://www.instagram.com/'+user_name)
setting_btn = driver.find_element_by_css_selector('#react-root > section > main > div > header > section > div.nZSzR > div > button > span')
setting_btn.click()
time.sleep(5)
logout = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > button:nth-child(8)')
logout.click()












