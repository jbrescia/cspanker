from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import re
import time

driver_path = 'chromedriver.exe'
pause = WebDriverWait(driver_path, 30)

chrome_options = Options()
chrome_options.headless = False
chrome_options.add_argument("--window-size=1920,1200")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")


browser = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

try:
    browser.get('http://www.c-span.org')
    # browser.save_screenshot("nooooo.png")
    # Optional screenshot for debugging during development - remove later
    time.sleep(5)
    # Likely should replace time.sleep with webdriver.wait at some point
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    link_list = []
    for link in soup.find_all(href=re.compile('washington-journal')):
        link_list.append(link.get('href'))
    wjlink = str(link_list[0])
    browser.get('http:' + wjlink)


except:
    # browser.quit
    # currently disabled during development
    None
