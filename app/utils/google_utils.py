import app.main as session
from app.google_models import ClaimSearch

def fact_check(news_to_check: str):
    service = session.google_fact_check_service
    model_prompt = "Convert the statement '' to True or False. Give a single word as 'True' or 'False'."
    is_fake_news = False
    try:
        claims: ClaimSearch = service.claims().search(query=news_to_check)
        # for now let's check only the first page
        # also assuming that the results are actually relevant
        for claim in claims.claims:
            # lets take first review for now
            claim_review = claim.claim_review[0]
            inputs = session.tokenizer(model_prompt.format(claim_review.textual_rating), return_tensors="pt")

            outputs = session.model.generate(inputs['input_ids'], max_length=10)
            result = session.tokenizer.decode(outputs[0], skip_special_tokens=True)

            is_fake_news = is_fake_news or (True if result == "True" else False)
            
    except Exception as ex:
        print(ex)
    finally:
        return is_fake_news