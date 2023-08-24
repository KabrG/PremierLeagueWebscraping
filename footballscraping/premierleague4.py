import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # importing "by"

# --------------------------------------------------------------------------------------------------------------------
# All Arrays
player_list = []
birthday_list = []

# Classes
class forward:
    player_list = []
    birthday_list = []
    stat1 = []
    stat2 = []

class midfielder:
    player_list = []
    birthday_list = []
    stat1 = []
    stat2 = []

class defender:
    player_list = []
    birthday_list = []
    stat1 = []
    stat2 = []

# --------------------------------------------------------------------------------------------------------------------

options = Options()
# Headless Setting
options.headless = True
options.add_argument("--window-size=1920,1080")

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(options=options)

url = 'https://www.premierleague.com/players'
driver.get(url)

# Closes Pop-Ups
def closePopUp():
    try:
        driver.find_element(By.XPATH, '//*[@id="advertClose"]').click()  # Closes pop-up
    except Exception:
        pass

# Accepts Cookies (Only Occurs once)
try:
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()  # Accepts Cookies
except Exception:
    pass

closePopUp()

# ------------------------------------------------------------------------------
# Scrolling
y = 1000
for timer in range(0,100):
     driver.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 1000
     time.sleep(1/2)
time.sleep(3)
# ------------------------------------------------------------------------------
time.sleep(3)
# Grabs the locations for elements under class name "playerName"
player_locations = driver.find_elements(By.CLASS_NAME, 'player__name')

for i in player_locations:
    try:
        print(i.text)
    except:
        print("Couldn't print")

for player in player_locations:
    stats_screen = False
    overall_screen = False
    success1 = True
    closePopUp()

    try:
        player.click()
        overall_screen = True

    except Exception:
        print("Player was skipped")  # Skips iteration anyways
        # driver.get_screenshot_as_file("screenshot.png")
        # driver.quit()
        continue

    closePopUp()

    try:
        # Grabs Name
        c_name = driver.find_element(By.XPATH, '//*[@id="mainContent"]/section/div[2]/div[2]/h1/div').text
        # Grabs Birthday
        c_bday = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[3]/div/div/div[1]/section/div/ul[2]/li/div[2]').text
        # Clicks on Stat Screen
        driver.find_element(By.XPATH, "//*[@id='mainContent']/div[2]/nav/ul/li[2]/a").click()
        stats_screen = True
        # Grabs player's position
        position = driver.find_element(By.XPATH, "//*[@id='mainContent']/div[3]/nav/div/section[1]/div[4]").text

    except Exception:
        print("Player was skipped")
        success1 = False

    # Checks number of appearances
    if success1:
        c_appearance = int(driver.find_element(By.XPATH, "//*[@id='mainContent']/div[3]/div/div/div[2]/div/div/div/div[1]/span/span").text)
        if c_appearance == 0:
            print('No appearances')
            success1 = False

    if success1:
        try:
            if position == 'Forward':
                # Goals per Game Played
                c_stat = driver.find_element(By.XPATH, "//*[@id='mainContent']/div[3]/div/div/div[2]/div/div/ul/li[1]/div/div[3]/span/span").text
                print(c_stat)
                forward.player_list.append(c_name)
                forward.birthday_list.append(c_bday)
                forward.stat1.append(c_stat)

                # Print Lists
                print('Forward:')
                print(forward.player_list)
                print(forward.birthday_list)
                print(forward.stat1)

            elif position == 'Midfielder':
                # Big Chances Created
                # print('GETS HERE')
                c_stat = int(driver.find_element(By.XPATH, "//*[@id='mainContent']/div[3]/div/div/div[2]/div/div/ul/li[2]/div/div[5]/span/span").text)
                # print('AND THERE')
                print(c_stat)
                midfielder.player_list.append(c_name)
                midfielder.birthday_list.append(c_bday)
                # Stat 1 is Big Chances created per Game
                midfielder.stat1.append(round(c_stat/c_appearance, 2))

                # Print Lists
                print('Midfielder:')
                print(midfielder.player_list)
                print(midfielder.birthday_list)
                print(midfielder.stat1)

            elif position == 'Defender':
                # Percent Tackles Won
                c_stat = driver.find_element(By.XPATH, "//*[@id='mainContent']/div[3]/div/div/div[2]/div/div/ul/li[1]/div/div[5]/span/span").text
                print(c_stat)
                defender.player_list.append(c_name)
                defender.birthday_list.append(c_bday)
                defender.stat1.append(c_stat)

                # Print Lists
                print('Defender:')
                print(defender.player_list)
                print(defender.birthday_list)
                print(defender.stat1)
            elif position == 'Goalkeeper':
                print("Goalkeeper. Ignoring.")

            else:
                print("Invalid Position")

        except Exception:
            success1 = False
            print("Unable to retrieve stat")

    if stats_screen:
        driver.back()
    if overall_screen:
        driver.back()

    # print(player_list)
    # print(birthday_list)

# -------------------------------------------------------------------------------------------
# Counts number of players in months
def monthCounter(array):
    monthCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    monthNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in array:
        for j in range(len(monthNum)):
            if int(i[3] + i[4]) == monthNum[j]:
                monthCount[j] += 1
    return monthCount

# Prints Data
print('Forwards:')
print(monthCounter(forward.birthday_list))
print(forward.birthday_list)
print(forward.player_list)
print(forward.stat1)

print('Midfielder Bday Count:')
print(monthCounter(midfielder.birthday_list))
print(midfielder.birthday_list)
print(midfielder.player_list)
print(midfielder.stat1)

print('Defender Bday Count:')
print(monthCounter(defender.birthday_list))
print(defender.birthday_list)
print(defender.player_list)
print(defender.stat1)

#-------------------------------------------------------------------------------------------
print("THE END")
time.sleep(5)
driver.quit()

