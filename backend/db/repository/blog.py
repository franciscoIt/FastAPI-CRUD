from sqlalchemy.orm import Session 
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from db.models.blog import Blog
from typing import List

def create_new_blog(blog: CreateBlog, db: Session, author_id:int = 1):
    blog = Blog(**blog.model_dump(),author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def retreive_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog



def list_blogs(db : Session) -> List[Blog] :
    blogs = db.query(Blog).all()    
    return blogs


def update_blog(id: int, updated_blog: UpdateBlog, author_id: int, db: Session):
    db_blog = db.query(Blog).filter(Blog.id==id).first()
    if not db_blog:
        return 
    
    db_blog.title = updated_blog.title
    db_blog.content = updated_blog.content

    db.add(db_blog)
    db.commit()
    return db_blog