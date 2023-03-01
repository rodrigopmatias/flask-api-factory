from unittest import mock

from flask.testing import FlaskClient

from flask_api_factory.page import Page

from .factories import PetTypeFactory


class TestPage:
    def test_next_when_empty_query(self, client: FlaskClient):
        PetTypeFactory.create_batch(10)
        response = client.get("/v1/pet-types/", query_string={"limit": 5})

        assert response.status_code == 200
        assert response.json["previus"] is None
        assert response.json["next"] is not None

    def test_page_count(self) -> None:
        MockedQuery = mock.Mock()
        MokedSerializer = mock.Mock()

        query = MockedQuery()
        query.count.return_value = 3

        page = Page(query, MokedSerializer)
        assert page.count() == 3
        assert query.count.call_count == 1

        assert page.count() == 3
        assert query.count.call_count == 1
