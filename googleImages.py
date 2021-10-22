import os
import sys
import time
import random 

try:
    import pip
except:
    print('PIP NOT INSTALLED!!! Kindly install pip correctly and then try again')
    time.sleep(2.5)
    sys.exit()
try:
    import requests #pip install requests
except:
    print('Request module not installed! Installing automatically.')
    os.system('python -m pip install requests')
    time.sleep(5)
    import requests #pip install requests

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as chromeOpt
    from selenium.webdriver.chrome.service import Service as chromeSrv
    from selenium.webdriver.common.by import By
except:
    print('Selenium module not installed! Installing automatically.')
    os.system('python -m pip install selenium')
    time.sleep(5)
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options as chromeOpt
    from selenium.webdriver.chrome.service import Service as chromeSrv
    from selenium.webdriver.common.by import By


search=input("[+] Search: ")
if(search==""):
    print("No input available! Exiting the program.")
    time.sleep(3)
    sys.exit(0)
try:
    maxCount=int(input("[+] Max number of images: "))
    if(search==""):
        print("No input available! Exiting the program.")
        time.sleep(3)
        sys.exit(0)
except:
    print("Invalid input! Exiting the program.")
    time.sleep(3)
    sys.exit(0)
url="http://www.google.com/search?q="+search.replace(" ","+")+"&tbm=isch"

# Getting all paths ready
path_driver=os.path.join(os.getcwd(),"chromedriver.exe") # Web Driver
path_browser=os.path.join(os.getcwd(),"chrome-win\\chrome.exe") # Web Browser
path_saveDown=os.path.join(os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') ,"imgSearch") # Downloading Images Folder
if not os.path.isdir(path_saveDown):
    os.mkdir(path_saveDown)

# Getting the Driver ready
options = chromeOpt()
options.binary_location = path_browser
options.add_argument("headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = chromeSrv(path_driver)
driver = webdriver.Chrome(options=options, service=service)

driver.maximize_window();
driver.get(url)
driver.execute_script("window.scrollTo(0,0);")
time.sleep(2.5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight * 5);")
time.sleep(2.5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight * 10);")
time.sleep(2.5)

forImgClk = driver.find_elements(By.CSS_SELECTOR, 'a.wXeWr.islib.nfEiy')

headers_list = [
# Firefox 77 Mac
{"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Referer": "https://www.google.com/","DNT": "1","Connection": "keep-alive","Upgrade-Insecure-Requests": "1"},
# Firefox 77 Windows
{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Referer": "https://www.google.com/","DNT": "1","Connection": "keep-alive","Upgrade-Insecure-Requests": "1"},
# Chrome 83 Mac
{"Connection": "keep-alive","DNT": "1","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Sec-Fetch-Site": "none","Sec-Fetch-Mode": "navigate","Sec-Fetch-Dest": "document","Referer": "https://www.google.com/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"},
# Chrome 83 Windows 
{"Connection": "keep-alive","Upgrade-Insecure-Requests": "1","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "navigate","Sec-Fetch-User": "?1","Sec-Fetch-Dest": "document","Referer": "https://www.google.com/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9"}
]

count=1
for i in forImgClk:
    # pass
    i.click()
    time.sleep(1)
    print("Downloading next image...")
    try:
        imgElem = driver.find_element(By.CSS_SELECTOR,"img.n3VNCb")
        img_conn = requests.get(str(imgElem.get_attribute("src")),headers=random.choice(headers_list))
        img_type = str(img_conn.headers.get('content-type'))[str(img_conn.headers.get('content-type')).index("/")+1:]
    except:
        print("Error; skipping!")
        continue
    with open( path_saveDown + "\\" + str(count)+"."+img_type , "wb") as f:
        f.write(img_conn.content)
        f.close()
    time.sleep(  random.choice( [1,2,3] )  )
    count+=1
    if count>maxCount:
        break
    print("Downloaded.")

time.sleep(2)
driver.quit()
