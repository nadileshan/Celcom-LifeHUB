from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime
import folder_mkr
from folder_mkr import path
from spinner import wait_for_spinner
from MyAcc import check_my_account
from billCheck import check_billing
from payment import make_payment
from usage import check_usage
from support import run_services
from service import run_support_section

# set up webdriver
driver = webdriver.Chrome()

# set up chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")

# navigate to lifeHUB
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.celcom.com.my/life-hub")
time.sleep(10)

# enter username and password
wait = WebDriverWait(driver, 30)
username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-0"]')))
username_input.send_keys("300303030311")
time.sleep(5)


# click login button
login_button = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div/app-base/div/div/app-login-form/div/div[1]/div/div[2]/form/app-form-button/div/div/button')
login_button.click()
time.sleep(80)
# !important Manualy add OTP 

# take a screenshot and save it to a file

# wait for dashboard to load
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="sidebar-padding"]/app-sidebar-new/section/div[2]/nav/div[1]')))
time.sleep(5)
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# take a screenshot of login and save it with the timestamp
screenshot_name = f'Overview_1/1_{timestamp}.png'
driver.save_screenshot(f"{path}/{screenshot_name}")
print('Overview Page loading')
time.sleep(10)
#check Myaccount
check_my_account(driver, timestamp, path)


# Billing
check_billing(driver)
time.sleep(5)
#reset
home = driver.find_element(By.XPATH,"/html/body/app-root/div/div/div/div/div[2]/app-sidebar-new/section/div[2]/div/nav/div[1]/a")
time.sleep(5)
home.click()
time.sleep(5)

#check Payment
make_payment(driver, timestamp, path)
time.sleep(5)
#USAGE

check_usage(driver, timestamp, path)
time.sleep(5)

# Services
run_services(driver, path, timestamp)
time.sleep(5)

# SUPPORT

run_support_section(driver, path, timestamp)

# close the browser
driver.quit()

# output success message
print("LifeHUB sanity test completed successfully.")