from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.src.comm.key_property import CommProperty


class DbEngine:
    def __init__(self):
        self.url = CommProperty().get_database()
        self.engine = create_engine(self.url)

    def connection_test(self):
        self.engine.execute("select 1")

    def get_session(self):
        return sessionmaker(bind=self.engine)


db = DbEngine()
aa = db.connection_test()

