import factory
import pytest
from blog.views import *
from django.test import RequestFactory

@pytest.mark.django_db(transaction=True)
def test_post_list():
    name = 'posts'
    request = RequestFactory().get('blog/post_list')
    response = post_list(request)
    assert response.status_code == 200