from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative

"""
With @as_declarative, SQLAlchemy will:

    - Recognize Base as the base class for all models 
    (i.e., any class inheriting from Base will 
    automatically have SQLAlchemy ORM features).

    - Enable configuration of common functionality 
    across models, like automatically generating 
    table names (as shown in your code) or defining 
    shared columns and methods."""

@as_declarative()
class Base:
    id: Any
    __name__: str

    #to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
"""
The @declared_attr decorator is applied to a method 
or attribute in a base class (like Base). 
It indicates that this attribute should be evaluated 
each time a subclass is created. Here, it is used to 
define the __tablename__ attribute, which SQLAlchemy 
uses to name tables in the database.
"""
