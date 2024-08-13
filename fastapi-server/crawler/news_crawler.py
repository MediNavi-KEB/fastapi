import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from dto.news_dto import NewsCreateModel
from crud.news_crud import create_news, delete_news
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_URL = "https://kormedi.com"


def get_article_details(article_url: str):
    try:
        response = requests.get(article_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            date_tag = soup.find("b")
            news_date_time = None
            summary = ""

            if date_tag:
                date_str = date_tag.get_text().strip()
                try:
                    news_date_time = datetime.strptime(date_str, "%Y.%m.%d %H:%M")
                except ValueError as e:
                    logger.error(f"Date parsing error: {e}")

            figure = soup.find("figure")
            if figure:
                figcaption = figure.find("figcaption")
                if figcaption:
                    summary = figcaption.get_text().strip()

            return news_date_time, summary
    except Exception as e:
        logger.error(f"Error fetching article details: {e}")
    return None, None


def crawl_and_store(db: Session, user_id: str, disease_name: str):
    delete_news(db, user_id)
    logger.info(f"Deleted existing news for user_id: {user_id}, disease_name: {disease_name}")

    logger.info("Starting crawl and store")
    try:
        for page in range(1):
            url = f"{BASE_URL}/page/{page}/?s={disease_name}"
            response = requests.get(url)

            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, "html.parser")
                articles = soup.find_all("h2", class_="title")

                for i, article in enumerate(articles):
                    if i == 2:
                        break
                    a_tag = article.find("a", class_="post-url post-title")
                    if a_tag:
                        title = a_tag.get_text().strip()
                        article_url = a_tag["href"]

                        if not article_url.startswith("http"):
                            article_url = BASE_URL + article_url

                        news_date_time, summary = get_article_details(article_url)
                        if news_date_time and summary:
                            news_item = NewsCreateModel(
                                title=title,
                                summary=summary,
                                news_date_time=news_date_time,
                                link=article_url
                            )
                            try:
                                create_news(db, news_item, user_id, disease_name)
                                logger.info(f"Stored news: {title}")
                            except Exception as e:
                                logger.error(f"Error storing news: {e}")
                        else:
                            logger.warning(f"Missing data for article: {title} (URL: {article_url})")
            else:
                logger.error(f"Failed to fetch the page: {response.status_code}")
    except Exception as e:
        logger.error(f"Error during crawl and store: {e}")
    logger.info("Crawl and store completed")
