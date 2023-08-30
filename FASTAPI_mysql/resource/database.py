from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "mysql+mysqldb://root:tiger@localhost/db_test"

args = {
    "pool_size": 1,
    "max_overflow": 3,
    "pool_recycle": 120
}

engine = create_engine(db_url, 
                       connect_args={"connect_timeout": 5}, 
                       **args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() #클래스를 정의할 떄 사용되는 기본 클래스

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()