from pydantic import BaseModel, Field
from typing import Optional, List


class SimpleForm(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    phone: str = Field(...)
    quantity_adults: int = Field(...)
    quantity_children: int = Field(...)
    guests: List[str] = Field(...)
    date: Optional[str] = Field(None)
