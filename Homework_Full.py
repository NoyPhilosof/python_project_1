from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from threading import Event

# exercise 1+2 - open Chrome and Firefox in specific address, get some info and refresh
# defining path for chrome webdriver
chrome_driver = webdriver.Chrome(executable_path=r'C:\Windows\System32\chromedriver.exe')

# sending a get and title requests to ynet
chrome_driver.get('https://www.ynet.co.il')
website_title = chrome_driver.title
print(website_title)

# storing website's URL as variable
website_name = chrome_driver.current_url
print(website_name)

# waiting for three seconds and refreshing the page
Event().wait(3)
chrome_driver.refresh()

# defining path for Firefox + sending a get request to walla
firefox_driver = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe')
firefox_driver.get('https://www.walla.co.il')
print()
print()
print()

# exercise 3 - seems like the HTML code is the same in different browsers (checked on a search box on www.ebay.com)
"""
Firefox:
<input type="text" class="gh-tb ui-autocomplete-input" aria-autocomplete="list" aria-expanded="false" size="50" maxlength="300" aria-label="Search for anything" placeholder="Search for anything" id="gh-ac" name="_nkw" autocapitalize="none" autocorrect="off" spellcheck="false" autocomplete="off" aria-haspopup="true" role="combobox" aria-owns="ui-id-1">
Chrome:
<input type="text" class ="gh-tb ui-autocomplete-input" aria-autocomplete="list" aria-expanded="false" size="50" maxlength="300" aria-label="Search for anything" placeholder="Search for anything" id="gh-ac" name="_nkw" autocapitalize="off" autocorrect="off" spellcheck="false" autocomplete="off" aria-haspopup="true" role="combobox" aria-owns="ui-id-1">
Edge:
<input type="text" class ="gh-tb ui-autocomplete-input" aria-autocomplete="list" aria-expanded="false" size="50" maxlength="300" aria-label="Search for anything" placeholder="Search for anything" id="gh-ac" name="_nkw" autocapitalize="off" autocorrect="off" spellcheck="false" autocomplete="off" aria-haspopup="true" role="combobox" aria-owns="ui-id-1">
"""

# exercise 4 - make a search in Google Translate
# defining path for chrome webdriver
chrome_driver = webdriver.Chrome(executable_path=r'C:\Windows\System32\chromedriver.exe')

# sending a get request to google translate
chrome_driver.get('https://translate.google.com')

# pressing the drop-down menu button for language selection
button1 = chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[2]/button/div[2]')
Event().wait(1)
button1.click()

# pressing the Hebrew language button
button2 = chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[1]/div/div[3]/div/div[3]/div[37]/div[2]')
Event().wait(1)
button2.click()

# entering hebrew string in the translation field
translation_field = chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
hebrew_string = "סגור לי את הפינה"
Event().wait(1)
translation_field.send_keys(hebrew_string)
print()
print()
print()


# exercise 5 - open YouTube and search for a song
# defining path for chrome webdriver
chrome_driver = webdriver.Chrome(executable_path=r'C:\Windows\System32\chromedriver.exe')

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


# exercise 6 - locate an element in three different ways
# defining path for chrome webdriver
chrome_driver = webdriver.Chrome(executable_path=r'C:\Windows\System32\chromedriver.exe')

# sending a get request to google translate
chrome_driver.get('https://translate.google.com')
hebrew_string = "סגור לי את הפינה"

# entering hebrew string through XPATH in the translation field
translation_field_xpath = chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
Event().wait(1)
translation_field_xpath.send_keys(hebrew_string)

# entering hebrew string through CSS_SELECTOR in the translation field
translation_field_CSS = chrome_driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz > div > div.WFnNle > c-wiz > div.OlSOob > c-wiz > div.ccvoYb > div.AxqVh > div.OPPzxe > c-wiz.rm1UF.UnxENd > span > span > div > textarea')
Event().wait(1)
translation_field_CSS.send_keys(hebrew_string)

# entering hebrew string through CLASS_NAME of the translation field
translation_field_CLASS = chrome_driver.find_element(By.CLASS_NAME, 'er8xn')
Event().wait(1)
translation_field_CLASS.send_keys(hebrew_string)
print()
print()
print()


# exercise 7 - login to facebook
def firefox_facebook_login(user='username@mailservice.com', password='password'):
    """
    This func allows for automatic facebook login via firefox web browser.
    :param user: accepts string formatted as an email address
    :param password: accepts a string
    :return: None
    """
    # setting up firefox webdriver
    firefox_driver = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe')

    # sending get message to facebook and waiting for a second
    firefox_driver.get('https://www.facebook.com')
    Event().wait(1)

    # fill string to the username field - either user defined or the default one
    username_field = firefox_driver.find_element(By.NAME, 'email')
    username_field.send_keys(user)

    # fill string to the password field - either user defined or the default one and wait for a second
    password_field = firefox_driver.find_element(By.NAME, 'pass')
    password_field.send_keys(password)
    Event().wait(1)

    # press the login button
    login_button = firefox_driver.find_element(By.NAME, 'login')
    login_button.click()
    return


# run the func with default values
firefox_facebook_login()
print()
print()
print()


# exercise 8 - open a webpage and delete cookies
def open_and_delete_cookies(address ='https://walla.co.il'):
    """
    This func opens a web page in FireFox, shows number of current cookies and deletes them afterwards
    :param address: accepts string formatted as http address
    :return: None
    """
    # setting up webdriver for firefox
    firefox_driver = webdriver.Firefox(executable_path=r'C:\Windows\System32\geckodriver.exe')

    # sending a get request to the specified address and waiting for three seconds
    firefox_driver.get(address)
    Event().wait(3)

    # counts and displays number of cookies before deletion
    current_cookies = firefox_driver.get_cookies()
    print(f'At the moment there are {len(current_cookies)} cookies in FireFox cache.\n')

    # delete all cookies
    firefox_driver.delete_all_cookies()

    # counts and displays number of cookies after deletion
    current_cookies = firefox_driver.get_cookies()
    print(f'After deletion there are {len(current_cookies)} cookies in FireFox cache.')
    return
print()
print()
print()

open_and_delete_cookies('https://ynet.co.il')


# exercise 9 - open GitHub and search for 'selenium'
# setting up webdriver for chrome
chrome_driver = webdriver.Chrome(executable_path=r'C:\Windows\System32\chromedriver.exe')

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
print()
print()
print()
