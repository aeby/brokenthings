# -*- coding: utf-8 -*-
# Copyright (c) Reto Aebersold.
# See LICENSE for details.


from scrapy.item import Item, Field


class BrokenItem(Item):
    title = Field()
    link = Field()
    desc = Field()
    source = Field()
    price = Field()
