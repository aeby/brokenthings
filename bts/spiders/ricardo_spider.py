# -*- coding: utf-8 -*-
# Copyright (c) Reto Aebersold.
# See LICENSE for details.


from bts.spiders import first_value
from scrapy.selector import Selector
from bts.items import BrokenItem
from scrapy.spider import BaseSpider


class RicardoSpider(BaseSpider):
    name = "ricardo"
    allowed_domains = ["ricardo.ch"]
    start_urls = [
        "http://www.ricardo.ch/search/index/?SplitMode=none&ItemCondition=16&Zip=3000&Range=10&PageSize=120&AreaCountryNr=2#"
    ]

    def parse(self, response):
        sel = Selector(response)
        offers = sel.xpath('/html/body/div/div[1]/div/section[3]/ol/li')

        #/html/body/div/div[1]/div/section[3]/ol/li[8]/div[3]/div[1]/span/span[1]

        items = []
        for site in offers:
            item = BrokenItem()
            item['title'] = first_value(site.xpath('div[2]/div/a/text()').extract())
            item['link'] = 'http://www.ricardo.ch' + first_value(site.xpath('div[2]/div/a/@href').extract())
            item['desc'] = first_value(site.xpath('div[2]/div/span/text()').extract(), default='-')
            item['price'] = first_value(site.xpath('div[3]/div[1]/span/span[1]/text()').extract())\
                .split(' ')[-1].replace(',', '')
            items.append(item)
        return items