from sqlalchemy import create_engine

def db_create(db_url):
	print(db_url)
	engine = create_engine(db_url, echo=True)

	from fastapi_hcytools.db.database import Base
	from db.models.project_info import ProjectInfo

	table_list = [
		ProjectInfo.__table__,
	]

	Base.metadata.create_all(bind=engine, tables=table_list)
	print("##### DB 생성 완료")
	pass


if __name__ == '__main__':
	db_create("mysql://ictk:#ictk1234@localhost:3306/table-name?charset=utf8")
