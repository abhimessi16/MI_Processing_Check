from fastapi import FastAPI
from googleapiclient import discovery
from transformers import pipeline

from app.routes.fact_check_route import fact_check_router
from app.params import google_fact_check_tools_api_key

# add all fact check services here
google_fact_check_service = discovery.build(
    "factchecktools", "v1alpha1", developerKey=google_fact_check_tools_api_key)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

fact_checks_app = FastAPI()
fact_checks_app.include_router(fact_check_router)