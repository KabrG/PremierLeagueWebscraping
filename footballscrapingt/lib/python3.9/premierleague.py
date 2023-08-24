import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # importing "by"

# try and except?

options = Options()
# Headless Setting
options.headless = True
options.add_argument("--window-size=1920,1200")

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)


player_list = []
birthday_list = []

url = 'https://www.premierleague.com/players'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click() # Accepts Cookies
driver.find_element(By.XPATH, '//*[@id="advertClose"]').click() # Closes thing


# ------------------------------------------------------------------------------
# Scroll to bottom of page
SCROLL_PAUSE_TIME = 0.5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
# ------------------------------------------------------------------------------

# By anchor tags
prem_position_list = []

for row in range(5):
    prem_player_list = driver.find_element(By.XPATH, "//*[@id='mainContent']/div[2]/div[1]/div/div/table")
    prem_player_list = prem_player_list.find_elements(By.CLASS_NAME, 'playerName')

for k in prem_player_list:
    player_list.append(k.text)

print(prem_player_list)
print(player_list)

driver.get('https://www.premierleague.com/players/Alisson/overview')
print(driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[3]/div/div/div[1]/section/div/ul[2]/li/div[2]').text) # Closes thing


# For positions


# # Finds Birthdays
# for i in player_list:
#     url = 'https://www.google.com/search?q=' + i + '+birthday'
#     driver.get(url)
#     try:
#         birthday = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]' ).text
#         birthday_list.append(birthday)
#         print("success")
#
#     except:
#         print("fail")
#         time.sleep(20)
#         continue
#
# print(birthday_list)
# print(player_list)
driver.quit()

# url = 'https://www.google.com/search?q=ronaldo+birthday'
# driver.get(url)
# messi = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]' ).text
# print(driver.title)
# print(driver.current_url)

