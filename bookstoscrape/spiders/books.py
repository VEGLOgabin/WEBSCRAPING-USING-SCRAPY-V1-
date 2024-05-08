import scrapy
from ..items import BookstoscrapeItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        items=BookstoscrapeItem()
     
        Name = response.css('.product_pod a').css('::text').extract()
        Price = response.css('.price_color').css('::text').extract()
        Image = response.css('.thumbnail::attr(src)').extract()
        for i in range(len(Name)):
           items['Name']=Name[i]
           items['Price']=Price[i]
           items['Image']=Image[i]
           
           yield items


        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

