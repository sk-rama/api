from pydantic import BaseModel, Field

class CounterOut(BaseModel):
    counter: int

    class Config:
        orm_mode = True


class IdIn(BaseModel):
    id: str = Field(..., min_length=3, max_length=1024)
    step: int = Field(1, ge=1, le=1000)

    class Config:
        orm_mode = True

