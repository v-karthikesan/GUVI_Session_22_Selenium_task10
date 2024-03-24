from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver import ActionChains
import time
#Creating a Chrome WebDriver instance
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

driver.implicitly_wait(10)
#Navigate to the Instagram profile
driver.get("https://www.instagram.com/guviofficial/")
# Find the followers element using XPath
followers = driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[2]/span").text

# Find the following element using XPath
following = driver.find_element(By.XPATH,"(//span[@class='_ac2a'])[3]/span").text

# Print the total number of followers and following
print("Followers: ", followers)
print("Following: ",following)

driver.quit()