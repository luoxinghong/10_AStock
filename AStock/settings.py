# -*- coding: utf-8 -*-

# Scrapy settings for AStock project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'AStock'

SPIDER_MODULES = ['AStock.spiders']
NEWSPIDER_MODULE = 'AStock.spiders'


# 定义scraoy日志的目录，等级，名字
import datetime
to_day = datetime.datetime.now()
log_file_path = "./logs/{}_{}_{}.log".format(to_day.year, to_day.month, to_day.day)
LOG_LEVEL = "INFO"
LOG_FILE = log_file_path


ROBOTSTXT_OBEY = False


DOWNLOADER_MIDDLEWARES = {
    'AStock.middlewares.AstockSpiderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'AStock.middlewares.RandomUserAgentMiddleware': 1,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,  # 这里要设置原来的scrapy的useragent为None，否者会被覆盖掉
    'AStock.middlewares.ProxyMiddleware': 542,  # 添加代理IP
}

# 增加爬虫速度及防ban配置
DOWNLOAD_DELAY = 3
DOWNLOAD_FAIL_ON_DATALOSS = False
CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1
COOKIES_ENABLED = False
DOWNLOAD_TIMEOUT = 30


# 配置自己重写的RFPDupeFilter
# DUPEFILTER_CLASS = 'AStock.middlewares.URLRedisFilter'

# 开启item_pipelines，入库
ITEM_PIPELINES = {
    'AStock.pipelines.AstockPipeline': 300,
}


# msyql数据库配置
MYSQL_HOST = "localhost"
MYSQL_DBNAME = "spider_data"
MYSQL_USER = "root"
MYSQL_PASSWD = "lxh123"
MYSQL_PORT = 3306

# redis数据库配置
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWD = "lxh123"
REDIS_DBNAME = 0
REDIS_KEY = "douban_moive"


# 配置user_agent的随机类型
RANDOM_UA_TYPE = 'random'
