from article_scraper.items import ArticleScraperItem
import scrapy
from scrapy.http import HtmlResponse, Request


class ArticleSpider(scrapy.Spider):
    name = "articles"

    def start_requests(self):
        for url in self.settings["START_URLS"]:
            yield Request(
                url, meta={"start_url": url}, callback=self.parse_landing_page
            )

    def parse_landing_page(self, response: HtmlResponse):
        # Grab all links on our landing page
        for link in response.css("a"):
            text = link.css("::text").get(default="")
            url = link.css("::attr(href)").get(default="")
            word_count = len(text.split())

            # If we meet our configured word threadhold assume that the link may be an article
            if word_count >= self.settings.getint("LINK_WORD_THRESHOLD"):
                yield response.follow(
                    url,
                    self.parse_article,
                    cb_kwargs=dict(
                        item=ArticleScraperItem(link_url=url, link_text=text)
                    ),
                )

    def parse_article(self, response: HtmlResponse, item: ArticleScraperItem):
        # Get article text content, remove new lines etc so I can get a read on the word count
        article_words = " ".join(response.css("article *::text").getall()).split()
        word_count = len(article_words)

        # If we meet our configured word threadhold assume that the content on this page is an article
        if word_count >= self.settings.getint("ARTICLE_WORD_THRESHOLD"):
            item['resp_url'] = response.url
            yield item
