import time
from selenium.webdriver.common.by import By

def check_billing(driver):
    try:
        bill = driver.find_element(By.XPATH, '//*[@id="side_menu_anchor_2"]')
        bill.click()
        time.sleep(10)

        statment = driver.find_element(By.XPATH, '//*[@id="Billing_0"]')
        statment.click()
        time.sleep(10)
        clickStatement = driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/div[2]/app-sidebar-new/section/div[2]/div/nav/div[2]/div/a")
        driver.execute_script("arguments[0].click();", clickStatement)
        
        time.sleep(10)
        statmentMonth = driver.find_element(By.XPATH, "/html/body/app-root/div/div/div/div/div[3]/app-base/div/div/app-statement-list/div/div[2]/div[1]/div[1]/p[1]")

        driver.execute_script("arguments[0].click();", statmentMonth)
        time.sleep(25)
        statementCheckbox = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div[3]/app-base/div/div/app-statement-list-download/div/div[3]/div[2]/div[1]/div[2]/span/mat-checkbox')
        statementCheckbox.click()
        time.sleep(25)
        downloadStatement = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div[2]/div/div[2]/app-button/div/div/button')
        downloadStatement.click()
        time.sleep(10)
        

        year = driver.find_element(By.XPATH, '//*[@id="Billing_1"]')
        year.click()
        time.sleep(10)
        year1 = driver.find_element(By.XPATH, '//*[@id="mat-select-0"]/div')
        driver.execute_script("arguments[0].click();", year1)
        time.sleep(10)
        year2 = driver.find_element(By.XPATH, '//html/body/div[2]/div[2]/div/div/div/mat-option[1]')
        year2.click()
        time.sleep(10)
        yeardownload = driver.find_element(By.XPATH, '/html/body/app-root/div/div/div/div/div[3]/app-base/div/div/app-dynamic-form/div/div/form/app-form-button/div/div/button')
        yeardownload.click()
        time.sleep(10)

     
        print("Bill sanity OK")
    except:
        print("Bill failed")
        #reset
       
        
