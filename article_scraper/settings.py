import json
import os
from dotenv import load_dotenv

load_dotenv()


BOT_NAME = "article_scraper"
SPIDER_MODULES = ["article_scraper.spiders"]
NEWSPIDER_MODULE = "article_scraper.spiders"
ROBOTSTXT_OBEY = os.getenv("ROBOTSTXT_OBEY", "False") == "True"
AUTOTHROTTLE_ENABLED = os.getenv("AUTOTHROTTLE_ENABLED", "False") == "True"

# Start URLS for the crawler
START_URLS = json.loads(os.getenv("START_URLS", '[]'))

# Word count threshold before we consider following a link
LINK_WORD_THRESHOLD = os.getenv("LINK_WORD_THRESHOLD", 5)

# Word count threshold before we consider a page we've landed on as an 'article'
ARTICLE_WORD_THRESHOLD = os.getenv("ARTICLE_WORD_THRESHOLD", 200)
