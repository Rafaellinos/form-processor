from typing import List
from fastapi import APIRouter, Depends

simple_form_router = APIRouter()


@simple_form_router.get("/", response_model=List[dict])
async def get_form_results():
    return [{"form_results": "some form results"}]
