import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # importing "by"

# try and except?

options = Options()
# Headless Setting
# options.headless = True
# options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

player_list = []
birthday_list = []

url = 'https://en.wikipedia.org/wiki/Category:2022_FIFA_World_Cup_players'
driver.get(url)

#brendon guy
print(driver.find_element(By.XPATH, '//*[@id="mw-pages"]/div/div/div[1]/ul/li[1]').text)

# By Classes. Problem: each alphabet is a long list
#wiki_player_list = driver.find_elements(By.CLASS_NAME, "mw-category-group")

#wiki_player_list = driver.find_element(By.XPATH, '//*[@id="mw-pages"]/div/div/div[1]/ul/li[1]')

# By anchor tags
# wiki_player_list = driver.find_elements(By.TAG_NAME, 'a')

# wiki_player_list = driver.find_elements(By.XPATH, ".//*[@id='mw-pages']/div/div")
# wiki_player_list = driver.find_elements(By.XPATH, "//*[@class='mw-category-group']//ul[last()]")

# wiki_player_list = driver.find_element(By.CLASS_NAME, "mw-category-group")

for page in range(1): # originally 5
    wiki_player_list = driver.find_element(By.XPATH, ".//*[@id='mw-pages']/div/div")
    wiki_player_list = wiki_player_list.find_elements(By.TAG_NAME, 'a')

    for j in wiki_player_list:
        #player_list.append([wiki_player_list])
        print('Name: '+ j.text)
        player_list.append(j.text)
    print(wiki_player_list)

    driver.find_element(By.XPATH, '//*[@id="mw-pages"]/a[2]').click()
print(player_list)

# Finds Birthdays
for i in player_list:
    url = 'https://www.google.com/search?q=' + i + '+birthday'
    driver.get(url)
    try:
        birthday = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]' ).text
        birthday_list.append(birthday)
        print("success")
        # time.sleep(random.randint(15,20)/10)

    except:
        print("fail")
        time.sleep(200)
        continue

print(birthday_list)
print(player_list)
driver.quit()

# url = 'https://www.google.com/search?q=ronaldo+birthday'
# driver.get(url)
# messi = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]' ).text
# print(driver.title)
# print(driver.current_url)
