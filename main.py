from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

my_driver = webdriver.Chrome(executable_path='/Users/noy/Downloads/chromedriver')
my_driver.get(url='file:///Users/noy/Downloads/tip_calc/index.html')
# my_driver.get(url='https://ynet.co.il')

# for i in range(3):
#    sleep(2)
#    my_driver.refresh()

my_driver.find_element_by_id("billamt").send_keys("100")
my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[2]').click()
my_driver.find_element_by_id("peopleamt").send_keys("5")
my_driver.find_element_by_id("calculate").click()
actual = my_driver.find_element_by_id("tip").text
print(actual)
expected = "6.00"
assert expected == actual

# if actual == "6.00":
#     print("It works")
# else:
#     print("Not work")
