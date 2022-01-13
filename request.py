from selenium import webdriver
from threading import Event
from selenium.webdriver.common.by import By

# exercise 5 - open YouTube and search for a song
# defining path for chrome webdriver

chrome_driver = webdriver.Chrome(r'/Users/noy/Downloads/chromedriver')

# navigating to YouTube
chrome_driver.get('https://youtube.com')

# typing the search in the text box
search_field = chrome_driver.find_element(By.NAME, 'search_query')
search_string = "Never gonna give you up"
Event().wait(1)
search_field.send_keys(search_string)

# pressing the search button
search_button = chrome_driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon')
Event().wait(1)
search_button.click()
print()
print()
print()
