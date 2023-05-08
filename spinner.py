from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_spinner(driver):
    spinner_selector = "/html/body/app-root/div[2]/app-loader/div/div/div"
    # Wait for the spinner to appear
    spinner = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, spinner_selector))
    )

    # Wait for the spinner to disappear
    WebDriverWait(driver, 20).until_not(
        EC.visibility_of_element_located((By.XPATH, spinner_selector))
    )

    # /html/body/app-root/div[2]/app-loader/div/div
    # /html/body/app-root/div[2]/app-loader/div/div/div