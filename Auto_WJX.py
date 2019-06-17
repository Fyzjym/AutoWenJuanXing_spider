#todo : 问卷自动填写。。。。。

import requests
import re
import time
import random

#answer
#submitdata : 1$3}2$1}3$2}4$1}5$1}6$2}7$3}8$3}9$3}10$4}11$3|4|5}12$2}13$2|4|7|9|11}14$4}15$2
"""
todo:答案，模型 
umm，一共十五道题

模型分析：
1. da学
       师大  内大 农业  工业 财经 
       34%   13％ 21%   17%  15%    

2.年纪分布
因为毕设发布者处于大三 ，因此周围环境为大三，结合参考硕论。
         1  2   3    4
即比例为 19% 21% 37% 23%

3.性别
因为发布者处于师范院校 ，因此男女比例稍偏，结合硕论。
          女  男
即比例为  65% 35％

4.专业属性
发布者处于工科学院，结合整个学校环境，结合硕论。
即
        文科  理科   工科   艺术    其他
        35％  22％   25%   15％    3% 

5.生源地
umm  没有合适的参考，只能根据硕论将城市比例调高
即
  生源地 
        城市  农村
        66%   34%

6.就业形势，近年来就业形势逐渐严峻，结合硕论。
        严峻  正常  容易  不了解
        58%  20%   18%   4％      

7.创业。。。
结合情况，结合硕论 
    创业 不创业
    26%  74%

8.想要的工作单位
结合硕论 
        外企  国企  政府机关  私营民营  自主创业
         28%   25%   35%      9%      3%

9.看中企业什么
结合硕论 
        公司规模  个人发展  待遇  公司名气  对人的重视程度
           20%    25%     28%       9%       18%


10.薪资要求
结合硕论
        3000-   3-6000  6-9000  9－12000 12000+
         1%       66%     21%      8%       4%

11.工作地域
结合硕论 
        沿海发达  内地大  东部中小 西部中小 边远。。
         37％     51%      3%      2％    7%
         
         
12.具有的素质 （最多三个）
   专业水平  心理素质  沟通能力  组织能力  适应能力 品德  
      74％    40%      59%      31%     46%    76%       tol = 326%
yici  23%     12%      18%      9%      14%    24%
      
      
13.影响决策
结合硕论 
        父母  老师  朋友  社会舆论  不受他人影响 其他
        22%   25%   8%      27%         12％    6%

14.影响五因素
结合硕论 
        能力 学历 专业  就业信息 实践经验   户口人口指标 
        57%  65% 48%     52%     84%     43%         tol = 421
        14   15  11      12      20      10
        社会关系 学习成绩 心理素质 
         34%     12%    26%    
         8       3      6
15.就业难的原因 
结合硕论 
        社会需求少 不公平现象 单位挑剔 毕业生挑剔  
        14%        19%      15%      27%
        信息发布不及时 沟通不畅 过度依赖学校 其他
        2%            5％      17%        1%
        
16.就业态度
结合硕论  
        先就业  先择业  考研   待业  创业  其他  
        43%     6%     38％   3%    4%   6%


"""


def sort_d(a, b, c):
    if a > b:
        a, b = b, a
        # print (a,b)
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c


def data_1():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 34):
        return 1
    elif (rate >= 35 and rate <= 48):
        return 2
    elif (rate >= 49 and rate <= 69):
        return 3
    elif (rate >= 70 and rate <= 86):
        return 4
    elif (rate >= 87 and rate <= 100):
        return 5


def data_2():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 19):
        return 1
    elif (rate >= 20 and rate <= 40):
        return 2
    elif (rate >= 41 and rate <= 77):
        return 3
    elif (rate >= 78 and rate <= 100):
        return 4

def data_3():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 65):
        return 2
    elif (rate >= 66 and rate <= 100):
        return 1

def data_4():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 35):
        return 1
    elif (rate >= 36 and rate <= 57):
        return 2
    elif (rate >= 58 and rate <= 82):
        return 3
    elif (rate >= 83 and rate <= 97):
        return 4
    elif (rate >= 97 and rate <= 100):
        return 5

def data_5():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 66):
        return 1
    elif (rate >= 67 and rate <= 100):
        return 2

def data_6():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 58):
        return 1
    elif (rate >= 59 and rate <= 78):
        return 2
    elif (rate >= 79 and rate <= 96):
        return 3
    elif (rate >= 97 and rate <= 100):
        return 4

def data_7():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 26):
        return 1
    elif (rate >= 27 and rate <= 100):
        return 2

def data_8():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 28):
        return 1
    elif (rate >= 29 and rate <= 53):
        return 2
    elif (rate >= 54 and rate <= 88):
        return 3
    elif (rate >= 89 and rate <= 97):
        return 4
    elif (rate >= 98 and rate <= 100):
        return 5

def data_9():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 20):
        return 1
    elif (rate >= 21 and rate <= 45):
        return 2
    elif (rate >= 46 and rate <= 73):
        return 3
    elif (rate >= 74 and rate <= 82):
        return 4
    elif (rate >= 83 and rate <= 100):
        return 5

def data_10():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 1):
        return 1
    elif (rate >= 2 and rate <= 67):
        return 2
    elif (rate >= 68 and rate <= 88):
        return 3
    elif (rate >= 89 and rate <= 96):
        return 4
    elif (rate >= 97 and rate <= 100):
        return 5

def data_11():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 37):
        return 1
    elif (rate >= 38 and rate <= 88):
        return 2
    elif (rate >= 89 and rate <= 91):
        return 3
    elif (rate >= 92 and rate <= 93):
        return 4
    elif (rate >= 94 and rate <= 100):
        return 5

def data_12_most_3():

    str = '1111111222233334445555566666666'
    data = random.choice(str)
    data1 = random.choice(str)
    data2 = random.choice(str)

    while(data1 == data):
        data1 = random.choice(str)

    while(data1 == data2 or data == data2):
        data2 = random.choice(str)

    order = sort_d(data,data1,data2)

    result = order[0]+"|"+order[1]+"|"+order[2]
    return result


def data_13():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 22):
        return 1
    elif (rate >= 23 and rate <= 47):
        return 2
    elif (rate >= 48 and rate <= 55):
        return 3
    elif (rate >= 56 and rate <= 82):
        return 4
    elif (rate >= 83 and rate <= 94):
        return 5
    elif (rate >= 95 and rate <= 100):
        return 6

def data_14_only_5():

        str = '111111111111112222222222222223333333333344444444444455555555555555555555666666666677777777888999999'
        data = random.choice(str)
        data1 = random.choice(str)
        data2 = random.choice(str)
        data3 = random.choice(str)
        data4 = random.choice(str)

        while (data1 == data):
            data1 = random.choice(str)

        while (data == data2 or data1 == data2):
            data2 = random.choice(str)

        while (data == data3 or data1 == data3 or data2 == data3):
            data3 = random.choice(str)

        while (data == data4 or data1 == data4 or data2 == data4 or data3 == data4):
            data4 = random.choice(str)

        list = [data, data1, data2, data3, data4]
        result = sorted(list)
        data = result[0] + "|" + result[1] + "|" + result[2] + "|" + result[3] + "|" + result[4]
        return data

def data_15():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 14):
        return 1
    elif (rate >= 15 and rate <= 33):
        return 2
    elif (rate >= 34 and rate <= 48):
        return 3
    elif (rate >= 49 and rate <= 75):
        return 4
    elif (rate >= 76 and rate <= 77):
        return 5
    elif (rate >= 78 and rate <= 82):
        return 6
    elif (rate >= 83 and rate <= 99):
        return 7
    elif (rate >= 100 and rate <= 100):
        return 8

def data_16():
    rate = random.randint(1,100)
    if (rate >= 1 and rate <= 43):
        return 1
    elif (rate >= 44 and rate <= 49):
        return 2
    elif (rate >= 50 and rate <= 87):
        return 3
    elif (rate >= 88 and rate <= 90):
        return 4
    elif (rate >= 91 and rate <= 94):
        return 5
    elif (rate >= 95 and rate <= 100):
        return 6





class WenJuanXing:
    def __init__(self, url):
        """
        :param url:要填写的问卷的url
        """
        self.wj_url = url
        self.post_url = None
        self.header = None
        self.cookie = None
        self.data = None

    def set_data(self):
        """
        这个函数中生成问卷的结果，可根据问卷结果，随机生成答案
        :return:
        """
        #上面十六个选项拼的 sumbitdata
        sumdata = "1$" + str(data_1()) + "}2$" + str(data_2()) + "}3$" + str(data_3()) + "}4$" + str(
            data_4()) + "}5$" + str(data_5()) + "}6$" + str(data_6()) + "}7$" + str(data_7()) + "}8$" + str(
            data_8()) + "}9$" + str(data_9()) + "}10$" + str(data_10()) + "}11$" + str(data_11()) + "}12$" + str(
            data_12_most_3()) + "}13$" + str(data_13()) + "}14$" + str(data_14_only_5()) + "}15$" + str(
            data_15()) + "}16$" + str(data_16())

        self.data = {
            'submitdata': sumdata
        }

    def set_header(self):
        """
        随机生成ip，设置X-Forwarded-For
        ip需要控制ip段，不然生成的大部分是国外的
        :return:
        """
        ip = '{}.{}.{}.{}'.format(211 ,138 , random.randint(88, 95), random.randint(0, 255))
        self.header = {
            'X-Forwarded-For': ip,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko\
                        ) Chrome/71.0.3578.98 Safari/537.36',
        }

    def get_ktimes(self):
        """
        随机生成一个ktimes,ktimes是构造post_url需要的参数，为一个整数
        :return:
        """
        return random.randint(15, 50)

    def get_response(self):
        """
        访问问卷网页，获取网页代码
        :return: get请求返回的response
        """
        response = requests.get(url=self.wj_url, headers=self.header)
        self.cookie = response.cookies
        return response

    def get_jqnonce(self, response):
        """
        通过正则表达式找出jqnonce,jqnonce是构造post_url需要的参数
        :param response: 访问问卷网页，返回的reaponse
        :return: 找到的jqnonce
        """
        jqnonce = re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}', response.text)
        return jqnonce.group()

    def get_rn(self, response):
        """
        通过正则表达式找出rn,rn是构造post_url需要的参数
        :param response: 访问问卷网页，返回的reaponse
        :return: 找到的rn
        """
        rn = re.search(r'\d{9,10}\.\d{8}', response.text)
        return rn.group()

    def get_id(self, response):
        """
        通过正则表达式找出问卷id,问卷是构造post_url需要的参数
        :param response: 访问问卷网页，返回的reaponse
        :return: 找到的问卷id
        """
        id = re.search(r'\d{8}', response.text)
        return id.group()

    def get_jqsign(self, ktimes, jqnonce):
        """
        通过ktimes和jqnonce计算jqsign,jqsign是构造post_url需要的参数
        :param ktimes: ktimes
        :param jqnonce: jqnonce
        :return: 生成的jqsign
        """
        result = []
        b = ktimes % 10
        if b == 0:
            b = 1
        for char in list(jqnonce):
            f = ord(char) ^ b
            result.append(chr(f))
        return ''.join(result)

    def get_start_time(self, response):
        """
        通过正则表达式找出问卷starttime,问卷是构造post_url需要的参数
        :param response: 访问问卷网页，返回的reaponse
        :return: 找到的starttime
        """
        start_time = re.search(r'\d+?/\d+?/\d+?\s\d+?:\d{2}', response.text)
        return start_time.group()

    def set_post_url(self):
        """
        生成post_url
        :return:
        """
        self.set_header()  # 设置请求头，更换ip
        response = self.get_response()  # 访问问卷网页，获取response
        ktimes = self.get_ktimes()  # 获取ktimes
        jqnonce = self.get_jqnonce(response)  # 获取jqnonce
        rn = self.get_rn(response)  # 获取rn
        id = self.get_id(response)  # 获取问卷id
        jqsign = self.get_jqsign(ktimes, jqnonce)  # 生成jqsign
        start_time = self.get_start_time(response)  # 获取starttime
        time_stamp = '{}{}'.format(int(time.time()), random.randint(100, 200))  # 生成一个时间戳，最后三位为随机数
        url = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID={}&t={}&starttim' \
              'e={}&ktimes={}&rn={}&jqnonce={}&jqsign={}'.format(id, time_stamp, start_time, ktimes, rn, jqnonce, jqsign)
        self.post_url = url  # 设置url
        print(self.post_url)

    def post_data(self):
        """
        发送数据给服务器
        :return: 服务器返回的结果
        """
        self.set_data()
        response = requests.post(url=self.post_url, data=self.data, headers=self.header, cookies=self.cookie)
        return response

    def run(self):
        """
        填写一次问卷
        :return:
        """
        self.set_post_url()
        result = self.post_data()
        print(result.content.decode())

    def mul_run(self, n):
        """
        填写多次问卷
        :return:
        """
        for i in range(n):
            time.sleep(random.randint(1,15))
            self.run()


if __name__ == '__main__':


    w = WenJuanXing('https://www.wjx.cn/jq/41489555.aspx')
    w.mul_run(1000)
