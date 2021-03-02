import re
import datetime
import json

import scrapy
from scrapy.selector import Selector
from common.branch import branchDict
from  scrapy.crawler import Settings

class CheckSpider(scrapy.Spider):
    name = "build_check"

    custom_settings = {
        "ROBOTSTXT_OBEY": False,
        }

    def __init__(self, name=None, **kwargs):
        self.today = datetime.date.today().isoformat()
        super().__init__(name,**kwargs)

    def parse(self, response):
        pass

    def start_requests(self):
        for branch in branchDict.keys():
            platformDict = branchDict[branch]
            for pl in platformDict.keys():
                typeDict = platformDict[pl]
                for tp in typeDict.keys():
                    url = "http://10.80.1.174:8090/agora_sdk/{branch}/nightly_build/{today}/{platform}/{pkgType}/"
                    checkStringDict = typeDict[tp]
                    meta = {
                        "branch": branch,
                        "platform" : pl,
                        "pkgType": tp,
                        "checkStringDict": checkStringDict
                    }
                    url = url.format(branch=branch, today=self.today, platform=pl, pkgType=tp)

                    yield scrapy.Request(url=url, meta=meta, callback=self.parse_check)

    def parse_check(self, response):
        checkStringDict = response.meta.get("checkStringDict")
        branch = response.meta.get("branch")
        currentPkgType = response.meta.get("pkgType")
        currentPlatform = response.meta.get("platform")
        checkStringList = checkStringDict.items()
        for checkString in checkStringList:
            checkName = checkString[0]
            reString = re.compile(checkString[1], re.I)
            checkResult = re.findall(reString, response.text)
            if bool(checkResult) is False:
                webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=cba55469-7415-4280-926f-d38c2a8d7f23"
                content = "Branch: {branch}\nPlatform: {currentPlatform}\nType: {currentPkgType}\nPkg: {checkName}\n未出包\nlink:\n{link}"
                headers = {'Content-Type': 'application/json'}
                content = content.format(
                    branch=branch, currentPlatform=currentPlatform,
                    currentPkgType=currentPkgType, checkName=checkName, link = response.url
                )
                data = {
                    "msgtype": "text",
                    "text": {
                    "content": content,
                    "mentioned_mobile_list":[]}
                }
                data = json.dumps(data)

                yield scrapy.Request(url=webhook, method="post", headers=headers, body=data)
            else:
                pass