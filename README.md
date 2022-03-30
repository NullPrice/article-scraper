# Article Scraper

Very basic scrapy scraper that attempts to identify 'article' content based a given landing pages by making a ton of (configurable) assumptions around content sizes

## Configuration

Configration of the scraper can be done via environment variables. A `.env` has been checked in with some default `START_URLS` as an example. 

- `START_URLS` - A JSON list of target landing pages you want to start at
    - Example: `["https://www.sei.org/publications/", "https://www.bbc.co.uk/news/world"]`
- `LINK_WORD_THRESHOLD` - Word count threshold before we consider following a link
    - Example: `5`
- `ARTICLE_WORD_THRESHOLD` - Word count threshold before we consider a page we've landed on as an 'article'
    -  Example: `200`

## Running

### Via Docker

```bash
make run
```

Or if you prefer not to run via Make for whatever reason:

```bash
docker build -t article-scraper .
docker run -it --rm --env-file=.env -v "$PWD"/output/:/app/output/ article-scraper
```

Output will show up as a `output.json` file inside an `output` folder within the project directory


### Locally

Make sure Python 3.9 is installed locally - [Pyenv](https://software.opensuse.org/package/pyenv) is what I recommend to setup specific Python versions.

A make command has been provided to get started locally:
```bash 
make local_run
```

OR

```bash
	pip install poetry
	poetry install
    poetry run scrapy crawl articles -O "$PWD"/output/output.json
```