from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Sequence, func
from sqlalchemy.orm import relationship

from fastapi_hcytools.db.database import Base
from fastapi_hcytools.db.models import make_timestamp


#참조 : https://wikidocs.net/175967
#from database import Base


class ProjectInfo(Base):
    __tablename__ = "project_info"

    id = Column(Integer, primary_key=True)
    name = Column(String(32, collation='utf8_general_ci'), nullable=False, unique=True)
    description = Column(Text(collation='utf8_general_ci'), nullable=True)

    data_count = Column(Integer, default=0)
    complete_count = Column(Integer, default=0)

    largest_mtr_index = Column(Integer, default=0)

    create_date = Column(DateTime, nullable=False, default=func.now())
    update_date = Column(DateTime, nullable=False, default=func.now(), onupdate=make_timestamp)



def get_model_dict(model):
    temp = dict((column.name, getattr(model, column.name))
                for column in model.__table__.columns)
    temp["create_date"] = temp["create_date"].strftime("%Y-%m-%d %H:%M:%S")
    temp["update_date"] = temp["update_date"].strftime("%Y-%m-%d %H:%M:%S")
    return temp
