.PHONY: build run local_build local_run

build:
	docker build -t article-scraper .

run: build
	docker run -it --rm --env-file=.env -v $(CURDIR)/output/:/app/output/ article-scraper

local_build:
	pip install poetry
	poetry install

local_run: local_build
	poetry run scrapy crawl articles -O $(CURDIR)/output/output.json