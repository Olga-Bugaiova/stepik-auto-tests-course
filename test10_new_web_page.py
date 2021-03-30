from selenium import webdriver
import math,time

browser=webdriver.Chrome()
link ="http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

elem_button=browser.find_element_by_tag_name("button")
elem_button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

elem=browser.find_element_by_id("input_value")
res_elem= elem.text

def cal(x):
    return(str(math.log(abs(12*math.sin(int(x))))))

res= cal(res_elem)
elem_text=browser.find_element_by_id("answer")
elem_text.send_keys(res)

button= browser.find_element_by_css_selector("button.btn")
button.click()
