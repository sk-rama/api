from fastapi import APIRouter, Depends, Request, Query, HTTPException
from fastapi.responses import PlainTextResponse
from typing import Any, Optional, List
from pydantic import Required

# io models
from .models_io import CounterOut, IdIn

# database
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import db_functions as dbf

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.get("/set/", response_model=CounterOut)
async def counter_update(request: Request, id: IdIn = Depends(IdIn), db: Session = Depends(get_db)) -> Any:
    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For']
    else:
        ip = request.client.host

    result = dbf.set_counter(db_session=db, id=id.id, step=id.step, ip=ip)
    return result


@router.get("/get/as_json/", response_model=CounterOut)
async def counter_get_as_json(id: IdIn = Depends(IdIn), db: Session = Depends(get_db)) -> Any:
    result = dbf.get_counter(db_session=db, id=id.id)
    if result:
        return result
    else:
        return {"counter": 0}

@router.get("/get/as_platintext/", response_model=CounterOut)
async def counter_get_as_plaintext(id: IdIn = Depends(IdIn), db: Session = Depends(get_db)) -> Any:
    result = dbf.get_counter(db_session=db, id=id.id)
    if result:
        return PlainTextResponse(content=str(result.counter))
    else:
        return PlainTextResponse(content="0")
