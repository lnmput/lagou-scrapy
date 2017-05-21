# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime

from Yangzie.items import LagouItemLoader, LagouItem
from Yangzie.common.helper import get_md5



class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com']

    rules = (
        Rule(LinkExtractor(allow=("zhaopin/.*",)), follow=True),
        Rule(LinkExtractor(allow=("gongsi/j\d+.html",)), follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )

    def __init__(self):




    def parse_job(self, response):
        item_loader = LagouItemLoader(item=LagouItem(), response=response)
        item_loader.add_css("title", ".job-name::attr(title)")
        item_loader.add_value("url", response.url)
        item_loader.add_value('url_id', get_md5(response.url))
        item_loader.add_css('salary', '.job_request .salary::text')
        item_loader.add_xpath('city', "//*[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath('work_years', "//*[@class='job_request']/p/span[3]/text()")
        item_loader.add_xpath('degree_need', "//*[@class='job_request']/p/span[4]/text()")
        item_loader.add_xpath('types', "//*[@class='job_request']/p/span[5]/text()")
        item_loader.add_css('publish_time', '.publish_time::text')
        item_loader.add_css('tags', '.position-label li::text')
        item_loader.add_css('descs', '.job_bt div')
        item_loader.add_css('address', '.work_addr')
        item_loader.add_css('company_url', '#job_company dt a::attr(href)')
        item_loader.add_css('company_name', '#job_company dt a img::attr(alt)')
        item_loader.add_value('created_at', datetime.now())

        job_item = item_loader.load_item()
        return job_item
