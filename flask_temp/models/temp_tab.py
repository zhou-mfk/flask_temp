from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from flask_temp.models import BaseModel


class TempDb(BaseModel):
    __tablename__ = "temp_db"

    username: Mapped[str] = mapped_column(String(128), doc="用户", nullable=True)
    email: Mapped[str] = mapped_column(String(128))
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return check_password_hash(self.password, password)
