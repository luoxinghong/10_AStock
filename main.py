# -*- coding: utf-8 -*-
from scrapy import cmdline

# cmdline.execute("scrapy crawl douban -s JOBDIR=./jobdir".split())
# cmdline.execute("scrapy crawl douban -o movie1.csv -t csv".split())
cmdline.execute("scrapy crawl astock".split())
