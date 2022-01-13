from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from threading import Event

# setting up webdriver for chrome
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
#firefox_options = Options()
#firefox_options.add_argument("--disable-extensions")
#edge_options = Options()
#edge_options.add_argument("--disable-extensions")

chrome_driver = webdriver.Chrome(executable_path=r'C:\Windows\System32\chromedriver.exe', chrome_options=chrome_options)
#firefox_driver = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe', firefox_options=firefox_options)
#edge_driver = webdriver.Edge(executable_path=r'C:\Windows\System32\msedgedriver.exe', edge_options=edge_options)

chrome_driver.get('https://google.com')
#firefox_driver.get('https://google.com')
#edge_driver.get('https://google.com')


"""
# sending a get request to GitHub and waiting for a second
chrome_driver.get('https://github.com')
chrome_driver.maximize_window()
Event().wait(1)

# entering the desired string through NAME in the search field
search_field_name = chrome_driver.find_element(By.NAME, 'q')
search_field_name.send_keys('selenium')

# pressing ENTER
enter_now = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]')
enter_now.send_keys(Keys.RETURN)
"""
print()
print()
print()
