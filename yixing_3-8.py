from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
############################################
###变量区
############################################
a_2 = '坏的光猫机顶盒、光模块、皮线、网线跳线这些我都要'
a_1 = '很早以前坏的光猫机顶盒，很多人都丢垃圾桶，'
a_3 = '皮线、光模块、网线有吗'
a_4 = '我在贵阳，你在哪里'
a_5 = '贵州地区内，我可以上门服务'
a_6 = '我找到你不容易，挥手即来，现金上门'
a_7 = '老铁，压力很大，希望能够和合作，赚点生活费'
a_8 = '你还在电信里面上班吗？'
a_9 = '我做的是废旧回收，易信朋友圈有我收的东西'
a_10 = '我发的这个消息不知道能不能收到，如果收的到，就回复我下，我给你发和2位数的红包'
a_12 = '老板，你上班为了养家，我也是，最近生意不好，你帮关照我下呗？'
a_11 = '你有我微信吗？ 我手机号码名字上有，希望合作'
a_13 = '光模块坏了咋办'
a_14 = '如果收的到就回复我下，我给你发和2位数的红包，不知道系统会不会屏蔽消息'
a_15 = '电信、移动、联通的光猫我都在收'
a_16 = '易信和微信没什么区别。也可以看朋友圈，看下我的朋友圈呗'
a_17 = '在有爱的地方不要讲道理，在赚钱的地方努力赚钱'
a_18 = '哪里有猫呀，光猫好坏、坏旧都收'
a_19 = '嗨，老板，在吗'
a_20 = '我基本都住在贵阳。你也可以把东西带过来，来贵阳一起玩哟'
a_22 = '赚钱有什么好方法吗'
a_21 = '我在易信看到你的'
a_23 = '我找到你我容易吗'
a_24 = '我在贵阳，贵州哪里都可以去'
a_25 = '生活都是很艰难，相互帮助'
a_26 = '网线有吗'
a_27 = '快乐工作，快乐赚钱'
a_28 = '高清线你有吗'
a_29 = '真想去你们那上班，去收光猫机顶盒'
a_30 = '能帮介绍一个活路吗'
a_32 = '我在等你？赚生活费'
a_31 = '哥，很想和你做朋友'
a_33 = '怎么称呼你呀'
a_34 = '我们一直都在一起，只是你还不认识我'
a_35 = '二手电源有吗'
a_36 = '你也可以看下我朋友圈'
a_37 = '易信让我们认识，你有我电话吗'
a_38 = '哪里有猫呀，带光的猫'
a_39 = '改天我去你那找你'
a_40 = '光猫有吗？光模块、网线、电源线三色线也要'
keys=[a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9, a_10, a_11, a_12, a_13, a_14, a_15, a_16, a_17, a_18, a_19, a_20,
a_21, a_22, a_23, a_24, a_25, a_26, a_27, a_28, a_29, a_30, a_31, a_32, a_33, a_34, a_35, a_36, a_37, a_38, a_39, a_40
      ]
times=[i for i in range(30,260) ]
a=0
############################################
###启动区
############################################

driver =webdriver.Chrome(executable_path="/Users/apple/Documents/chromedriver")
driver.get('https://web.yixin.im/?&kick=1')
driver.implicitly_wait(30)#扫码等待时间
driver.maximize_window()#窗口最大化

############################################
###列表加载区
############################################
driver.find_element_by_xpath('//i[@class="u-icn u-icn-user"]').click()
users=driver.find_elements_by_xpath('//li[@data-res-type="1"]')#获取通讯录列表
print('初始化列表内个数是：',len(users))
for i in range(5):
    for user in users[a:]:
        ActionChains(driver).send_keys(user)
        ActionChains(driver).move_to_element(user).click(user).perform()
        a+=1
        print('坐标-------是{}-------，名称为【{}】'.format(a,user.find_element_by_xpath('./div[2]/div').text.replace('\r','').replace('\n','')))#打印日志
        #time.sleep(1)
        """上面是加载列表中的位置"""
    users=driver.find_elements_by_xpath('//li[@data-res-type="1"]')
    #print("**************")#打印分割符号
    #print(len(users))#打印列表内元素数量


print("*******易信通讯录列表加载完毕*******")#打印分割符号
print('列表加载总数量：',len(users))

############################################
###发送文本区域
############################################

print("列表已经加载完成现在开始发送消息")
a_data = 0
num_2=int(input("请输入开始位置"))
while True:
    time.sleep(1)
    users=driver.find_elements_by_xpath('//li[@data-res-type="1"]')#获取通讯录列表
    time.sleep(1)
    wang_12 = num_2 + a_data - 1
    user=users[wang_12]
    try:
        driver.execute_script("arguments[0].scrollIntoView();",user) #对齐窗口
        user.click()#点击元素
        user_name=user.find_element_by_xpath('./div[2]/div').text#获得元素名字
        driver.find_element_by_xpath('//textarea[@class="j-flag"]').send_keys(random.choice(keys))#随机发生内容
        driver.find_element_by_xpath('//span[@class="u-btn u-btn-c3"]').click()#点击发送
        print('坐标---{}----名称为：【{}】已发送完毕，----发送时间【{}】---'.format(num_2+a_data, user_name.replace('\r','').replace('\n',''), time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())))#打印日志
        time.sleep(random.choice(times))#间隔时间的变量
        a_data+=1
    finally:
        #print("内部常识失败马上重新刷新li")
        time.sleep(3)


