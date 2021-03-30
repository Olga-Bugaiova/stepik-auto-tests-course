from selenium import webdriver
import math,time
import os

link="http://suninjuly.github.io/alert_accept.html"
browser=webdriver.Chrome()
browser.get(link)

elem_button=browser.find_element_by_tag_name("button")
elem_button.click()

confirm=browser.switch_to.alert
confirm.accept()


elem_formula=browser.find_element_by_id("input_value")
data=elem_formula.text

def calc(x):
    return(str(math.log(abs(12*math.sin(int(x))))))
data_input=calc(data)

text_add=browser.find_element_by_id("answer")
text_add.send_keys(data_input)

button_submit=browser.find_element_by_tag_name('button')
button_submit.click()


