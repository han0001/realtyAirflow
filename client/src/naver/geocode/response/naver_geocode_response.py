from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AddressSeachResponse(BaseModel):
    roadAddress: str
    jibunAddress: str
    englishAddress: str
    x: str
    y: str