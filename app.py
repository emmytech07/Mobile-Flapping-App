from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import By, AppiumBy
import time as sl
desired_caps = dict(
    deviceName='Andriod',
    platformName='Android',
    appPackage='flipboard.app',
    appActivity='flipboard.activities.LaunchActivityAlias',

)

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

driver.find_element(By.ID, "flipboard.app:id/first_launch_get_started_button").click()

driver.find_elements(By.ID, "flipboard.app:id/topic_picker_topic_row_topic_tag")[0].click()
driver.find_elements(By.ID, "flipboard.app:id/topic_picker_topic_row_topic_tag")[1].click()
driver.find_elements(By.ID, "flipboard.app:id/topic_picker_topic_row_topic_tag")[2].click()

