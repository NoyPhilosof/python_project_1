#firefox
<input type="text" class="gh-tb ui-autocomplete-input" aria-autocomplete="list" aria-expanded="false" size="50" maxlength="300" aria-label="Search for anything" placeholder="Search for anything" id="gh-ac" name="_nkw" autocapitalize="none" autocorrect="off" spellcheck="false" autocomplete="off" aria-haspopup="true" role="combobox" aria-owns="ui-id-1">

#chrome
<input type="text" class ="gh-tb ui-autocomplete-input" aria-autocomplete="list" aria-expanded="false" size="50" maxlength="300" aria-label="Search for anything" placeholder="Search for anything" id="gh-ac" name="_nkw" autocapitalize="off" autocorrect="off" spellcheck="false" autocomplete="off" aria-haspopup="true" role="combobox" aria-owns="ui-id-1">

#edge
<input type="text"class ="gh-tb ui-autocomplete-input" aria-autocomplete="list" aria-expanded="false" size="50" maxlength="300" aria-label="Search for anything" placeholder="Search for anything" id="gh-ac" name="_nkw" autocapitalize="off" autocorrect="off" spellcheck="false" autocomplete="off" aria-haspopup="true" role="combobox" aria-owns="ui-id-1">


chrome_driver.get('https://www.facebook.com')

username_field = chrome_driver.find_element(By.NAME, 'email')
username_field.send_keys("noyphilosof@gmail.com")

password_field = chrome_driver.find_element(By.NAME, 'pass')
password_field.send_keys("zinvoz-9tupgu-voSruw")

login_button = chrome_driver.find_element(By.ID, 'u_0_d_tN')
login_button.click()
