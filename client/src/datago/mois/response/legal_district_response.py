from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class LegalDistrictResponse(BaseModel):
    """
    행정안전부 법정동 응답 객체
    """
    legal_district_code: Optional[str] = Field(alias="region_cd")
    si_do_code: Optional[str] = Field(alias="sido_cd")
    si_gun_gu_code: Optional[str] = Field(alias="sgg_cd")
    eup_myeon_dong_code: Optional[str] = Field(alias="umd_cd")
    ri_code: Optional[str] = Field(alias="ri_cd")
    locat_jumin_code: Optional[str] = Field(alias="locatjumin_cd")
    locat_jijuk_code: Optional[str] = Field(alias="locatjijuk_cd")
    locat_address_name: Optional[str] = Field(alias="locatadd_nm")
    locat_order: Optional[int] = Field(alias="locat_order")
    locat_rm: Optional[str] = Field(alias="locat_rm")
    locat_high_code: Optional[str] = Field(alias="locathigh_cd")
    locat_low_name: Optional[str] = Field(alias="locallow_nm")
    adoption_date: Optional[str] = Field(alias="adpt_de")