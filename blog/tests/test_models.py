
import pytest
from blog.models import Post

from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key


@pytest.mark.django_db(transaction=False)
def test_creation_post():
    post = mommy.make(model=Post)
    assert isinstance(post, Post)

@pytest.mark.django_db(transaction=False)
def test_published():
    post = mommy.make(model=Post)
    Post.publish(post)