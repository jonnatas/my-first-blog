import pytest
import datetime
from blog.models import Post, Comment

from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

@pytest.mark.django_db(transaction=False)
def test_creation_post():
    post = mommy.make(Post)
    assert isinstance(post, Post)

@pytest.mark.django_db(transaction=False)
def test_approved_comments():
    post = mommy.make(Post)
    commentAproved = mommy.make(Comment)
    commentNotAproved = mommy.make(Comment)
    commentAproved.approve()
    assert commentAproved.post.approved_comments() != []
   
@pytest.mark.django_db(transaction=False)
def test_published():
    post = mommy.make(Post)
    post.publish()
    assert type(post.published_date) == datetime.datetime

@pytest.mark.django_db(transaction=False)
def test_creation_comment():
    comment = mommy.make(Comment)
    assert isinstance(comment, Comment)

@pytest.mark.django_db(transaction=False)
def test_approved():
    comment = mommy.make(Comment)
    comment.approve()
    assert comment.approved_comment == True
