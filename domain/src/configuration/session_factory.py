from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from domain.src.comm.key_property import CommProperty
from util.singleton import SingletonInstance


class SessionFactory(SingletonInstance):
    def __init__(self):
        user_name = CommProperty().get_database_user_name()
        password = CommProperty().get_database_password()
        url = CommProperty().get_database_url()
        self.engine = create_engine(f"mysql+pymysql://{user_name}:{password}@{url}:3306/mydb")
        self.session = sessionmaker(bind=self.engine)

    def connection_test(self):
        self.engine.execute("select 1")

    def get_session(self):
        return self.session


