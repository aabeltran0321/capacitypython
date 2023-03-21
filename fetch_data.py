from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://openstat.psa.gov.ph/PXWeb/pxweb/en/DB/DB__2G__MNFG__MISSI__2000/0032G4CMCU0.px/?rxid=5f70fb2a-1d3e-4269-9454-b1098257e294")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()