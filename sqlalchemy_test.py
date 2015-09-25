#!/usr/bin/env python
# coding=utf-8
#传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上
from sqlalchemy import Column, String, create_engine, relationship,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建连接对像
Base = declarative_base()

#定义user对介
class User(Base):
    #表名字
    #__tablename__ == 'user'
    __tablename__ = 'user'
    #表结构
    id =Column(String(20),primary_key=True)
    name = Column(String(20))
    #设置一对多
    books = relationship('Book')
class Book(Base):
    __tablename__='book'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))

#初始化数据库连接
#连接信息：SQLAlchemy用一个字符串表示连接信息：'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/yjoqm')
#创建dbsession类弄
DBSession = sessionmaker(bind=engine)


#创建session 对像
session = DBSession()
#创建user对像
new_user = User(id='5', name = 'ellen')
#添加到session
session.add(new_user)
#提交保存到数据库，并关闭session
session.commit()
session.close()


#查询接口
session = DBSession()
user = session.query(User).filter(User.id=='5').one()
print 'type:', type(user)
print 'name:', user.name
