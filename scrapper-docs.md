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