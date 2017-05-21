# -*- coding: utf-8 -*-

import requests
from scrapy.selector import Selector
from fake_useragent import UserAgent
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='root', db='test', charset='utf8', use_unicode=True)
cursor = conn.cursor()
ua = UserAgent()


# 一个爬虫,从西刺爬取ip并放入数据库
def get_ips():

    headers = {'User-Agent' : ua.random}
    for i in range(1568):
        re = requests.get('http://www.xicidaili.com/nn/{0}'.format(i), headers=headers)
        selector = Selector(text=re.text)
        print(selector)
        all_trs = selector.css('#ip_list tr')
        ip_lists =[]
        for tr in all_trs[1:]:
            print(tr)
            speed = tr.css('.bar::attr(title)').extract_first(0)
            if speed:
                speed = float(speed.split("秒")[0])
            all_text = tr.css('td::text').extract()

            ip = all_text[0]
            port = all_text[1]
            type = all_text[5]
            ip_lists.append((ip, port, type, speed))
            print(ip_lists)



        for ip_info in ip_lists:
            cursor.execute(
                "insert xiciip (ip, type , port, speed) values('{0}', 'http', '{1}', '{2}')".format(
                    ip_info[0],ip_info[1],ip_info[3]
                )
            )
            conn.commot()


class GetIP(object):

    # 删除无用的ip
    def delete_ip(self, ip):
        sql= """
        DELETE FROM xiciip WHERE ip = '{0}'
        """.format(ip)
        cursor.execute(sql)
        conn.commit()
        return True

    # 判断ip是否可用
    def judge_ip(self, ip, port):
        http_url = 'http://www.baidu.com'
        proxy_url = 'http://{0}:{1}'.format(ip, port)
        try:
            proxy_dict = {
                'http':proxy_url
            }
            response = requests.get(http_url, proxies=proxy_dict)
            return True
        except Exception as e:
            print('invalid ip and port')
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print('effective ip')
                return True
            else:
                print('invalid ip and port')
                self.delete_ip(ip)
                return False

    #从数据库中随机获取ip
    def get_random_ip(self):
        sql= """
        SELECT ip, port FROM xiciip ORDER BY RAND() LIMIT 1
        """
        result = cursor.execute(sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            re = self.judge_ip(ip, port)
            if re:
                return 'http://{0}:{1}'.format(ip, port)
            else:
                return self.get_random_ip()


if __name__ == "__main__":
    get_ip = GetIP()
    get_ip.get_random_ip()