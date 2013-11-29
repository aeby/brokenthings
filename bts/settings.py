# -*- coding: utf-8 -*-
# Copyright (c) Reto Aebersold.
# See LICENSE for details.

BOT_NAME = 'bts'

SPIDER_MODULES = ['bts.spiders']
NEWSPIDER_MODULE = 'bts.spiders'

ITEM_PIPELINES = ['bts.pipelines.FilterWordsPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'waster (+http://www.yourdomain.com)'
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'
