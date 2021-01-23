# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
class FinalprojectPipeline:
    def process_item(self, item, spider):
        filmName = item['movieName'].replace(u'\xa0', u' ').strip() #remove 'xa0'
        score = item['score']
        reviewNum = item['reviewNum']
        releaseDate = item['releaseDate'].replace('\n', ' ').strip()
        genre = item['genre']
        runtime = item['runtime'][0].strip() #error fixed
        director = item['director']
        stars = item['stars']
        writer = item['writer']
        budget = "No Record" if len(item['budget'])==0 else item['budget'][0].strip() # return "No Record" if nothing in list
        worldWideGross = item['worldWideGross']
        language = item['language']
        country = item['country']
        company = item['company']

        #下面准备插入数据库
        #将以下四个数据插入film Table

        #filmName  #列名 filmName
        #runtime   #列名 runtime
        #releaseDate #列名 releaseDate
        #budget    #列名 budget

        #将genre 插入 genres Table
        #genre    #列名 genre



        conn = None
        cursor = None
        self.conn = pymysql.Connect()
        self.cursor = self.conn.cursor()
        try:
            sql = "INSERT INTO film (filmName,runtime,releaseDate,budget) VALUES ('%s','%s','%s','%s')"%(filmName,runtime,releaseDate,budget)
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()