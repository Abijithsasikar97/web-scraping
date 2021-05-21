import requests
import json
# import csv
from selenium import webdriver

#getting cookies dynamically with selenium and chromedriver
def get_session_cookies():
    driver = webdriver.Chrome(executable_path="/usr/lib/chromium-browser/chromedriver")
    driver.get("https://www.nseindia.com")
    cookies = driver.get_cookies()
    cookie_dict ={}
    with open('cookies', 'w') as line:
        for cookie in cookies:
            cookie_dict[cookie['name']] = cookie['value']
        line.write(json.dumps(cookie_dict))
    driver.quit()
    return cookie_dict

url = "https://www.nseindia.com/api/quote-derivative?symbol=RELIANCE"
#below headers wants to changed for every website according to their header.
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36', "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Accept-Encoding": "gzip, deflate, br"}

try:
    print("Reading from file")
    cookie_dict = json.loads(open('cookies').read()) #reading from file
except Exception as e:
    print("Error in reading cookies")
    cookie_dict = get_session_cookies()

session = requests.Session()

for cookie in cookie_dict:
    if cookie == "bm_sv":
        session.cookies.set(cookie, cookie_dict[cookie])

#if cookies expired again getting dynamically by calling the above function
try:
    r = session.get(url, headers = headers).json()
    print(r)
except Exception as e:
    print("Error in reading cookies")
    cookie_dict = get_session_cookies()
    for cookie in cookie_dict:
        if cookie == "bm_sv":
                session.cookies.set(cookie, cookie_dict[cookie])
    r = session.get(url, headers = headers).json()
    print(r)

filename = "scrapped_data.json"
with open(filename, 'w') as jsonfile:
    json_object = json.dumps(r)
    jsonfile.write(json_object)
