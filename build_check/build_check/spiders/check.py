import re
from urllib import parse

import scrapy
from scrapy.selector import Selector

class CheckSpider(scrapy.Spider):
    name = "check"
    start_urls = [
        "http://10.80.1.174:8090/agora_sdk/2.7.1.2/nightly_build/2021-02-23/"
    ]

    def parse(self, response):
        platformList = response.xpath('//a/text()').getall()[1:]
        for platform in platformList:
            yield scrapy.Request(url=parse.urljoin(response.url,platform))