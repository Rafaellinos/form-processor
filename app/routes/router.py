from fastapi import APIRouter

from .simple_form_router import simple_form_router

router = APIRouter()
router.include_router(simple_form_router, prefix="/simple_forms", tags=["form_results"])
