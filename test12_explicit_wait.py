from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

wait = WebDriverWait(browser,12).until(
    EC.text_to_be_present_in_element((By.ID,"price"),"100"))
button=browser.find_element_by_tag_name("button")
button.click()

elem=browser.find_element_by_id("input_value")
res_elem= elem.text

def calc(x):
    return(str(math.log(abs(12*math.sin(int(x))))))
    
res= calc(res_elem)
elem_text=browser.find_element_by_id("answer")
elem_text.send_keys(res)

button= browser.find_element_by_css_selector("[type='submit']")
button.click()
