from sqlalchemy import Column, ForeignKey, Integer
from pixiv_sql.model.base import BaseModel


class IllustTag(BaseModel):
    """
    IllustTag Model
    """

    __tablename__ = "illusts_tags"

    illust_id = Column(Integer, ForeignKey("bookmarked_illusts.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))
