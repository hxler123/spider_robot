import re
import datetime

import scrapy
from scrapy.selector import Selector
from common.platform import PLATFORMS

class CheckSpider(scrapy.Spider):
    name = "check"
    TODAY = datetime.date.today().isoformat()

    def start_requests(self):
        for version in PLATFORMS.keys():
            url = "http://10.80.1.174:8090/agora_sdk/{version}/nightly_build/{today}".format(
                version=version,today=self.TODAY
            )
            yield scrapy.Request(url=url, meta={"version":version})

    def parse(self, response):
        version = response.meta.get("version")
        versionDict = PLATFORMS[version]
        for pl in versionDict.keys():
            branchDict = versionDict[pl]
            for br in branchDict.keys():
                url = response.url + "/" + pl + "/" + br + "/"
                checkStringDict = branchDict[br]
                yield scrapy.Request(url = url, callback=self.check,
                                    meta={"checkStringDict": checkStringDict,
                                          "version": version,
                                          "branch": br,
                                          "platform": pl})

    def check(self, response):
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
                print("==============={currentPlatform}_{currentBranch}_{checkName}_Failed=============".format(
                      currentPlatform=currentPlatform, currentBranch=current_branch, checkName=checkName))
            else:
                pass