from pydantic import BaseModel, Field
from datetime import datetime


class RegionResponse(BaseModel):
    """
    기본 주소 정보를 위한 Base Model
    """
    sido: str = Field(alias="시도명")
    sigungu: str = Field(alias="시군구명")
    dongmyeon: str = Field(alias="읍면동명")
    legalDongCode: int = Field(alias="법정동코드")
    createDate: datetime = Field(alias="생성일자", format="%Y-%m-%d")
    order: int = Field(alias="순위")

