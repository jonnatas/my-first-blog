import pytest
from blog.urls import *
from django.test import RequestFactory


@pytest.mark.django_db(transaction=True)
def test_with_client(client):
    response = client.get('/')
    assert response.status_code == 200