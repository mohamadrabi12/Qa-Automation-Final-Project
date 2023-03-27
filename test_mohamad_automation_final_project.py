import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     driver.get("https://svburger1.co.il/#/HomePage")
#     driver.maximize_window()



def test_sanity():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()

    sign = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button')
    sign.click()

    email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
    email.send_keys("mohamad.rabi@Hotmail.com")

    password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
    password.send_keys("ajha123456")

    sign2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    sign2.click()

    driver.implicitly_wait(8)

    kids_meal = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div')
    kids_meal.click()

    reverse = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[2]')
    reverse.click()

    table_number = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[3]/div[5]/input')
    table_number.send_keys(Keys.BACKSPACE)

    table_number = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[3]/div[5]/input')
    table_number.send_keys("1")

    send = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[1]/button')
    send.click()

    order_done = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/h3[1]')

    time.sleep(1)
    assert order_done.is_displayed()


#sign up suite- Functionality 1 – register only with required field
def test_sign_up_register_only_with_required_field():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()

    sign_up1 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[2]/button')
    sign_up1.click()
    email1 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[3]')
    email1.send_keys("mohamad.rabi132@hotmail.com")
    create_password1 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[4]')
    create_password1.send_keys("ajha123456")
    confir_password1 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[5]')
    confir_password1.send_keys("ajha123456")
    sign_up2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    sign_up2.click()
    driver.implicitly_wait(2)
    sign_up_done1 = driver.find_element(By.XPATH,
                                       '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
    time.sleep(1)
    assert sign_up_done1.is_displayed()
    time.sleep(3)
# sign up suite- Functionality 2 – register with 7 chars on First Name
def test_sign_up_register_with_7_chars_on_first_name():
   driver = webdriver.Chrome()
   driver.get("https://svburger1.co.il/#/HomePage")
   driver.maximize_window()

   sign_up5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[2]/button')
   sign_up5.click()
   email3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[3]')
   email3.send_keys("mohamad.rabi502@hotmail.com")
   firstname3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[1]')
   firstname3.send_keys("abcdaaa")
   create_password3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[4]')
   create_password3.send_keys("ajha123456")
   confir_password3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[5]')
   confir_password3.send_keys("ajha123456")
   time.sleep(1)
   sign_up6 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
   sign_up6.click()

   sign_up_done3 = driver.find_element(By.XPATH,
                                       '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
   time.sleep(1)
   driver.implicitly_wait(2)
   assert sign_up_done3.is_displayed()
   time.sleep(1)
# sign up suite- Functionality 3 – register with 8 chars on First Name
def test_sign_up_register_with_8_chars_on_first_name():
   driver = webdriver.Chrome()
   driver.get("https://svburger1.co.il/#/HomePage")
   driver.maximize_window()

   sign_up5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[2]/button')
   sign_up5.click()
   email3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[3]')
   email3.send_keys("mohamad.rabi82@hotmail.com")
   firstname3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[1]')
   firstname3.send_keys("abcdaaab")
   create_password3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[4]')
   create_password3.send_keys("ajha123456")
   confir_password3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[5]')
   confir_password3.send_keys("ajha123456")
   time.sleep(1)
   sign_up6 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
   sign_up6.click()

   sign_up_done3 = driver.find_element(By.XPATH,
                                       '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
   time.sleep(1)
   driver.implicitly_wait(2)
   assert sign_up_done3.is_displayed()
   time.sleep(1)

# sign up suite- Functionality 4 – register with 9 chars on First Name

def test_sign_up_register_with_9_chars_on_first_name():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()

    sign_up7 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[2]/button')
    sign_up7.click()

    email4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[3]')
    email4.send_keys("mohamad.ra127@hotmail.com")

    firstname4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[1]')
    firstname4.send_keys("abcdaaabc")

    create_password4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[4]')
    create_password4.send_keys("ajha123456")

    confir_password4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[5]')
    confir_password4.send_keys("ajha123456")

    sign_up8 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    sign_up8.click()

    sign_up_done4 = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
    time.sleep(1)
    driver.implicitly_wait(2)
    assert sign_up_done4.is_displayed()

    time.sleep(8)
# sign up suite- Functionality 5 – register with 10 chars on First Name
def test_sign_up_register_with_10_chars_on_first_name():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()

    sign_up7 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[2]/button')
    sign_up7.click()

    email4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[3]')
    email4.send_keys("mohamad.r1232@hotmail.com")

    firstname4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[1]')
    firstname4.send_keys("abcdaaabcb")

    create_password4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[4]')
    create_password4.send_keys("ajha123456")

    confir_password4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[5]')
    confir_password4.send_keys("ajha123456")

    sign_up8 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    sign_up8.click()

    sign_up_done4 = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
    time.sleep(1)
    driver.implicitly_wait(2)
    assert sign_up_done4.is_displayed()

    time.sleep(8)

    # sign up suite- ERROR HANDLING 1 – Sign up with 11 characters on first name
def test_sign_up_with_11_characters_on_first_name():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()

    sign_up9 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[2]/button')
    sign_up9.click()

    email5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[3]')
    email5.send_keys("mohaajfsfk@hotmail.com")

    firstname5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[1]')
    firstname5.send_keys("faximmaximm")

    create_password5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[4]')
    create_password5.send_keys("ajha123456")

    confir_password5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[5]')
    confir_password5.send_keys("ajha123456")
    driver.implicitly_wait(2)
    sign_up10 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    sign_up10.click()
    time.sleep(3)

    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "First name must be between 2 and 10 characters"
    time.sleep(5)
# sign up suite- ERROR HANDLING 2 – without inserting an Email.
def test_sign_up_with_11_characters_on_first_name():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()

    sign_up8 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[2]/button')
    sign_up8.click()

    create_password5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[4]')
    create_password5.send_keys("ajha123456")

    confir_password5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/input[5]')
    confir_password5.send_keys("ajha123456")
    driver.implicitly_wait(2)
    sign_up9 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/form/button')
    sign_up9.click()
    time.sleep(3)
    sign_up_done4 = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div[2]/div[1]/div/div/form/input[3]')
    # if this field still in the page so the sing up failed .
    # beacuse this error message isnt alert so i dont know what i should do
    time.sleep(1)
    assert sign_up_done4.is_displayed()
#Log in suite - Functionality 1 - Login via hotmail (mohamad.rabi@hotmail.com)
def test_login_via_hotmail():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/SignIn")
    driver.maximize_window()

    login_email1 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
    login_email1.send_keys("mohamad.rabi@hotmail.com")

    login_pass1 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
    login_pass1.send_keys("ajha123456")

    sign_in1 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    sign_in1.click()
    driver.implicitly_wait(1)
    login_done = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')

    time.sleep(1)
    assert login_done.is_displayed()
    time.sleep(3)
#Log in suite - Functionality 2 - Login via Yahoo (mohamad.rabi@yahoo.com)
def test_login_via_yahoo():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/SignIn")
    driver.maximize_window()

    login_email2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
    login_email2.send_keys("mohamad.rabi@yahoo.com")

    login_pass2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
    login_pass2.send_keys("ajha123456")

    sign_in2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    sign_in2.click()
    driver.implicitly_wait(1)
    sign_up_done4 = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
    time.sleep(1)
    assert sign_up_done4.is_displayed()
#Log in suite - Functionality 3 - Login via gmail (mohamad.rabi@gmail.com)
def test_login_via_gmail():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/SignIn")
    driver.maximize_window()

    login_email3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
    login_email3.send_keys("mohamad.rabi@gmail.com")

    login_pass3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
    login_pass3.send_keys("ajha123456")

    sign_in3 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    sign_in3.click()
    driver.implicitly_wait(1)
    sign_up_done5 = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
    time.sleep(1)
    assert sign_up_done5.is_displayed()
#Log in suite - Functionality 4 - Login via outlook (mohamad.rabi@outlook.com)
def test_login_via_outlook():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/SignIn")
    driver.maximize_window()

    login_email4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
    login_email4.send_keys("mohamad.rabi@outlook.com")

    login_pass4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
    login_pass4.send_keys("ajha123456")

    sign_in4 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    sign_in4.click()
    driver.implicitly_wait(1)
    sign_up_done6 = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
    time.sleep(1)
    assert sign_up_done6.is_displayed()
#Log in suite - Functionality 5 - Login via aol (mohamad.rabi@aol.com)
def test_login_via_aol():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/SignIn")
    driver.maximize_window()

    login_email5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
    login_email5.send_keys("mohamad.rabi@aol.com")

    login_pass5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
    login_pass5.send_keys("ajha123456")

    sign_in5 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    sign_in5.click()
    driver.implicitly_wait(1)
    sign_up_done7 = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
    time.sleep(1)
    assert sign_up_done7.is_displayed()
#Log in suite - Error Handling 1 - Login with wrong password (123)
def test_login_with_wrong_pass():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/SignIn")
    driver.maximize_window()

    login_email6 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
    login_email6.send_keys("mohamad.rabi@aol.com")

    login_pass6 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
    login_pass6.send_keys("123")
    driver.implicitly_wait(1)
    sign_in6 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    sign_in6.click()
    time.sleep(3)
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Failed to log in"
    # Log in suite - Error Handling 2 - sign up without inserting an email
def test_login_without_email():
    driver = webdriver.Chrome()
    driver.get("https://svburger1.co.il/#/SignIn")
    driver.maximize_window()

    login_pass7 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
    login_pass7.send_keys("ajha123456")
    driver.implicitly_wait(1)
    sign_in7 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
    sign_in7.click()
    time.sleep(3)
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Failed to log in"
# Reservation and confirm reservation - Functionality 1 - Select 2 Meals

def test_select_2_meals():
   driver = webdriver.Chrome()
   driver.get("https://svburger1.co.il/#/HomePage")
   driver.maximize_window()

   sign = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button')
   sign.click()
   email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
   email.send_keys("mohamad.rabi@Hotmail.com")
   password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
   password.send_keys("ajha123456")
   sign2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
   sign2.click()
   driver.implicitly_wait(2)
   combo_meal = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
   combo_meal.click()
   vegan_meal = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[4]/div/div/div[2]/div/h5')
   vegan_meal.click()
   reverse = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[2]')
   reverse.click()
   table_number = driver.find_element(By.XPATH,
                                      '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[5]/input')
   table_number.send_keys(Keys.BACKSPACE)

   table_number = driver.find_element(By.XPATH,
                                      '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[5]/input')
   table_number.send_keys("1")

   send = driver.find_element(By.XPATH,
                              '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[5]/div[1]/button')
   send.click()
   time.sleep(1)
   correct_price = driver.find_element(By.XPATH, '//h2[text()="114.4"]')
   assert correct_price.is_displayed()
# Reservation and confirm reservation - Functionality 2 - Select same meal twice to cancel order


def test_select_same_meal_twice_to_cancel():
   driver = webdriver.Chrome()
   driver.get("https://svburger1.co.il/#/HomePage")
   driver.maximize_window()

   sign = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button')
   sign.click()
   email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
   email.send_keys("mohamad.rabi@Hotmail.com")
   password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
   password.send_keys("ajha123456")
   sign2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
   sign2.click()
   time.sleep(1)
   combo_meal = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
   combo_meal.click()
   combo_meal.click()
   time.sleep(1)
   assert not combo_meal.is_selected()

# Reservation and confirm reservation - Functionality 3 - Order 2 meals (combo,vegan) to table number 2
def test_order_2_meals_combo_vegan_to_table_2():
   driver = webdriver.Chrome()
   driver.get("https://svburger1.co.il/#/HomePage")
   driver.maximize_window()

   sign = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button')
   sign.click()
   email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
   email.send_keys("mohamad.rabi@Hotmail.com")
   password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
   password.send_keys("ajha123456")
   sign2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
   sign2.click()
   time.sleep(1)
   combo_meal = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
   combo_meal.click()
   vegan = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[4]/div/div/div[2]/div/h5')
   vegan.click()
   reserve = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[2]')
   reserve.click()
   table_number = driver.find_element(By.XPATH,
                                      '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[5]/input')
   table_number.send_keys(Keys.BACKSPACE)

   table_number = driver.find_element(By.XPATH,
                                      '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[5]/input')
   table_number.send_keys("2")
   send = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[5]/div[1]/button')
   send.click()
   time.sleep(1)
   order_done_with_correct_expected_price = driver.find_element(By.XPATH, '//h2[text()="114.4"]')
   time.sleep(1)
   assert order_done_with_correct_expected_price.is_displayed()
# Reservation and confirm reservation - Functionality 4 - Press on Log Out
def test_press_log_out():
       driver = webdriver.Chrome()
       driver.get("https://svburger1.co.il/#/HomePage")
       driver.maximize_window()

       sign = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button')
       sign.click()
       email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
       email.send_keys("mohamad.rabi@Hotmail.com")
       password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
       password.send_keys("ajha123456")
       sign2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
       sign2.click()
       time.sleep(1)
       log_out = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[1]')
       log_out.click()
       time.sleep(1)
       back_to_home_page = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/p[1]')
       time.sleep(1)
       assert back_to_home_page.is_displayed()
# Reservation and confirm reservation - Functionality 5 - Press in Back to menu
def test_press_in_back_to_menu():
   driver = webdriver.Chrome()
   driver.get("https://svburger1.co.il/#/HomePage")
   driver.maximize_window()

   sign = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button')
   sign.click()
   email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
   email.send_keys("mohamad.rabi@Hotmail.com")
   password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
   password.send_keys("ajha123456")
   sign2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
   sign2.click()
   time.sleep(1)
   kids_meal = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div')
   kids_meal.click()
   reverse = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[2]')
   reverse.click()
   time.sleep(1)
   back_to_menu = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[2]/button')
   back_to_menu.click()
   back_to_menu_page = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div/h5')
   time.sleep(1)
   assert back_to_menu_page.is_displayed()
# Reservation and confirm reservation - Error Handling 1 - insert 3 on quantity(kids meal)
def test_insert_3_on_quantity():
   driver = webdriver.Chrome()
   driver.get("https://svburger1.co.il/#/HomePage")
   driver.maximize_window()

   sign = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button')
   sign.click()
   email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
   email.send_keys("mohamad.rabi@Hotmail.com")
   password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
   password.send_keys("ajha123456")
   sign2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
   sign2.click()
   time.sleep(1)
   kids_meal = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[2]/div/div/div[2]/div/h5')
   kids_meal.click()
   reserve = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/button[2]')
   reserve.click()
   quantity = driver.find_element(By.XPATH,
                                      '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input')
   quantity.send_keys(Keys.BACKSPACE)

   quantity = driver.find_element(By.XPATH,
                                      '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/input')
   quantity.send_keys("3")
   time.sleep(1)
   send = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[1]/button')
   send.click()
   time.sleep(1)
   send_button = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div[4]/div[1]/button')
   time.sleep(1)
   # if send button still in the page thats mean the test success if send button didnt still in the page so the order has been received.
   # and that means the test failed beacuse thats not the  expected result.
   assert send_button.is_displayed()
# Reservation and confirm reservation - Error Handling 2 - select 4 meal
def test_select_4_meal():
   driver = webdriver.Chrome()
   driver.get("https://svburger1.co.il/#/HomePage")
   driver.maximize_window()

   sign = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/a[1]/button')
   sign.click()
   email = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[1]')
   email.send_keys("mohamad.rabi@Hotmail.com")
   password = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/input[2]')
   password.send_keys("ajha123456")
   sign2 = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/form/div/button')
   sign2.click()
   time.sleep(1)
   burger = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[3]/div/div/div[2]/div/h5')
   burger.click()
   combo_meal = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[1]/div/div/div[2]/div/h5')
   combo_meal.click()
   vegan = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[4]/div/div/div[2]/div/h5')
   vegan.click()
   time.sleep(1)
   sides = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div/div/div[5]/div/div/div[2]/div/h5')
   sides.click()
   time.sleep(1)
   assert sides.is_selected()
   time.sleep(1)
#    if sides is selected thats mean our test failed