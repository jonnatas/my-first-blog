import factory
import pytest
from blog.views import *
from django.test import RequestFactory
from blog.models import Post, Comment
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key
from django.contrib.auth.models import User

@pytest.mark.django_db(transaction=False)
def test_post_list():
    name = 'posts'
    request = RequestFactory().get('/')
    response = post_list(request)
    assert response.status_code == 200


@pytest.mark.django_db(transaction=False)
def test_post_remove():
    post = mommy.make(Post)
    request = RequestFactory().get(r'^post/'+str(post.id)+'/remove/$')
    request.user = mommy.make(User)
    request.session = {}
    response = post_remove(request, post.id)
    assert response.status_code == 302

@pytest.mark.django_db(transaction=False)
def test_post_draft_list():
    post1 = mommy.make(Post)
    post2 = mommy.make(Post)
    post3 = mommy.make(Post)
    lista = []
    lista.append(post1)
    lista.append(post2)
    lista.append(post3)
    request = RequestFactory().get(r'^drafts/$')
    request.user = mommy.make(User)
    request.session = {}    
    response = post_draft_list(request)
    assert response.status_code == 200
    assert response.content.post == lista