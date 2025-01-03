import app.main as session

def fact_check(news_to_check: str):
    service = session.google_fact_check_service
    is_fake_news = False
    fact_source = ""
    try:
        news_keywords = session.summarizer(news_to_check, max_length=20, min_length=10, do_sample=False)
        claims = service.claims().search(query=news_keywords[0].get("summary_text", news_to_check)).execute()
        # for now let's check only the first page
        # also assuming that the results are actually relevant
        for claim in claims.get("claims", []):
            # lets take first review for now
            claim_review = claim.get("claimReview", [])
            if not claim_review:
                return is_fake_news

            # there's multiple categories like half true, misleading, false, true, etc. For simplicity we check only true or false
            is_fake_news = is_fake_news or (False if "true" in claim_review[0].get("textualRating", "").lower() else True)
            fact_source = claim_review[0].get("url", "No link")
            
    except Exception as ex:
        print(ex)
    finally:
        return [is_fake_news, fact_source]