from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

def err():
    print('出了点问题，建议您看看自动打开的Chrome页面')

op = webdriver.ChromeOptions()
op.add_experimental_option('excludeSwitches', ['enable-logging'])
op.add_argument("--log-level=3")
op.add_argument("--disable-logging")

driver = webdriver.Chrome(options=op)
driver.implicitly_wait(5)


driver.get('https://qun.qq.com/#/login')

try:
    iframe = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe)
    sleep(2 + 0.001 * randint(153, 524))
    driver.find_element(By.CLASS_NAME, 'face').click()
except Exception:
    err()


sleep(2 + 0.001 * randint(153, 524))
driver.get('https://qun.qq.com/#/member-manage/base-manage')
try:
    if driver.find_elements(By.XPATH, "//*[starts-with(@class, '_logout_')]") == []:
        print('自动登录失败！需要手动登录。')
except Exception:
    err()
    print('自动登录失败！需要手动登录。')

print('请在登录成功后，在浏览器窗口中手动通过下拉菜单选择指定的群')
answer = input('是否已准备好读取群成员列表 (Y/n): ')
if(answer == 'N' and answer == 'n'):
    driver.quit()
    quit()

page_number = 1
try:
    page_number = int(driver.find_element(By.CLASS_NAME, 't-input-adornment__text').text.strip('/').strip('页').strip())
except Exception:
    err()

for i in range(page_number):
    driver.get('https://qun.qq.com/#/member-manage/base-manage')
    try:
        userInfos = driver.find_elements(By.XPATH, "//*[starts-with(@class, '_userInfo_')]")
        GroupCards = driver.find_elements(By.XPATH, "//*[starts-with(@class, '_nickName_')]")
    except Exception:
        err()

    for j in range(10):
        try:
            userInfo = userInfos[j].find_elements(By.TAG_NAME, 'p')
        except Exception:
            err()
        
        QQ_NickName = userInfo[0].text
        QQ_UIN = userInfo[1].text.strip('QQ:')
        QQ_GroupCard = GroupCards[j].text
        print(QQ_UIN+',\t\t'+QQ_NickName+',\t\t'+QQ_GroupCard)
    
    driver.find_element(By.CLASS_NAME, 't-pagination__btn.t-pagination__btn-next').click()
    sleep(2 + 0.001 * randint(153, 524))

driver.quit()
quit()