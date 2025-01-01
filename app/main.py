from fastapi import FastAPI
from googleapiclient import discovery
from transformers import T5ForConditionalGeneration, T5Tokenizer

from app.routes.fact_check_route import fact_check_router
from app.params import google_fact_check_tools_api_key

# add all fact check services here
google_fact_check_service = discovery.build(
    "factchecktools", "v1alpha1", developerKey=google_fact_check_tools_api_key)

model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

fact_checks_app = FastAPI()
fact_checks_app.include_router(fact_check_router)