import sys
import os

# sys.path.append(os.path.abspath('C:/Users/PC/PycharmProjects/API_Test_Project'))

import pytest
from endpoints.authorization import Authorization
from endpoints.create_meme import CreateMeme
from endpoints.update_meme import UpdateMeme
from endpoints.get_meme import GetMeme
from endpoints.get_all_memes import GetAllMemes
from endpoints.delete_meme import DeleteMeme


@pytest.fixture(scope='session')
def auth():
    return Authorization()


@pytest.fixture(scope='session')
def token(auth):
    return auth.authorization_token()


@pytest.fixture()
def post_create_meme():
    return CreateMeme()


@pytest.fixture()
def put_update_meme():
    return UpdateMeme()


@pytest.fixture()
def get_request_meme():
    return GetMeme()


@pytest.fixture()
def get_request_all_memes():
    return GetAllMemes()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def new_meme_id(post_create_meme, delete_meme, token):
    payload = {
        "text": "Relax, it's not a competition",
        "url": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2010/07/01/16/405231.jpg",
        "tags": ["squirrel_1", "squirrel_2", "squirrel_3"],
        "info": {"squirrel": ["healthy", "sporty"]}
    }
    response = post_create_meme.new_meme(payload, token)
    meme_id = response.json()['id']
    yield meme_id
    delete_meme.delete_meme_by_id(f'{meme_id}', token)
