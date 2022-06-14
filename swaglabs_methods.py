import datetime
from selenium import webdriver  # import selenium to the file
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import swaglabs_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select # ----------add this import for drop down lists
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch SwagLabs App')
    print(f'___________________________________________')
    # make browser full screen
    driver.maximize_window()
    # give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # navigate to SwagLabs App
    driver.get(locators.swaglabs_url)

    # check that SwagLabs URL and the home page title are as expected
    if  driver.current_url == locators.swaglabs_url and driver.title == locators.swaglabs_home_page_title :
        print(f'Yey! {locators.app} Funnel launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} Funnel did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print(f'______________________________________________')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


def log_in():
    print(f'This is the LOGIN Page')
    if driver.current_url == locators.swaglabs_url and driver.title == locators.swaglabs_home_page_title :
        driver.find_element(By.ID, 'user-name').send_keys(locators.username)
        sleep(0.25)
        driver.find_element(By.ID, 'password').send_keys(locators.password)
        sleep(0.25)
        driver.find_element(By.ID, 'login-button').click()
        print(f'Hey! You have successfully logged in')
    else:
        print(f'Something is not right, check your code ')
        sleep(0.25)


def my_cart():
    print(f'Yippey! This is my shopping cart')
    sleep(1.00)
    driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] div[class="inventory_item_name"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//button[@id="back-to-products"]').click()
    sleep(1.25)
    driver.find_element(By.CSS_SELECTOR, 'a[id="item_3_title_link"] div[class="inventory_item_name"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//button[@id="back-to-products"]').click()
    sleep(1.25)
    driver.find_element(By.CSS_SELECTOR, 'a[id="item_1_title_link"] div[class="inventory_item_name"]').click()
    sleep(1.25)
    driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    sleep(1.25)
    driver.find_element(By.CSS_SELECTOR, 'div[id="shopping_cart_container"]').click()
    sleep(1.25)
    print(f'**********My Shopping cart is displayed***************')
    assert driver.find_element(By.XPATH, '//span[contains(., "Your Cart")]').is_displayed()
    print(f'This is the orders in my cart')
    sleep(0.25)
    print(f'*************Validating to check all items are displayed in Shopping cart****************************')
    for i in range(len(locators.cartitems)):
        assert driver.find_element(By.XPATH, f'//div[contains(., "{locators.cartitems[i]}")]').is_displayed()
        verifyshoppingcart = driver.find_element(By.XPATH, f'//div[contains(., "{locators.cartitems[i]}")]').is_displayed()
        print(f'The item {locators.cartitems[i]} is displayed: {verifyshoppingcart}')
        sleep(0.75)


def check_out():
    print(f'*********Proceeding to checkout*****************************************')
    driver.find_element(By.ID, 'checkout').click()
    assert driver.find_element(By.XPATH, f'//span[@class="title"]').is_displayed()
    your_info = driver.find_element(By.XPATH, f'//span[@class="title"]').is_displayed()
    print(your_info)
    sleep(0.25)
    driver.find_element(By.ID, 'first-name').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'last-name').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'postal-code').send_keys(locators.zip)
    sleep(0.25)
    driver.find_element(By.ID, 'continue').click()
    assert driver.find_element(By.XPATH, f'//span[@class="title"]').is_displayed()
    overview = driver.find_element(By.XPATH, f'//span[@class="title"]').is_displayed()
    print(overview)
    sleep(0.25)
    driver.find_element(By.ID, 'finish').click()
    sleep(0.25)
    assert driver.find_element(By.XPATH, '//h2[@class="complete-header"]').is_displayed()
    checkout_complete = driver.find_element(By.XPATH, '//h2[@class="complete-header"]').is_displayed()
    print(checkout_complete)
    if driver.find_element(By.XPATH, f'//h2[contains(., "THANK YOU FOR YOUR ORDER")]').is_displayed():
        print(f'THANK YOU FOR YOUR ORDER message is displayed')
    else:
        print(f'Thank you message is not displayed')
        sleep(0.25)
    driver.find_element(By.XPATH, '//button[@class="btn btn_primary btn_small"]').click()
    sleep(0.25)


def log_out():
    print(f'***********Proceed to log out**********************************')
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    sleep(0.25)
    driver.find_element(By.ID, 'logout_sidebar_link').click()
    sleep(0.25)
    print(f'You are logged out. Feel free to check in and shop.')







# setUp()
# log_in()
# my_cart()
# check_out()
# log_out()
# tearDown()