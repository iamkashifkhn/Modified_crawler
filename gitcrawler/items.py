# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GitcrawlerItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    author_title = scrapy.Field()
    last_updated = scrapy.Field()
    url = scrapy.Field()
    tags = scrapy.Field()
    languages = scrapy.Field()
    stars = scrapy.Field()
    forks = scrapy.Field()
    license = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    print("Hello testing",file_urls)
