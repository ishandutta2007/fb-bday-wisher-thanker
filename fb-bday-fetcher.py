from selenium import webdriver
from facepy import GraphAPI
import json
import time
import constants
import pprint as pp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, UnexpectedAlertPresentException, WebDriverException
from selenium.webdriver.support.select import Select
import time
import traceback

chrome_options = Options()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=constants.CHROME_DRIVER_PATH)

fb_url = "https://www.facebook.com/login.php"
driver.get(fb_url)
fb_email_element = driver.find_element_by_id("email")
fb_email_element.send_keys(constants.FB_ID)
fb_pass_element = driver.find_element_by_id("pass")
fb_pass_element.send_keys(constants.FB_PASS)
fb_pass_element.send_keys(Keys.ENTER)
time.sleep(2)

driver.get("https://www.facebook.com/ishandutta2007/friends")
time.sleep(2)
try:
    for i in range(1):
        driver.execute_script("window.scrollTo(0, " + str(1000+i*1000) + ")")
        time.sleep(3)

    profile_as = driver.find_elements_by_css_selector("li > div > div > div.uiProfileBlockContent > div > div:nth-child(2) > div > a")

    print("Found", len(profile_as), "profiles")
    profiles = []
    for profile_a in profile_as:
        friend_url = profile_a.get_attribute('href').split('?')[0].split('#')[0]
        if len(friend_url.split('/')) > 4:
            continue
        profiles.append(friend_url)

    pp.pprint(profiles)
    for profile in profiles:
        driver.get(profile+'/about?section=year-overviews')
        life_events = driver.find_elements_by_css_selector("div > ul > li > div > div > ul > li > div > div > a > span")
        if len(life_events) > 0:
            # print(profile, life_events[-1].text)
            try:
                dob = life_events[-1].text.split('Born on ')[1]
                print(profile, dob)
                continue
            except Exception as e:
                pass

        driver.get(profile+'/about')
        overview_events = driver.find_elements_by_css_selector("div > ul > li > div > div > span > div:nth-child(2)")
        for overview_event in overview_events:
            print(profile, overview_event.text)
            try:
                from dateutil.parser import parse
                dob = parse(overview_event.text)
                print(profile, dob)
                continue
            except Exception as e:
                pass

except Exception as e:
		traceback.print_exc()

driver.quit()
