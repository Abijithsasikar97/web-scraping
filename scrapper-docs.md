### webscraping with python using selenium.

#### Packages to install before running the scrapper.py
> INSTALL SELENIUM USING --> pip3 install selenium

## Important changes to be done for every website(VERY IMPORTANT);
1. Kindly open the website you want to scrape on chrome.
2. Right click on the website and open inspect.
3. Open network tab in inspect(Chrome Dev Tools).
4. Now copy and paste all the required accept header in the code in line 21
5. Below is the example code.
> headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36', "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Accept-Encoding": "gzip, deflate, br"}

### Code explanation
1. Actually the selenium webdriver is like a normal browser which at first it launch the website we want to scrape with the given link.
2. In our our code at first we get session coookies with get_session_cookies() function and write that cookies to cookies file which has the sessions cookies.
3. when every time we try to scrape the cookies the code first look into that cookies file and check whether the cookies expired or not.
4. If the cookies expired we are calling that get_session_cookies() function again and it will write over the old cookies in cookies file.
5. The most important part to be done in this code is we wanted to give the exact header as the header in the website wanted to scrape.
6. Why we want to give the exact header and why it is so important?
> If we didn't give the exact header as in the website nah the website will confrim that someone is trying to do something on website and it may leads to legal issue.
> This happening because actually the selenium webdriver lanch the website like normaly the user viewing the website and scrape.
> If we hitting the website without correct header leads to legal issues and sometimes your ip may gets blocked.