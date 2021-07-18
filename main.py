from bot import Mobile_fbBot 
import time

MFB = Mobile_fbBot()

try:
    MFB.insert_login_info()
    MFB.get_cookie()
    MFB.insert_cookies()
    MFB.login()
    #MFB.create_f_list()
    while(True):
        MFB.get_active_list()
        time.sleep(10)
        print("--------------------------------------------")
except BaseException as error:
    raise error
