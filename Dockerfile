FROM python:buster

RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-dev

COPY . /app

CMD [ "scrapy", "crawl", "articles", "-O", "./output/output.json" ]