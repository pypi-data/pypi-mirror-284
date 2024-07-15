import os

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, close_all_sessions

import contextlib

from fastapi_hcytools.comm.config import config

# print(config.SQLALCHEMY_DATABASE_URL_LIST)
Base = declarative_base()

engines = []
Sessions = []

def get_db():
    if len(Sessions) < 5:
        if config.SQLALCHEMY_DATABASE_URL == "":
            engine = create_engine(os.environ["DATABASE_URL"], pool_pre_ping=True)
            engines.append(engine)
            SessionLocal = sessionmaker(bind=engine)
            Sessions.append(SessionLocal)

        else:
            engine = create_engine(config.SQLALCHEMY_DATABASE_URL, pool_size=5, max_overflow=5, pool_pre_ping=True)
            engines.append(engine)
            SessionLocal = sessionmaker(bind=engine)
            Sessions.append(SessionLocal)
    for session in Sessions:
        try:
            db = session()
            db.query('SELECT 1')
            break
        except:
            continue
    try:
        yield db
    finally:
        db.close()


def db_create(db_url):
    engine = create_engine(db_url, pool_pre_ping=True, echo=True)

    from app.db.models.project_info import ProjectInfo
    from app.db.models.mtr_data import MtrData

    print(ProjectInfo)
    print(MtrData)

    table_list = [
        ProjectInfo.__table__,
        MtrData.__table__
    ]

    Base.metadata.create_all(bind=engine, tables=table_list)
    # print("##### DB 생성 완료")

    # print(inspect(engine).get_table_names())
    pass

if __name__=="__main__":
    db_create("mysql://ictk:#ictk1234@localhost:9036/mtr_data_manager?charset=utf8")

