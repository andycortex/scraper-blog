import scrapy


class BlogsSpider(scrapy.Spider):
    name = 'blogs'
    allowed_domains = ['scrapeit.home.blog']
    start_urls = ['https://scrapeit.home.blog/']

    def parse(self, response):
        blogs = response.css('article')
        for blog in blogs:
            item = {
                'title' : blog.css('.entry-title a::text').get(),
                'summary' : ''.join(blog.css('p:nth-child(1) ::text').getall()),
                'author' : blog.css('.author.vcard a::text').get(),
                'date' : blog.css('.entry-date.published::text').get(),
                'cateogries' : blog.css('.cat-links a::text').getall(),
                'tags' : blog.css('.tags-links a::text').getall(),
            }

            yield item
