import httpx
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from tortoise.contrib.test import TestCase

from app.main import app
from app.models.article import Article
from app.models.comment import Comment


class TestArticleRouter(TestCase):

    async def test_get_article_and_comments(self) -> None:
        # Given
        article_id = "test_article"
        article = await Article.create(id=article_id, author="author", title="title", body="body")

        await Comment.create(id="comment1", article=article, author="c1_author", body="c1_body")
        await Comment.create(id="comment2", article=article, author="c2_author", body="c2_body")

        # When
        async with httpx.AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get(
                url=f"/v1/articles/{article_id}",
                headers={"Accept": "application/json"},
            )

        # Then
        self.assertEqual(response.status_code, HTTP_200_OK)
        response_body = response.json()
        self.assertEqual(response_body["id"], article_id)
        self.assertEqual(response_body["author"], "author")
        self.assertEqual(response_body["title"], "title")
        self.assertEqual(response_body["body"], "body")

        self.assertEqual(len(response_body["comments"]), 2)
        self.assertEqual(response_body["comments"][0]["id"], "comment1")
        self.assertEqual(response_body["comments"][0]["author"], "c1_author")
        self.assertEqual(response_body["comments"][0]["body"], "c1_body")

        self.assertEqual(response_body["comments"][1]["id"], "comment2")
        self.assertEqual(response_body["comments"][1]["author"], "c2_author")
        self.assertEqual(response_body["comments"][1]["body"], "c2_body")

    async def test_when_there_is_no_article(self) -> None:
        # Given
        # no article
        async with httpx.AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get(
                url=f"/v1/articles/test_no_article",
                headers={"Accept": "application/json"},
            )

        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
        response_body = response.json()
        self.assertEqual(response_body.get("detail"), "Article $test_no_article not found")

        # When
