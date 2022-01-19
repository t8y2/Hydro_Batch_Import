# @Time    : 2022/1/19
# @Author  : Wiz1Code
# @FileName: 有头浏览器导入Hydro

import time
from selenium import webdriver

web = webdriver.Edge() 
web.get("http://"http://url/p/problem/import/syzoj") #此处填写自己的OJ URL

print("请输入您想从SYZOJ中导入的起始PROBLEM ID")
beg = int(input())

print("请输入您想从SYZOJ中导入的结束PROBLEM ID")
ed = int(input())

print("请输入要定义的起始编号")
pos = int(input())

web.get("http://url/problem/import/syzoj)  #此处填写你自己的OJ url 

web.maximize_window() #将浏览器最大化显示
print("已全屏")

time.sleep(1)

web.find_element_by_name("uname").send_keys("xxx")  #此处填写用户名
web.find_element_by_name("password").send_keys("xxxxx")   #此处填写密码

time.sleep(1)

web.find_element_by_xpath("/html/body/div[2]/div[4]/div/div/div/form/div[5]/div/div/input[2]").click()

print("登录成功")

time.sleep(1)

for i in range(beg,ed):
    url = "https://syzoj.com/problem/"  
    url += str(i)

    pid = "P" + str(pos)  #默认编号为P开头，可自由更改
    
    web.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div/div/form/div[1]/div[1]/label/input").send_keys(url)
    web.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div/div/form/div[1]/div[2]/label/input").send_keys(pid)
   
    web.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/div/div/form/div[2]/div/button[1]").click()
    web.back();
    print("成功从SYZOJ导入第%s题,定义题目编号为:%s" %(i, pid))
    pos += 1

web.close()
