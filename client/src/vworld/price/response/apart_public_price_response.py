from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class AddressSeachResponse(BaseModel):
    """
    공동주택가격속성 응답

    pnu             고유번호
    ldCode          법정동코드
    ldCodeNm        법정동명
    regstrSeCode    특수지구분코드
    regstrSeCodeNm  특수지구분명
    mnnmSlno        지번
    stdrYear        기준연도
    stdrMt          기준월
    aphusCode       공동주택코드
    aphusSeCode     공동주택구분코드
    aphusSeCodeNm   공동주택구분명
    spclLandNm      특수지명
    aphusNm         공동주택명
    dongNm          동명
    floorNm         층명
    hoNm            호명
    prvuseAr        전용면적(㎡)
    pblntfPc        공시가격(원)
    lastUpdtD       데이터기준일자
    """

    pnu: str = Field(description="고유번호")
    ldCode: str = Field(description="법정동코드")
    ldCodeNm: str = Field(description="법정동명")
    regstrSeCode: str = Field(description="특수지구분코드")
    regstrSeCodeNm: str = Field(description="특수지구분명")
    mnnmSlno: str = Field(description="지번")
    stdrYear: int = Field(description="기준연도")
    stdrMt: int = Field(description="기준월")
    aphusCode: str = Field(description="공동주택코드")
    aphusSeCode: str = Field(description="공동주택구분코드")
    aphusSeCodeNm: str = Field(description="공동주택구분명")
    spclLandNm: str = Field(description="특수지명")
    aphusNm: str = Field(description="공동주택명")
    dongNm: str = Field(description="동명")
    floorNm: str = Field(description="층명")
    hoNm: str = Field(description="호명")
    prvuseAr: float = Field(description="전용면적(㎡)")

    # 공시가격(원)
    pblntfPc: int = Field(description="공시가격(원)")

    # 데이터기준일자
    lastUpdtDt: str = Field(description="데이터기준일자")