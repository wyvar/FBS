from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from static.parms import *
import time
from file_manage import *
from datetime import date
from getpass import getpass

class Error(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message

class Mobile_fbBot():
    def __init__(self):
        self.URL_Mobile_Face = URL_Mobile_Face
        self.URL_Mobile_FList = URL_Mobile_FList
        self.URL_Mobile_Active_FList = URL_Mobile_Active_FList
        self.URL_Mobile_Profile = URL_Mobile_Profile
        self.cookie = cookie
        self.time_delay = time_delay
        self.mail = mail
        self.pwd = pwd
        self.friend_list = friend_list
        self.friend_downloaded = friend_downloaded

        

    def insert_cookies(self, URL = URL_Mobile_Face, cookie= cookie):
        driver.get(URL)
        driver.add_cookie(cookie)

    def get_cookie(self,URL = URL_Mobile_Face, time_delay = time_delay,cookie=cookie):
        driver.get(URL)
        time.sleep(time_delay)
        driver.find_element_by_id("accept-cookie-banner-label").click()
        self.cookie = driver.get_cookies()
        time.sleep(time_delay)

    def insert_login_info(self, mail =mail, pwd=pwd):
        if self.mail == "" or self.pwd =="":
            print("Remember - you can always enter your Email and password in params.py \n")
            self.mail = input("Enter your email:        ")
            self.pwd = getpass("Enter your password:     ")
            print("\n")
        else:
            print("Email and Password is set \n Continue...")

    def login(self, URL=URL_Mobile_Face, mail=mail, pwd=pwd, time_delay = time_delay):
        try:
            driver.get(URL_Mobile_Face)
            time.sleep(self.time_delay)
            username = driver.find_element_by_name("email")
            driver.implicitly_wait(implicity_delay)
            username.send_keys(self.mail)
            password = driver.find_element_by_name("pass")
            driver.implicitly_wait(implicity_delay)
            password.send_keys(self.pwd)
            driver.find_element_by_name('login').click()
            time.sleep(time_delay)
            check = driver.current_url()
            if check == URL_Mobile_Face_main:
                print("You're logged as: " + self.mail)
            else:
                error = "Wrong pass or mail"
                raise error
        except BaseException as error:
            print(error)

    def scroll_fix(self, time_delay = time_delay):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.implicitly_wait(implicity_delay)
        time.sleep(time_delay)


    def create_f_list(self, URL_Mobile_FList = URL_Mobile_FList):
        driver.get(URL_Mobile_FList)
        self.scroll_fix()
        self.scroll_fix()
        for lists in driver.find_elements_by_class_name("_2pit"):
            for person in lists.find_elements_by_tag_name("h3"):
                #data = str(person.find_element_by_class_name("_5pxc").text)
                need1 = str(person.text)
                self.friend_list.append(need1)
                create_file(need1)
            print(friend_list)

    def get_active_list(self, friend_list = URL_Mobile_Active_FList, friend_downloaded = friend_downloaded):
        driver.get(URL_Mobile_Active_FList)
        
        # {NAME: START_ACTIVE_TIME }
        today = date.today()
        date_format = today.strftime("%d/%m/%Y")
        for person in driver.find_elements_by_class_name("buddylistItem"):
            name = str(person.find_element_by_class_name("title").text)
            t =time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(name)

            if person not in friend_downloaded:
                friend_saved[person] = current_time
        print(friend_downloaded)
        f_diffrence = set(friend_saved.keys()).difference(set(friend_downloaded))

        for person in f_diffrence:
            dict_cont = {'date':date_format, 'start':friend_saved.pop(person),'end':current_time}
            print(person.text + " : " )
            print(dict_cont)
            #add_to_file(person ,dict_cont)

    def create_log_info(self, name,active):
        today = date.today()
        date_format = today.strftime("%d/%m/%Y")
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        #print(name)
        dict_cont = {'date':date_format,'time':current_time ,'active':active}
        #print(dict_cont)
        return dict_cont

