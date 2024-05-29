import datetime
from typing import Dict

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from typing_extensions import Annotated

from flask_temp.ext import db

"""设置类型映射"""
intpk = Annotated[int, mapped_column(primary_key=True)]
timestamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=func.current_timestamp()),
]


class BaseModel(db.Model):  # type: ignore[name-defined]
    """声明基类，用于公共模型, 以及公共查询"""

    __abstract__ = True

    id: Mapped[intpk]
    created_at: Mapped[timestamp]

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()

    def update(self, data: Dict) -> None:
        if data:
            fields = [x for x in self.__dict__.keys() if not x.startswith("_")]
            for k, v in data.items():
                if k not in fields:
                    print(f"WARN: Field `{k}` may not be saved!")
                else:
                    setattr(self, k, v)
            try:
                db.session.commit()
            except Exception:
                db.session.rollback()
