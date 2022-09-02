import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
         self.log(f'got response from {response.url}')
         quotes = response.css('.quote')
         for quote in quotes:
            item = {
               'author':quote.css('small[class="author"]::text').get(),
               'quote':quote.css('.text::text').get(),
               'tags':quote.css('.tag::text').getall(),
            }

            yield item
