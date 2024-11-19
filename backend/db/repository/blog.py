from typing import List

from db.models.blog import Blog
from schemas.blog import CreateBlog
from schemas.blog import UpdateBlog
from sqlalchemy.orm import Session


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(**blog.model_dump(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retreive_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def list_blogs(db: Session) -> List[Blog]:
    blogs = db.query(Blog).all()
    return blogs


def update_blog(id: int, updated_blog: UpdateBlog, author_id: int, db: Session):
    db_blog = db.query(Blog).filter(Blog.id == id).first()
    if not db_blog:
        return

    db_blog.title = updated_blog.title
    db_blog.content = updated_blog.content

    db.add(db_blog)
    db.commit()
    return db_blog


def delete_blog_by_ids(id: int, author_id: int, db: Session) -> dict | None:
    """ "
    Notice the use of .first() If we write, blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    Then we will get an actual blog object from the database. This blog object has no delete() method defined.
    So, instead, we are working with the reference of the blog object and deleting it.
    """

    db_blog = db.query(Blog).filter(Blog.id == id)
    response_dict = {}

    if db_blog.first():
        response_dict["msg"] = f"deleted blog with id {id}"

    else:
        response_dict["error"] = f"Could not find blog with id {id}"

    db_blog.delete()
    db.commit()
    return response_dict
