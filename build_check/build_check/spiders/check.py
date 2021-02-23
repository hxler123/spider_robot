import re
from urllib import parse
import datetime

import scrapy
from scrapy.selector import Selector

class CheckSpider(scrapy.Spider):
    name = "check"
    # today = datetime.date.today()
    today = "2021-02-23"
    url = "http://10.80.1.174:8090/agora_sdk/2.7.1.2/nightly_build/" + today
    start_urls = [url]


    def parse(self, response):
        res = response.xpath('//a/text()').getall()[1:]
        if "default" not in res:
            for i in res:
                yield scrapy.Request(url=parse.urljoin(response.url,i))
        else:
            for i in res:
                platform = response.url.split("/")[-2]
                yield scrapy.Request(url=parse.urljoin(response.url,i+'/'),
                                    callback=self.check,
                                    meta={"branch": i, "platform": platform})

    def check(self, response):
        branch = response.meta.get("branch")
        platform = response.meta.get("platform")
        res = response.xpath('//a/text()').getall()[1:]
        if branch == "audio_only":
            if platform == "android":
                check_result = True
                a = "Agora_WayangAudio_for_Android"
                c = response.text
                b = re.findall(r"Agora_WayangAudio_for_Android.*apk</A>",response.text)
                print()
                if b:
                    pass
                else:
                    check_result = False
                    print("====================hxl==================")
                


            