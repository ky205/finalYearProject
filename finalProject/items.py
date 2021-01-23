# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FinalprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movieName = scrapy.Field()
    score = scrapy.Field()
    reviewNum = scrapy.Field()
    releaseDate = scrapy.Field()
    genre = scrapy.Field()
    runtime = scrapy.Field()
    director = scrapy.Field()
    stars = scrapy.Field()
    writer = scrapy.Field()
    budget = scrapy.Field()
    worldWideGross = scrapy.Field()
    language = scrapy.Field()
    country = scrapy.Field()
    company = scrapy.Field()




    pass
