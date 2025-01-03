import importlib
import json

from fastapi import APIRouter, Response

from app.params import fact_check_apis

fact_check_router = APIRouter(prefix="/api/v1/fact-check")

@fact_check_router.get("")
def fact_check(news_to_check: str):
    is_fake_news = False
    # using only google fact check api, later when multiple apis are used, need to change logic
    # checking which api gave different result? etc.
    for api in fact_check_apis:
        api_utils = importlib.import_module(f"app.utils.{api}_utils")
        is_fake_news, fact_source = is_fake_news or api_utils.fact_check(news_to_check)
    return Response(content=json.dumps({
        is_fake_news: is_fake_news,
        fact_source: fact_source
    }))