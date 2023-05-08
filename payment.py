import time
from selenium.webdriver.common.by import By


def make_payment(driver, timestamp, path):
    try:
        payment = driver.find_element(By.XPATH,'//*[@id="side_menu_anchor_3"]')
        payment.click()
        time.sleep(5)

        paybill = driver.find_element(By.XPATH,'//*[@id="Payment_0"]')
        paybill.click()
        time.sleep(10)
        paybillcheck = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div[1]/div/div[3]/app-base/div/div/app-dynamic-table/div[2]/div[1]/table/tbody/tr[1]/td[3]/mat-checkbox/label/span[1]')
        paybillcheck.click()
        time.sleep(5)
        payvalue = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div[1]/div/div[3]/app-base/div/div/app-dynamic-table/div[2]/div[1]/table/tbody/tr[1]/td[3]/input')

        payvalue.clear()
        payvalue.send_keys("10")

        paynext = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div[2]/div/div[2]/app-button/div/div/button')
        paynext.click()
        time.sleep(5)

        paybillOnlineBank = driver.find_element(By.XPATH,'//*[@id="mat-radio-2"]')
        paybillOnlineBank.click()
        time.sleep(5)
        bankdir = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div/app-base/div/div/app-dynamic-form/div/div/form/app-form-button/div/div/button')
        bankdir.click()
        time.sleep(10)

        screenshot_name = f'screenshot_Bank_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(5)

        cancelPay = driver.find_element(By.XPATH,'/html/body/div[2]/div/span[1]/a')
        cancelPay.click()
        time.sleep(10)

        HisNRec = driver.find_element(By.XPATH,'//*[@id="Payment_1"]')
        HisNRec.click()
        time.sleep(5)

        screenshot_name = f'screenshot_History&Recp_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(5)

        promiseTOpay = driver.find_element(By.XPATH,'//*[@id="Payment_2"]')
        promiseTOpay.click()
        time.sleep(10)

        clickMobNumber = driver.find_element(By.XPATH,'//*[@id="mat-select-0"]/div')
        clickMobNumber.click()
        time.sleep(5)
        MobOption = driver.find_element(By.XPATH,'//*[@id="mat-option-0"]')
        MobOption.click()
        time.sleep(5)

        CheckEntitle = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div[3]/app-base/div/div/app-promise-to-pay/form/div/app-button/div/div/button')
        CheckEntitle.click()
        time.sleep(5)
        screenshot_name = f'screenshot_Promisetopay_{timestamp}.png'
        driver.save_screenshot(f"{path}/{screenshot_name}")
        time.sleep(2)

        backtoMain = driver.find_element(By.XPATH,'/html/body/app-root/div/div/div/div/div[3]/app-base/div/div/app-promise-to-pay/div/app-dynamic-error-card/div/div/div/div[2]/div[2]/div/div[1]/app-button/div/div/button')
        backtoMain.click()
        time.sleep(5)
        print("payment Ok")
    except:
        print("payment failed")
