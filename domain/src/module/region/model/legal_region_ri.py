from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry

Base = declarative_base()


class LegalRegionRi(Base):
    __tablename__ = 'tb_legal_region_ri'

    id = Column(Integer, primary_key=True, autoincrement=True)
    emd_id = Column(Integer, nullable=False)
    ri_code = Column(String(10), nullable=True)
    ri_name = Column(String(64), nullable=True)
    center_location = Column(Geometry('POINT'), nullable=True)
    legal_region_code = Column(String(20), nullable=True)
    address_name = Column(String(255), nullable=True)
    created_date = Column(DateTime, nullable=True)
    modified_date = Column(DateTime, nullable=True)



