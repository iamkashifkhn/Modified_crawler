import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider
from gitcrawler.items import GitcrawlerItem

class MyspiderSpider(Spider):
    name = 'myspider'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/muddasar-de/muddasar-folio']


    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths="//a[@class='v-align-middle']"), callback='parse_post', follow=True),
    #     Rule(LinkExtractor(restrict_xpaths="//a[@class='next_page']"), callback='parse_post', follow=True ),
        
    # )
    # def __init__(self):
    #     URL = 'https://github.com/search?p=1&q=java&type=Repositories'
    #     self.start_urls = [URL]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url = url, callback=self.parse_content)

    # def parse_content(self, response):
    #     next_page_url = self.get_next_page(response)
    #     print("Hello my friend", next_page_url)
    #     if next_page_url is not None:
    #         yield scrapy.Request(response.urljoin(next_page_url))
    #     else:
    #         return

    # def get_next_page(self, response):
    #     next_page_url = response.xpath("//a[@class='next_page']/@href").get()
    #     print("Hello", next_page_url)
    #     return next_page_url

    def parse(self, response):
            title = self.extract_title(response)
            author = self.extract_author(response)
            last_updated = self.extract_last_updated(response)
            author_title = self.author_title(response)
            url = self.extract_url(response)
            tags = self.extract_tags(response)
            languages = self.extract_languages(response)
            stars = self.extract_stars(response)
            forks = self.extract_forks(response)
            license = self.extract_license(response)
            getlink = self.download(response)
            # download = self.download(response)
            # download = self.download(response)
            # for item in zip(title, author, last_updated, url, tags, languages, stars, forks, license, getlink):
            new_item = GitcrawlerItem()
            new_item['title'] = title
            new_item['author'] = author
            new_item['author_title']= author_title
            new_item['last_updated'] = last_updated
            new_item['url'] = url
            new_item['tags'] = tags
            new_item['languages'] = languages
            new_item['stars'] = stars
            new_item['forks'] = forks
            new_item['license'] = license
            new_item['file_urls'] = [getlink]
            # if new_item['language'] is not None:
            yield new_item

            # jsonData = {
            #     'title': title,
            #     'author': author,
            #     'last_updated': last_updated,
            #     # 'href': href,
            #     'url': url,
            #     'tags': tags,
            #     'languages': languages,
            #     'stars': stars,
            #     'forks': forks,
            #     'license': license,

            #     # 'download': download
            # }
            # return jsonData
        
    def extract_title(self, response):
        title = response.xpath("//strong[@class='mr-2 flex-self-stretch']/a/text()").get()
        return title

    def extract_author(self, response):
        author = response.xpath("//span[@class='author flex-self-stretch']/a/text()").get()
        return author
    
    def extract_last_updated(self, response):
        last_updated = response.xpath('//relative-time/@datetime').get()
        return last_updated
    
    def extract_url(self, response):
        url= f'https://www.github.com{response.xpath("//strong/a/@href").get()}',
        return url
    
    def extract_tags(self, response):
        tags= response.xpath("//a[@class='topic-tag topic-tag-link']/text()").getall(),
        for i in range(len(tags[0])):
            tags[0][i] = tags[0][i].strip()
        if tags[0]==[]:
            tags= None
        return tags

    def extract_languages(self, response):
        languages= response.xpath("//span[@class='color-fg-default text-bold mr-1']/text()").getall(),
        return languages

    def extract_stars(self, response):
        stars= response.xpath("//span[@id='repo-stars-counter-star']/text()").get(),
        return stars
    
    def extract_forks(self, response):
        forks= response.xpath("//span[@id='repo-network-counter']/text()").get(),
        return forks

    def extract_license(self, response):
        license= response.xpath("//div[@class='mt-2']/a[contains(@href, 'LICENSE')]/text()[2]").get()
        if license:
            license = license.strip()
        return license

    def download(self, response):
        link = response.xpath("//strong[@class='mr-2 flex-self-stretch']/a/@href").get()
        if link is not None:
            link = f'https://www.github.com{link}/archive/refs/heads/master.zip'
            return link

    def author_title(self, response):
        title = response.xpath("//strong[@class='mr-2 flex-self-stretch']/a/text()").get()
        author = response.xpath("//span[@class='author flex-self-stretch']/a/text()").get()
        author_title = f'{author}_{title}'
        return author_title

       