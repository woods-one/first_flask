
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///user.db')  # user.db というデータベースを使うという宣言です
Base = declarative_base()  # データベースのテーブルの親です


class User(Base):  # PythonではUserというクラスのインスタンスとしてデータを扱います
    __tablename__ = 'users'  # テーブル名は users です
    id = Column(Integer, primary_key=True, unique=True)  # 整数型のid をprimary_key として、被らないようにします
    email = Column(String)  # 文字列の emailというデータを作ります
    name = Column(String)  # 文字列の nameというデータを使います

    def __repr__(self):
        return "User<{}, {}, {}>".format(self.id, self.email, self.name)


Base.metadata.create_all(engine)  # 実際にデータベースを構築します
SessionMaker = sessionmaker(bind=engine)  # Pythonとデータベースの経路です
session = SessionMaker()  # 経路を実際に作成しました

user1 = User(email="thisisme@test.com", name="Python")  # emailと nameを決めたUserのインスタンスを作りましょう(idは自動で1から順に振られます)
session.add(user1)  # user1 をデータベースに入力するための準備をします
session.commit()  # 実際にデータベースにデータを入れます。