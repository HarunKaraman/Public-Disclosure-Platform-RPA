# -*- coding: utf-8 -*-
"""
Fetch and Analyse for Personal Data from Public Disclosure Platform

September 2021

@project manager : Seha Solakoğlu
@author          : Harun Karaman
"""
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import wget
import time
#import datetime
import glob
#from pandas import DataFrame as df

def getwdandcwd():
    scriptcurrentdirectory = os.path.dirname(os.path.realpath(__file__))
    os.chdir(scriptcurrentdirectory)

def analyse_documents(path):
    try:
        for filename in glob.glob(path+'\*.doc', recursive=True):
            #print(filename)  # print file name
            #f = open(filename)
            #content = f.read()
            #print(content)
            print('in progress')
    except:
        print('in progress')

def open_last_5_notifications():
    #Open Last 5 announcement page
    browser.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/a').click()

    #ENERJISA ENERJI A.S Fetch Last 5 Announcements 
    try:
        #1
        print("1.Bildirim Açılıyor.")
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[7]/div/div/div[4]/div/disclosure-list/div/div/div/div[1]/disclosure-list-item[1]/div').click()
        #Download as word
        #webdriver.ActionChains(browser).send_keys(Keys.END).perform()
        download_file_link1 = browser.find_element_by_partial_link_text('Word').get_attribute('href')
        print("1.Bildirim WORD Şeklinde Kaydediliyor.")
        time.sleep(1)
        wget.download(download_file_link1)
        webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    except: print("1.Bildirimde hata alındı.")
    
    try:
        #2
        print("2.Bildirim Açılıyor.")
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[7]/div/div/div[4]/div/disclosure-list/div/div/div/div[1]/disclosure-list-item[2]/div').click()
        #Download as word
        #webdriver.ActionChains(browser).send_keys(Keys.END).perform()
        download_file_link2 = browser.find_element_by_partial_link_text('Word').get_attribute('href')
        print("2.Bildirim WORD Şeklinde Kaydediliyor.")
        time.sleep(1)
        wget.download(download_file_link2)
        webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    except:print("2.Bildirimde hata alındı")
    
    try:    
        #3
        print("3.Bildirim Açılıyor.")
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[7]/div/div/div[4]/div/disclosure-list/div/div/div/div[1]/disclosure-list-item[3]/div').click()
        #Download as word
        #webdriver.ActionChains(browser).send_keys(Keys.END).perform()
        download_file_link3 = browser.find_element_by_partial_link_text('Word').get_attribute('href')
        print("3.Bildirim WORD Şeklinde Kaydediliyor.")
        time.sleep(1)
        wget.download(download_file_link3)
        webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    except:print("3.Bildirimde hata alındı.")
    
    try:
        #4
        print("4.Bildirim Açılıyor.")
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[7]/div/div/div[4]/div/disclosure-list/div/div/div/div[1]/disclosure-list-item[4]/div').click()
        #Download as word
        #webdriver.ActionChains(browser).send_keys(Keys.END).perform()
        download_file_link4 = browser.find_element_by_partial_link_text('Word').get_attribute('href')
        print("4.Bildirim WORD Şeklinde Kaydediliyor.")
        time.sleep(1)
        wget.download(download_file_link4)
        webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    except: print("4.Bildirimde hata alındı.")
    
    try:
        #5
        print("5.Bildirim Açılıyor.")
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[7]/div/div/div[4]/div/disclosure-list/div/div/div/div[1]/disclosure-list-item[5]/div').click()
        #Download as word
        #webdriver.ActionChains(browser).send_keys(Keys.END).perform()
        download_file_link5 = browser.find_element_by_partial_link_text('Word').get_attribute('href')
        print("5.Bildirim WORD Şeklinde Kaydediliyor.")
        time.sleep(1)
        wget.download(download_file_link5)
        webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
    except:("5.Bildirimde hata alındı.")
    
    try:
        print("Son 5 bildirim kaydedildi.")
        #analyse_documents(os.getcwd())
    except:
        print("Fonksiyonun çağrılmasında hata alındı.")
        
    
def open_browser_and_navigate(link):
    global browser
    getwdandcwd()
    kap_url = link
    print(link)
    #Setting up webdriver and navigate to Enerjisa Enerji A.S page
    try:
        print("WEBDriver Başlatılıyor.")
        browser = webdriver.Chrome(r"\chromedriver_new.exe")
        browser.set_window_position(-10, 0)
        browser.set_window_size(720, 700)
        browser.get(kap_url)
        browser.implicitly_wait(5)
        open_last_5_notifications()
    except: print("Webdriver'ın açılmasında hata alındı.")

def start():
    print("KAP Bildirimi - RPA Çalıştırıldı.")
    time.sleep(2)

# The main purpose of this script is to check 
# whether public companies traded in Borsa Istanbul 
# contain personal data on the last 5 notifications 
# they have made to the Public Disclosure Platform.

#https://www.kap.org.tr/tr/sirket-bilgileri/ozet/4028e4a140e95bea0140ee33bff201cd
#https://www.kap.org.tr/tr/sirket-bilgileri/ozet/3494-enerjisa-enerji-a-s
if __name__ == "__main__":
    open_browser_and_navigate("https://www.kap.org.tr/tr/sirket-bilgileri/ozet/4028e4a1422d98690142bceaa31957cf")