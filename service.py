import time
from selenium.webdriver.common.by import By

def run_support_section(driver, path, timestamp):
    try:
        support = driver.find_element(By.XPATH,'//*[@id="side_menu_anchor_6"]')
        support.click()
        time.sleep(10)

        PUKnum = driver.find_element(By.XPATH,'//*[@id="Support_0"]')
        PUKnum.click()
        time.sleep(10)

        PUKnumCheck = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div[3]/app-base/div/div/app-puk-listing/div[2]/div/div[2]/div[1]')
        PUKnumCheck.click()
        time.sleep(10)

        screenshot_name = f'screenshot_PUKnum_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(10)


        TrackReport = driver.find_element(By.XPATH,'//*[@id="Support_1"]')
        TrackReport.click()
        time.sleep(10)

        screenshot_name = f'screenshot_TrackReport_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(10)

        trackTransaction = driver.find_element(By.XPATH,'//*[@id="Support_2"]')
        trackTransaction.click()
        time.sleep(5)
        screenshot_name = f'screenshot_TrackTransactions_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(10)
        
        print("Support section ran successfully.")
    except Exception as e:
        print(f"Support section failed with error: {e}")
