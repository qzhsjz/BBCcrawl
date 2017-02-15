# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import mysql.connector


class BbccrawlPipeline(object):
    # 在构造函数中连接数据库
    def __init__(self):
        config = {'host': '127.0.0.1',  # 默认127.0.0.1
                  'user': 'qzhsjz',
                  'password': '86.corrode',
                  'port': 3306,  # 默认即为3306
                  'database': 'bbccrawl',
                  'charset': 'utf8'  # 默认即为utf8
                  }
        try:
            self.sqlconn = mysql.connector.connect(**config)
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))

    # 处理函数
    def process_item(self, item, spider):
        cur = self.sqlconn.cursor()
        SQLinsert = 'INSERT IGNORE INTO `bbc`(title, newstype, pubtime, refer, summary, content) VALUES ("%(Title)s", "%(Type)s", "%(Pubtime)s", "%(Refer)s", "%(Summary)s", "%(Content)s")'
        cur.execute(SQLinsert, dict(item))
        rows = cur.rowcount
        self.sqlconn.commit()
        cur.close()
        if rows == 0: raise DropItem("Already in the database.")
        return item

    # 析构函数中断开连接
    def __del__(self):
        self.sqlconn.close()
