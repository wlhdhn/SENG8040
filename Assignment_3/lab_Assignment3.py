# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.amazon.ca")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox") old syntax
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("laptop mouse")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "laptop mouse" in driver.title

# Selecting a laptop from the search results
laptop_link = driver.find_element("xpath","/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div")
# laptop_link = driver.find_element("By.CSS_SELECTOR","span[data-component-type='s-product-image'] a")
laptop_link.click()

# Waiting for the laptop details page to load
time.sleep(5)

# Buying the laptop now
buy_now_button = driver.find_element("id","buy-now-button")
buy_now_button.click()

# Waiting to update
time.sleep(5)

# Proceed to create an account
create_Account_checkout= driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/div[2]/div[2]/span/span/a")
create_Account_checkout.click()
time.sleep(2)

# Creating an account
create_Account_button = driver.find_element("id","createAccountSubmit")
create_Account_button.click()

# Verifying that the laptop has been added to the cart
# cart_count = driver.find_element("id","nav-cart-count")
# assert cart_count.text == "1"
# cart_count.click()

# Closing the webdriver
driver.close()
