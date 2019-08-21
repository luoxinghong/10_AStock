# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi
import traceback
import logging

logger = logging.getLogger(__name__)

class AstockPipeline(object):
    commit_sql_str = """insert into astock(astock_id,astock_name,date,volume,open,close,high,low) values ("{astock_id}","{astock_name}","{date}","{volume}","{open}","{close}","{high}","{low}");"""

    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_item(self, item, spider):
        # 执行具体的插入
        # 根据不同的item 构建不同的sql语句并插入到mysql中
        try:
            sqltext = self.commit_sql_str.format(
                astock_id=pymysql.escape_string(str(item["astock_id"])),
                astock_name=pymysql.escape_string(str(item["astock_name"])),
                date=pymysql.escape_string(str(item["date"])),
                volume=pymysql.escape_string(str(item["volume"])),
                open=pymysql.escape_string(str(item["open"])),
                close=pymysql.escape_string(str(item["close"])),
                high=pymysql.escape_string(str(item["high"])),
                low=pymysql.escape_string(str(item["low"]))
            )
            self.cursor.execute(sqltext)
        except Exception as e:
            logger.warning(e)

    def open_spider(self, spider):
        self.connect = pymysql.connect(
            host=self.settings.get("MYSQL_HOST"),
            port=self.settings.get("MYSQL_PORT"),
            db=self.settings.get("MYSQL_DBNAME"),
            user=self.settings.get("MYSQL_USER"),
            passwd=self.settings.get("MYSQL_PASSWD"),
            charset='utf8mb4',
            use_unicode=True
        )
        self.cursor = self.connect.cursor()
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
