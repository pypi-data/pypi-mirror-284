'''
Name: ChickenSoup.Config
Author: Monarchdos
Date: 2024-07-15 15:14:38
LastEditTime: 2024-07-15 15:15:56
'''
from pydantic import BaseModel, validator

class Config(BaseModel):
    chickensoup_reply_at: bool = True

    @validator('chickensoup_reply_at', pre=True, always=True)
    def check_boolean(cls, v):
        if not isinstance(v, bool):
            raise ValueError('chickensoup_reply_at must be a boolean value')
        return v
