from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import field_validator


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None

    model_config = ConfigDict(validate_assignment=True)

    @field_validator("slug", mode="before")
    def generate_slug(cls, v, values):
        if not v and "title" in values:
            return values["title"].replace(" ", "-").lower()
        return v


class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: date

    class Config:
        orm_mode = True


class UpdateBlog(CreateBlog):
    pass


class DeleteBlog:
    pass
