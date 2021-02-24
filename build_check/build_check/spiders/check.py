import re
from urllib import parse
import datetime

import scrapy
from scrapy.selector import Selector
from common.platform import platforms

class CheckSpider(scrapy.Spider):
    name = "check"
    today = datetime.date.today().isoformat()
    url1 = "http://10.80.1.174:8090/agora_sdk/2.7.1.2/nightly_build/" + today
    url2 = "http://10.80.1.174:8090/agora_sdk/2.7.2/nightly_build/" + today
    start_urls = [url1,url2]

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
        current_branch = response.meta.get("branch")
        current_platform = response.meta.get("platform")
        for check_name in platforms[current_platform][current_branch].keys():
            check_string = platforms[current_platform][current_branch][check_name]
            check_string2 = re.compile(check_string)
            check_result = re.findall(check_string2, response.text)
            if bool(check_result) is False:
                print("==============={current_platform}_{current_branch}_{check_name}_Failed=============".format(
                      current_platform=current_platform, current_branch=current_branch, check_name=check_name))
            else:
                pass


            