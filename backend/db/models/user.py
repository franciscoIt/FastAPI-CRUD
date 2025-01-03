from typing import List

from db.base_class import Base
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class User(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True, index=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    blogs: Mapped[list["Blog"]] = relationship("Blog", back_populates="author")
