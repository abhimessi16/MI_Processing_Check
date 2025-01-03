# Fact checking API

API to check whether a given input news is valid, by passing it through various fact check apis, currently only using Google Fact Check Tools API. Used in flink stream processing pipeline.

Requirements

    Python 3.12

Clone the repo - https://github.com/abhimessi16/MI_Processing_Check

    cd into repo folder
    Create a virtual environment - recommended
    Run - pip install -r requirements.txt
    Create .env file using .envExample. Add your Google API key. This API key must have access to the Google Fact Check Tools API
    Run - fastapi run app/main.py (or run using uvicorn on different port)
