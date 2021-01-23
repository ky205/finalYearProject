import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from finalProject.items import  FinalprojectItem
import re
class ImdbSpider(CrawlSpider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/search/keyword/?ref_=kw_ref_yr&mode=detail&page=1&title_type=movie&sort=moviemeter,asc&release_date=1900%2C2020']

    rules = (
        Rule(LinkExtractor(allow=r'/?ref_=kw_li_tt'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'sort=moviemeter,asc&title_type=movie&explore=keywords&mode=detail&ref_=kw_nxt#main'),callback='parse_next', follow=True),
    )



    def parse_item(self, response):
        name = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/h1/text() | //*[@id="title-overview-widget"]/div[1]/div[2]/div/div/div[2]/h1/text()').extract()
        movieName = name[0]

        score = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[1]/div[1]/div[1]/strong/span/text()').extract()

        review_num = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[1]/div[1]/a/span/text()').extract()

        release_date1 = response.xpath('//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[2]/div/a/text()').extract()

        release_date = release_date1[-1]
        release_date1.pop()
        genre = release_date1

        directors = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[2]/a/text() | //*[@id="title-overview-widget"]/div[2]/div[2]/div[2]/a/text() | //*[@id="title-overview-widget"]/div[2]/div[2]/div[1]/div[2]/a/text()').extract()
        writer = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[3]/a/text() | //*[@id="title-overview-widget"]/div[2]/div[2]/div[3]/a/text() | //*[@id="title-overview-widget"]/div[2]/div[2]/div[1]/div[3]/a/text()').extract()
        stars = response.xpath('//*[@id="title-overview-widget"]/div[2]/div[1]/div[4]/a/text() | //*[@id="title-overview-widget"]/div[2]/div[2]/div[4]/a/text() | //*[@id="title-overview-widget"]/div[2]/div[2]/div[1]/div[4]/a/text()').extract()

        ex1 = 'h4 class="inline">Language:</h4>\n        <a href=".*?">(.*?)</a>\n'
        ex2 = '<h4 class="inline">Country:</h4>\n        <a href=".*?">(.*?)</a>\n'
        ex3 = 'Cumulative Worldwide Gross:</h4> (.*?)        </div>'
        ex4 = '<h4 class="inline">Production Co:</h4>\n<a href=".*?">(.*?)</a>'
        ex5 = '<h4 class="inline">Runtime:</h4>\n        <time datetime=".*?">(.*?)</time>\n'
        ex6 = '<h4 class="inline">Budget:</h4>(.*?)\n'

        worldWideGross = response.selector.re(ex3)
        language = response.selector.re(ex1)
        country = response.selector.re(ex2)
        company = response.selector.re(ex4)
        runtime = response.selector.re(ex5)
        budget = response.selector.re(ex6)


        dic = {
            "name":movieName,
            "score":score,
            "review":review_num,
            "release":release_date,
            "genre":genre,
            "runtime":runtime,
            "writer" : writer,
            "star":stars,
            "directors":directors,
            "budget":budget,
            "company":company,
            "country":country,
            "language":language,
            "worldwidegross":worldWideGross
        }
        item = FinalprojectItem()
        item['score'] = score
        item['reviewNum'] = review_num
        item['movieName'] = movieName
        item['releaseDate'] = release_date
        item['genre'] = genre
        item['runtime'] = runtime
        item['director'] = directors
        item['stars'] = stars
        item['writer'] = writer
        item['budget'] = budget
        item['worldWideGross'] = worldWideGross
        item['language'] = language
        item['country'] = country
        item['company'] = company
        yield item


    def parse_next(self, response):
        print(response)

