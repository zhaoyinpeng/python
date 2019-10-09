import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = 'C:\\Users\\zhaoyp\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
# 创建Chrome对象,有界面
driver = webdriver.Chrome(driver_path)

# 无界面操作
# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome(executable_path=driver_path, options=option)

# 12306页面
evaluate = 'https://www.12306.cn/index/index.html'
driver.get(evaluate)
driver.maximize_window()

print('===============')
# 修改输入框中的值并查询 给元素赋值
fromStationText = driver.find_element_by_id('fromStationText')
driver.execute_script("arguments[0].value = '广州';", fromStationText)

toStationText = driver.find_element_by_id('toStationText')
driver.execute_script("arguments[0].value = '洛阳';", toStationText)

train_date = driver.find_element_by_id('train_date')
driver.execute_script("arguments[0].value = '2019-10-20';", train_date)

driver.execute_script("console.log('测试selenium，广州至洛阳的车');")
btn = driver.find_element_by_id('search_one')
print(btn)

time.sleep(3)
btn.click()

time.sleep(20)

# 使用完关闭浏览器，不然Chromedriver.exe 进程会一直在内存中
driver.quit()
