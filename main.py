from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

recipe_search = input('What would you like recipes for?')

# chrome_driver_path = ''
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
service = Service(executable_path=ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
driver = webdriver.Chrome(service=service)
page_url = 'https://www.kosher.com/'

driver.get(page_url)

search_button = driver.find_element_by_class_name('link-search')
search_button.click()

search_text = driver.find_element_by_css_selector('.header-search__form .form-input input')
search_text.send_keys(recipe_search)
search_text.send_keys(Keys.ENTER)

item_links = [item.get_attribute('href') for item in driver.find_elements_by_class_name('item-card__visual')][0:3]

def get_recipe():
    recipe_name = driver.find_element_by_class_name('recipe-detail__title').text
    print(recipe_name)

    ingredients = driver.find_elements_by_css_selector('.list-checkbox-ingredients li .form-checkbox__title')
    for ingredient in ingredients:
        print(ingredient.text)

    step_title = driver.find_element_by_class_name('step__title').text
    print(step_title)

    step_content = driver.find_elements_by_css_selector('.step__content ol li div')
    for step in step_content:
        print(step.text)

def link_search(href, card_list):
    for card in card_list:
        if card.get_attribute('href') == href:
            card.click()
            get_recipe()
            driver.back()
            time.sleep(5)
            return

for link in item_links:
    link_search(link, driver.find_elements_by_class_name('item-card__visual'))

driver.quit()