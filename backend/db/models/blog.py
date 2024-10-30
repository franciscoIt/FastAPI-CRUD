from typing import List
from datetime import datetime,date
from sqlalchemy import Text, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base_class import Base

class Blog(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30), nullable=False)
    slug: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    author: Mapped["User"] = relationship("User", back_populates="blogs")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=date.today())
    is_active: Mapped[bool] = mapped_column(Boolean, default=False)