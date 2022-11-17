from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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
driver.find_element(By.ID, "flipboard.app:id/topic_picker_continue_button").click()

# Using UIAutomator(Java Function)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Continue")').click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Skip for Now")').click()

sl.sleep(2)

ScrollUtil.swipeUp(4, driver)
sl.sleep(2)

ScrollUtil.swipeDown(4, driver)
sl.sleep(2)


ScrollUtil.swipeLeft(2, driver)
sl.sleep(2)

ScrollUtil.swipeRight(2, driver)
sl.sleep(2)