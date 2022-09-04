from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import msteamn
from datetime import datetime
join,subj,stt=msteamn.day_check()
print(subj)
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--disable-extensions")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 2
  })
d=webdriver.Chrome(chrome_options=opt)
d.get("https://www.microsoft.com/en-in/microsoft-365/microsoft-teams/log-in")
se=d.find_element_by_xpath('//a[@class="c-button f-primary ow-slide-in ow-slide-in-2 xs-ow-mr-0 ow-mt-25 ow-txt-trans-upper"]')
action=ActionChains(d)
action.click(se).perform()
c=d.current_window_handle
tl=d.window_handles
for i in tl:
    if c!=i:
        d.switch_to.window(i)
        break
time.sleep(5)
d.find_element_by_id("i0116").send_keys("kumailtaqi1120t@gmail.com")
d.find_element_by_id("idSIButton9").click()
time.sleep(5)
d.find_element_by_id("i0118").send_keys("5#bot@1214")
time.sleep(5)
d.find_element_by_id("idSIButton9").click()
time.sleep(5)
d.find_element_by_xpath('//a[@class="use-app-lnk"]').click()
time.sleep(10)
d.find_element_by_xpath('//a[@class="guest-license-error-dropdown ts-sym"]').click()
d.find_element_by_xpath('??a[@ng-repeat="tenant in ::glec.redeemedTenants track by tenant.tenantId"]').click()
time.sleep(5)
d.find_element_by_xpath('//a[@class="ts-btn ts-btn-primary guest-license-error-button""]').click()
time.sleep(20)
s="]"
st='//span[@title="'+subj+'"'+s
print(st)
d.find_element_by_xpath(st).click()
time.sleep(12)
spl=stt.split(":")
ti= datetime.now()
print(ti)
t2=ti.split(":")
if join==1:
    while int(t2[0])==int(spl[0]) and int(t2[1])<=int((spl[1])+30):
        ti= datetime.now()
        t2=ti.split(":")
        if(d.find_element_by_xpath('//span[@aria-label="Join"]')):
            d.find_element_by_xpath('//span[@aria-label="Join"]').click()
            time.sleep(5)
            d.find_element_by_xpath('//span[@title="Turn camera off"]').click()
            d.find_element_by_xpath('//span[@title="Mute microphone"]').click()
            time.sleep(5)
            d.find_element_by_xpath('//button[@track-name="333"]').click()
        else:
            d.navigate().refresh();
