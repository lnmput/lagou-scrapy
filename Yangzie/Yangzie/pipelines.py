# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import time

class YangziePipeline(object):
    def process_item(self, item, spider):
        return item



def handle_error(self, failure, item, spider):
    print(failure)

class DbMysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'root', 'test', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = """
                 insert into lagou (url, url_id, title, salary, city, work_years, degree_need, types, publish_time, tags, descs, address, company_url, company_name, created_at) VALUES
                  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s )
                """
        self.cursor.execute(sql, (item['url'],item['url_id'],item['title'],item['salary'],item['city'],item['work_years'],item['degree_need'],item['types'],item['publish_time'],item['tags'],
                                  item['descs'],item['address'],item['company_url'],item['company_name'],item['created_at']))
        self.conn.commit()