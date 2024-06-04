import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    #Create object for manage browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    #open page
    driver.get("https://github.com/login")


    #find place for input
    login_elem = driver.find_element(By.ID, "login_field")



    #send info
    login_elem.send_keys("sergiibutenko@gmail.com")

    pass_elem= driver.find_element(By.ID,"password")
    pass_elem.send_keys("12345679")


    btn_elem = driver.find_element(By.NAME, "commit")
    btn_elem.click()


    assert driver.title == "Sign in to GitHub · GitHub"


    time.sleep(4)

    #close page
    driver.close()
