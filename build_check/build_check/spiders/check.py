import re
import datetime
import json

import scrapy
from scrapy.selector import Selector
from common.platform import PLATFORMS

class CheckSpider(scrapy.Spider):
    name = "check"
    TODAY = datetime.date.today().isoformat()

    def start_requests(self):
        for version in PLATFORMS.keys():
            url = "http://10.80.1.174:8090/agora_sdk/{version}/nightly_build/{today}/".format(
                version=version,today=self.TODAY
            )
            yield scrapy.Request(url=url, meta={"version":version}, callback=self.check_parse)

    def parse(self, response):
        pass

    def check_parse(self, response):
        version = response.meta.get("version")
        versionDict = PLATFORMS[version]
        for pl in versionDict.keys():
            branchDict = versionDict[pl]
            for br in branchDict.keys():
                url = response.url + pl + "/" + br + "/"
                checkStringDict = branchDict[br]
                yield scrapy.Request(url = url, callback=self.build_check,
                                    meta={"checkStringDict": checkStringDict,
                                          "version": version,
                                          "branch": br,
                                          "platform": pl})

    def build_check(self, response):
        checkStringDict = response.meta.get("checkStringDict")
        version = response.meta.get("version")
        currentBranch = response.meta.get("branch")
        currentPlatform = response.meta.get("platform")
        checkStringList = checkStringDict.items()
        for checkString in checkStringList:
            checkName = checkString[0]
            reString = re.compile(checkString[1], re.I)
            checkResult = re.findall(reString, response.text)
            if bool(checkResult) is False:
                url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=cba55469-7415-4280-926f-d38c2a8d7f23"
                content = "{version}_{currentPlatform}_{currentBranch}_{checkName} 未出包\nlink: {link}".format(
                    version=version, currentPlatform=currentPlatform,
                    currentBranch=currentBranch, checkName=checkName, link = response.url
                )
                data = {
                    "msgtype": "text",
                    "text": {
                    "content": content,
                    "mentioned_list":["@all"],
                    "mentioned_mobile_list":["@all"]}
                }
                headers = {'Content-Type': 'application/json'}
                data = json.dumps(data)
                yield scrapy.Request(url=url, method="post", headers=headers, body=data)
                print("===========ADFDASFASF===========")
            else:
                pass