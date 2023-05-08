import time
from selenium.webdriver.common.by import By

def check_my_account(driver, timestamp, path):
    try:
        myAcc = driver.find_element(By.XPATH, '//*[@id="side_menu_anchor_1"]')
        myAcc.click()
        time.sleep(5)
        
        profile = driver.find_element(By.XPATH, '//*[@id="My Account_0"]')
        profile.click()
        time.sleep(10)

        screenshot_name = f'screenshot_profile_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        print("Profile OK")
        time.sleep(10)
        profile = driver.find_element(By.XPATH, '//*[@id="My Account_0"]')
        profile.click()
        time.sleep(5)
        screenshot_name = f'screenshot_profile_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
      

        billing = driver.find_element(By.XPATH, '//*[@id="My Account_1"]')
        billing.click()
        time.sleep(5)
        screenshot_name = f'screenshot_billing_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
       

        planANDcontrat = driver.find_element(By.XPATH, '//*[@id="My Account_2"]')
        planANDcontrat.click()
        time.sleep(5)
        screenshot_name = f'screenshot_planANDcontrat_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
       
        #reset
        home = driver.find_element(By.XPATH,"/html/body/app-root/div/div/div/div/div[2]/app-sidebar-new/section/div[2]/div/nav/div[1]/a")
        home.click()
        time.sleep(5)
        return "OK"
    except:
        print("None")
         #reset
        home = driver.find_element(By.XPATH,"/html/body/app-root/div/div/div/div/div[2]/app-sidebar-new/section/div[2]/div/nav/div[1]/a")
        home.click()
        time.sleep(5)
