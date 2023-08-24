import time
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

url = 'https://www.premierleague.com/players'
driver.get(url)
try:
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click() # Accepts Cookies
except Exception:
    pass

try:
    driver.find_element(By.XPATH, '//*[@id="advertClose"]').click() # Closes thing
except Exception:
    pass

time.sleep(1)

# ------------------------------------------------------------------------------
# y = 1000
# for timer in range(0,100):
#      driver.execute_script("window.scrollTo(0, "+str(y)+")")
#      y += 1000
#      time.sleep(1/4)
# time.sleep(3)
# ------------------------------------------------------------------------------
player_locations = driver.find_elements(By.CLASS_NAME, 'playerName')
time.sleep(1)
for i in player_locations:
    try:
        print(i.text)
    except:
        print("Couldn't print")

for player in player_locations:
    stats_screen = False
    success1 = True
    try:
        player.click()
        time.sleep(1)
    except Exception:
        print("Player was skipped") # Skips iteration anyways
        continue

    time.sleep(1)
    try:
        c_name = driver.find_element(By.XPATH, '//*[@id="mainContent"]/section/div[2]/div[2]/h1/div').text # Grabs Name
        c_bday = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[3]/div/div/div[1]/section/div/ul[2]/li/div[2]').text # Grabs Birthday
        driver.find_element(By.XPATH, "//*[@id='mainContent']/div[2]/nav/ul/li[2]/a").click() # Clicks on Stat Screen
        stats_screen = True
        print(driver.find_element(By.XPATH, "//*[@id='mainContent']/div[3]/nav/div/section[1]/div[4]").text) # Grabs position
        driver.back()

    except:
        try:
            driver.find_element(By.XPATH, '//*[@id="advertClose"]').click()  # Closes thing
            player_list.append(driver.find_element(By.XPATH, '//*[@id="mainContent"]/section/div[2]/div[2]/h1/div').text)
            birthday_list.append(driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[3]/div/div/div[1]/section/div/ul[2]/li/div[2]').text)
            driver.find_element(By.XPATH, "//*[@id='mainContent']/div[2]/nav/ul/li[2]/a").click()
            print(driver.find_element(By.XPATH, "//*[@id='mainContent']/div[3]/nav/div/section[1]/div[4]").text)
            driver.back()

        except:
            print("Player was skipped")
            success1 = False
            pass

    if success1:
        birthday_list.append(c_bday) # Current player's birthday
        player_list.append(c_name) # Current player's name


    print(player_list)
    print(birthday_list)
    driver.back()



time.sleep(33)


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


