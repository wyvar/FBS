from selenium import webdriver

#EDIT THIS PARMS
mail = ''
pwd= ''
profile_name=''
cookie = {'name':'',
'value': '',
'domain': 'facebook.com'
}

#EDIT THIS PARMS

URL_Mobile_FList='https://m.facebook.com/friends/center/friends/?mff_nav=1'
friend_downloaded= list()
friend_saved = dict()
URL_Mobile_Face = 'https://m.facebook.com/login.php?next=https%3A%2F%2Fm.facebook.com%2Fhome.php%3Frefsrc%3Dhttp%253A%252F%252Fwww.google.com%252F&refsrc=http%3A%2F%2Fwww.google.com%2F&_rdr'
URL_Mobile_Profile='https://m.facebook.com/'+ profile_name
URL_Mobile_Active_FList="https://m.facebook.com/buddylist.php"
URL_Mobile_Face_main="https://m.facebook.com/home.php?_rdc=1&_rdr"

URL_Mess = 'https://www.messenger.com/'
URL_Face_FList= 'https://www.facebook.com/'+ profile_name +'/friends'

cookie_popup_class = "_9fwi"
accept_all = 'data-cookiebanner="accept_button"'


friend_slector='//*[@id="root"]/div/div/div[3]/div[1]/div[2]/div/div[1]/h3'
friend_slector_fix='//*[@id="root"]/div/div/div/div'
friend_text_fix='./div[2]/div/div[1]/h3/a'
factive_selector='///a[1]/div/div[2]/div/strong'
sd='//*[@id="root"]/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/div[1]/h3/a2'
friend_list =[]

driver = webdriver.Chrome(executable_path="webdriver/chromedriver")

implicity_delay = 100       ###Delay depends on computer power
time_delay = 2              ###Delay depends onn internet + computer power
