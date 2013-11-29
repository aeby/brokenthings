# -*- coding: utf-8 -*-
# Copyright (c) Reto Aebersold.
# See LICENSE for details.


from bts.spiders import first_value
from scrapy.selector import Selector
from bts.items import BrokenItem
from scrapy.spider import BaseSpider


class TuttiSpider(BaseSpider):
    name = "tutti"
    allowed_domains = ["tutti.ch"]
    start_urls = [
        "http://www.tutti.ch/bern?st=s&q=defekt",
        "http://www.tutti.ch/bern?st=s&q=kaputt",
    ]

    def parse(self, response):
        sel = Selector(response)
        offers = sel.xpath('//*[@id="ctn"]/ol/li')

        items = []
        for site in offers:
            item = BrokenItem()
            item['title'] = first_value(site.xpath('a/div/h3/text()').extract())
            item['link'] = first_value(site.xpath('a[1]/@href').extract())
            item['desc'] = first_value(site.xpath('a/div/p/text()').extract())
            item['price'] = first_value(site.xpath('a/span/strong/text()').extract()).replace('\'', '')
            items.append(item)
        return items