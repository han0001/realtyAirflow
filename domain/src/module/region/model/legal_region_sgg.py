from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()


class LegalRegionSgg(Base):
    __tablename__ = 'tb_legal_region_sgg'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sido_id = Column(Integer, nullable=False)
    sgg_code = Column(String(10), nullable=True)
    sgg_name = Column(String(64), nullable=True)
    center_location = Column(Geometry('POINT'), nullable=True)
    legal_region_code = Column(String(20), nullable=True)
    address_name = Column(String(255), nullable=True)
    created_date = Column(DateTime, default=func.now())
    modified_date = Column(DateTime, default=func.now())

