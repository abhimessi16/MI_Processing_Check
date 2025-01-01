from pydantic import BaseModel, Field

class Publisher(BaseModel):
    name: str
    site: str

class ClaimReview(BaseModel):
    publisher: Publisher
    url: str
    title: str
    review_date: str = Field(None, alias="reviewDate")
    textual_rating: str = Field(None, alias="textualRating")
    language_code: str = Field(None, alias="languageCode")

class Claim(BaseModel):
    text: str
    claimant: str
    claim_date: str = Field(None, alias="claimDate")
    claim_review: list[ClaimReview] = Field(None, alias="claimReview")

class ClaimSearch(BaseModel):
    claims: list[Claim]
    next_page_token: str = Field(None, alias="nextPageToken")