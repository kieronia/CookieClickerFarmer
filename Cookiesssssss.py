from selenium import webdriver
import sys
import pathlib
import time
import os
from colorama import Fore, init, Back, Style
init(convert=True)

driver = webdriver.Chrome(executable_path= r'C:\Users\Kieronia\downloads\chromedriver.exe') #specify path here - download the executable at https://chromedriver.chromium.org/downloads

driver.get("https://orteil.dashnet.org/cookieclicker/")
os.system("title  [Loadinggg uppp...]")
time.sleep(3)
os.system("cls")
os.system(f"title  [Press ENTER to start!]")
input(f"{Fore.CYAN}Press enter to start clicking!\nMake a text file called 'pause.txt' to pause.\nThen return to console and press enter to continue.\nHave fun!\n>")
os.system("cls")


count = int(0)
overallcount = int(0)
while True:
    current = driver.find_element_by_xpath('//*[@id="cookies"]').text
    os.system(f"title  [{overallcount} Clicks Sent!]")
    driver.find_element_by_xpath('//*[@id="bigCookie"]').click()
    count = count + 1
    overallcount = overallcount+1
    os.system(f"title  [{overallcount} Clicks Sent!]")
    if count > 50:
        #print(f"{Fore.GREEN}[+] 50 Clicks Sent!")
        print(f"{Fore.GREEN}[+]Total Cookies - {current}   \n[+]Clicks Sent! - {overallcount} " )# i use the 50 as a timer system aha.
        count = 0
    else:
        pass
    file = pathlib.Path("pause.txt")
    if file.exists ():
        input(f"{Fore.RED}[!] You paused - Press enter to continue!")
        os. remove("pause.txt")
    else:
        pass
        

        
