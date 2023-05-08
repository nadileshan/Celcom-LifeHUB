import time
from selenium.webdriver.common.by import By

def run_services(driver, path, timestamp):
    try:
        services = driver.find_element(By.XPATH,'//*[@id="side_menu_anchor_5"]')
        services.click()
        time.sleep(5)
        screenshot_name = f'screenshot_services_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(2)

        # simreplacement
        simReplace = driver.find_element(By.XPATH,'//*[@id="Services_0"]')
        simReplace.click()
        time.sleep(5)
        screenshot_name = f'screenshot_Sim_Replacement_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(2)

        changeCredit = driver.find_element(By.XPATH,'//*[@id="Services_2"]')
        changeCredit.click()
        time.sleep(5)
        screenshot_name = f'screenshot_temperaryCredit_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(10)

        permenenrtCredit = driver.find_element(By.CLASS_NAME, 'mat-ripple.mat-tab-label.mat-focus-indicator.ng-star-inserted')
        driver.execute_script("arguments[0].click();", permenenrtCredit)
        time.sleep(5)
        screenshot_name = f'screenshot_permenenrtCredit_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(5)

        autoBiling = driver.find_element(By.XPATH,'//*[@id="Services_3"]')
        autoBiling.click()
        time.sleep(5)
        screenshot_name = f'screenshot_autoBiling_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(5)

        addOnes = driver.find_element(By.XPATH,'//*[@id="Services_4"]')
        addOnes.click()
        time.sleep(5)

        numClick = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div[3]/app-base/div/div/app-add-on-list/div/div[2]/div[2]/div[1]')
        numClick.click()
        time.sleep(10)

        intPackage = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div[3]/app-base/div/div/app-dynamic-tabs/div[3]/app-add-on-tab-details-card/div/div[1]')
        intPackage.click()
        time.sleep(10)

        screenshot_name = f'screenshot_Int_Packeage_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(10)

        backIntAddon = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div[1]/div/div/app-base/div/div/app-add-on-preprocess/div/a/h2/img')
        backIntAddon.click()
        time.sleep(10)

        print("Service Ok")
    
    except Exception as e:
        print(f"Service failed: {str(e)}")
