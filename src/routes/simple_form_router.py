from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException
from src.database.database import Database
from src.models.schemas.simple_form import SimpleForm

simple_form_router = APIRouter()


@simple_form_router.get("/", response_model=List[dict])
async def get_form_results():
    try:
        result = await Database.get_items()
        if not result:
            raise HTTPException(status_code=404, detail="No items found")
    except Exception as e:
        raise e
    return result


@simple_form_router.get("/{item_id}", response_model=dict)
async def get_form_result_by_id(item_id: UUID):
    try:
        result = await Database.get_item_by_id(item_id)
        if not result:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise e
    return result


@simple_form_router.post("/", response_model=dict)
async def post_form_result(simple_form_data: SimpleForm):
    try:
        result = await Database.put_item(simple_form_data)
    except Exception as e:
        raise e
    return result
