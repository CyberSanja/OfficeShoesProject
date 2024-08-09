from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def load_office_shoes(url):

    driver = webdriver.Chrome(service=Service("C:/Windows/chromedriver-win64/chromedriver.exe"))
    driver.maximize_window()
    driver.get(url)
    return driver


def test_closing_promo_code_header_message():

    driver = load_office_shoes("https://www.officeshoes.rs/")
    sleep(1)
    driver.find_element(By.CLASS_NAME, "promo_code_header_message_close").click()
    sleep(2)

    assert driver.save_screenshot("promo_code_header_closed.png")

    close_chrome(driver)


def test_search_input():

    driver = load_office_shoes("https://www.officeshoes.rs/")
    sleep(1)
    driver.find_element(By.NAME, "q").send_keys("vans")
    sleep(2)
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    sleep(2)

    assert driver.save_screenshot("vans_search_results.png")
    sleep(1)

    close_chrome(driver)


def test_display_item_info():

    driver = load_office_shoes("https://www.officeshoes.rs/")
    sleep(1)
    driver.find_element(By.NAME, "q").send_keys("vans")
    sleep(1)
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "img[alt='Vans Majica Tagged SS']").click()
    sleep(1)

    assert driver.current_url == "https://www.officeshoes.rs/accessory-vans-majica-tagged-ss/84460"
    sleep(2)

    close_chrome(driver)



def close_chrome(driver):

    driver.minimize_window()
    driver.quit()