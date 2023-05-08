import time
from selenium.webdriver.common.by import By

def check_usage(driver, timestamp, path):
    usage = driver.find_element(By.XPATH,'//*[@id="side_menu_anchor_4"]')
    usage.click()
    time.sleep(5)

    Celno = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div[3]/app-base/div/div/app-auto-billing-list/div/div/div[2]/div/div[2]/div[1]')
    Celno.click()
    time.sleep(10)

    local = driver.find_element(By.XPATH,'//*[@id="mat-tab-label-0-1"]')
    local.click()
    time.sleep(10)
    screenshot_name = f'screenshot_Local_{timestamp}.png'
    driver.save_screenshot(f"{path}/{screenshot_name}")
    time.sleep(5)

    charges = driver.find_element(By.XPATH,'//*[@id="mat-tab-label-0-0"]')
    charges.click()
    time.sleep(10)
    screenshot_name = f'screenshot_ChargesTAB_{timestamp}.png'
    driver.save_screenshot(f"{path}/{screenshot_name}")
    time.sleep(5)

    roming = driver.find_element(By.XPATH,'//*[@id="mat-tab-label-0-2"]')
    roming.click()
    time.sleep(10)
    screenshot_name = f'screenshot_roming_{timestamp}.png'
    driver.save_screenshot(f"{path}/{screenshot_name}")
    time.sleep(5)

    if 'usage' in driver.current_url:
        print("Usage OK")
    else:
        print("Usage failed")
