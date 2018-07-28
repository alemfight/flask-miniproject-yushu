
from sqlalchemy import Column, Integer ,String #基础类型从基础包导入
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy 模型映射工具
# Flask.SQLAlchemy flask版
# WTforms flask_wtforms
db = SQLAlchemy()

class book(db.Model):
	id = Column(Integer,primary_key=True,autoincrement=True)
	title = Column(String(50),nullable=False)
	author = Column(String(30),nullable=True,default='未名')
	binding = Column(String(20))
	publisher = Column(String(50))
	price = Column(String(20))
	pages = Column(Integer)
	pubdate = Column(String(20))
	isbn = Column(String(15),nullable=False,unique=True)
	summary = Column(String(1000))
	image = Column(String(50))

	#ORM 对象关系映射 code first

