from selenium import webdriver
from pyquery import PyQuery as pq
import time

# driver = webdriver.Chrome()

driver_path = 'C:\\Users\\zhaoyp\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
# 创建Chrome对象,有界面
driver = webdriver.Chrome(driver_path)

driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=广州,GZQ&ts=洛阳,LYF&date=2019-10-10&flag=N,N,Y")
driver.maximize_window()

time.sleep(2)
a = "window.scrollTo(0,800);"
b = "window.scrollTo(0,1600);"
c = "window.scrollTo(0,3200);"

driver.execute_script(a)
time.sleep(1)
driver.execute_script(b)
time.sleep(1)
driver.execute_script(c)
time.sleep(1)


def start():
    print("开始")
    label = driver.find_element_by_xpath('//*[@id="queryLeftTable"]')
    # print(label)

    aaa()


def aaa():
    html = driver.page_source
    row = driver.find_elements_by_tag_name('tr')
    list = []
    for i in row:
        j = i.find_elements_by_tag_name('td')
        for item in j:
            text = item.text
            if text != "":
                list.append(text)
    # print(list)
    # print(html)
    doc = pq(html)
    qq = doc('.t-list tbody tr').items()

    j = 1
    for a in range(len(list)):

        for i in qq:

            if i.find('.train').text() != "":
                # res = driver.find_element_by_xpath('//*[contains(@id,"SWZ_")]').text

                qq_data = {
                    "车次": i.find('.train').text().split("\n")[0],
                    "出发站到达站": i.find('.cdz').text(),
                    "出发时间到达时间": i.find('.cds').text(),
                    "历时": i.find('.ls').text(),
                    "商务座": list[j],
                    "一等座": list[j+1],
                    "二等座": list[j+2],
                    "高级软卧": list[j+3],
                    "软卧": list[j+4],
                    "动卧": list[j+5],
                    "硬卧": list[j+6],
                    "软座": list[j+7],
                    "硬座": list[j+8],
                    "无座": list[j+9],

                }

                print(qq_data)
                j += 13


def main():
    start()


if __name__ == '__main__':
    main()
