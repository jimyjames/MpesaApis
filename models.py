from abc import ABC, abstractmethod
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime
from dataclasses import dataclass



db_conventions = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}



metadata=MetaData(naming_convention=db_conventions)
db=SQLAlchemy(metadata=metadata)





class Callback(db.Model):
    __table__name='callbacks'

    id=db.Column(db.Integer,primary_key=True)
    status=db.Column(db.Integer)
    message=db.Column(db.String(150))
    request_id=db.Column(db.String(50))
