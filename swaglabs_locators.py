import datetime

from faker import Faker
fake = Faker(locale='en_CA')


#_________________Swag Labs App DATA PARAMETERS__________________________
app = 'SwagLabs'
swaglabs_url = 'https://www.saucedemo.com/'
swaglabs_home_page_title = 'Swag Labs'

username = 'standard_user'
password = 'secret_sauce'
first_name = fake.first_name()
last_name = fake.last_name()
zip = fake.postcode()

cartitems = ['Sauce Labs Backpack', 'Test.allTheThings() T-Shirt (Red)', 'Sauce Labs Bolt T-Shirt']