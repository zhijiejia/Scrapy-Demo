import scrapy
import random
from scrapy import Request
from project1.items import Project1Item

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com', 'baidu.com', '360.com', 'zhihu.com', 'csdn.net']
    start_urls = ['https://www.bilibili.com/']

    def parse(self, response):

        # hrefs = response.xpath('//div[@class="bili-video-card__info--right"]/a/@href').getall()
        # titles = response.xpath('//div[@class="bili-video-card__info--right"]//h3/@title').extract()
        # texts = response.xpath('//div[@class="bili-video-card__info--right"]//a[@class="bili-video-card__info--owner"]/span/text()').extract()

        # for href in hrefs:
        #     item = Project1Item()
        #     item['href'] = href
        #     yield item

        x = random.randint(1, 9)
        yield Request(url=f'https://www.bilibili.com/', callback=self.parse, dont_filter=True)