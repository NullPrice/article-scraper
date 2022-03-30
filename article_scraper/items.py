import scrapy


class ArticleScraperItem(scrapy.Item):
    link_url = scrapy.Field()
    link_text = scrapy.Field()
    resp_url = scrapy.Field()
