from fastapi import APIRouter, Depends, HTTPException, Query, Path, Response
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/teste", tags=["teste"])

@router.get("", summary="test")
async def test():
    return "hello world"