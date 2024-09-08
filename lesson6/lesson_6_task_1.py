from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options)

driver.implicitly_wait(20)
driver.get("http://www.uitestingplayground.com/ajax")

driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
print(driver.find_element(By.CSS_SELECTOR, "p.bg-success").text)

driver.quit()
