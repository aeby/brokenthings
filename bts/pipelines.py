# -*- coding: utf-8 -*-
# Copyright (c) Reto Aebersold.
# See LICENSE for details.


from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):

    # put all words in lowercase
    words_to_filter = ['ohne defekt', 'nicht kaputt']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['desc']).lower():
                raise DropItem("Is not broken")
        else:
            return item
