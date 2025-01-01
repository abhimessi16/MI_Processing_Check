import os
from dotenv import load_dotenv

if not load_dotenv():
    print("Environment variables not loaded!")

google_fact_check_tools_api_key = os.getenv("GOOGLE_FACT_CHECK_TOOLS_API_KEY").split(",")
fact_check_apis = ["google"]