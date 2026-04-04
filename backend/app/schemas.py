from pydantic import BaseModel

class SearchResultItem(BaseModel):
    filename: str
    score: float

class SearchResponse(BaseModel):
    query_filename: str
    top_k: int
    results: list[SearchResultItem]
