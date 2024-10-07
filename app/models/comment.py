from __future__ import annotations

from tortoise import Model, fields

from app.models.article import Article
from app.models.base_model import BaseModel


class Comment(BaseModel, Model):
    article: fields.ForeignKeyRelation[Article] = fields.ForeignKeyField(
        "models.Article",
        related_name="comments",
        db_constraint=False,
        # 어차피 아티클 삭제하면 저절로 코멘트들도 삭제되도록 로직을 짜게되기 때문에 false로 하더라도 상관은 없어야 한다 (성능도 이쪽이 빠름...)
    )
    author = fields.CharField(max_length=255)
    body = fields.TextField()

    class Meta:
        table = "comments"

    @classmethod
    async def get_all_by_article_id(cls, article_id: str) -> list[Comment]:
        return await cls.filter(article_id=article_id)
