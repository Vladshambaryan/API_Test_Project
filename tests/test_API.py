import pytest
import allure
from endpoints.data import (valid_data_create, invalid_data_create, invalid_data_update, valid_data_update,
                                 invalid_token)


@allure.feature('Get')
@pytest.mark.smoke
@allure.title('Получите один мем')
def test_get_one_meme(new_meme_id, get_request_meme, token):
    response = get_request_meme.get_meme_by_id(new_meme_id, token)
    if response is not None:
        get_request_meme.check_id_is_correct(response['id'])
        get_request_meme.check_text_is_correct(response['text'])
        get_request_meme.check_url_is_correct(response['url'])
        get_request_meme.check_tags_is_correct(response['tags'])
        get_request_meme.check_info_is_correct(response['info'])
        get_request_meme.check_response_is_list()
    get_request_meme.check_status_code_is_correct(status_code=200)


@allure.feature('Get')
@pytest.mark.smoke
@allure.title('Получить все мемы')
def test_get_all_meme(get_request_all_memes, token):
    response = get_request_all_memes.get_all_memes(token)
    if response is not None:
        data_list = response.get('data', [])
        get_request_all_memes.check_response_is_list(data_list)
        for meme in data_list:
            get_request_all_memes.check_id_not_empty(meme)
            get_request_all_memes.check_text_not_empty(meme)
            get_request_all_memes.check_url_not_empty(meme)
            get_request_all_memes.check_tags_not_empty(meme)
            get_request_all_memes.check_info_not_empty(meme)
    get_request_all_memes.check_status_code_is_correct(status_code=200)


@allure.feature('Post')
@pytest.mark.regression
@allure.title('Создать новый мем')
@pytest.mark.parametrize('data', valid_data_create)
def test_add_meme(post_create_meme, data, token):
    post_create_meme.new_meme(data, token)
    post_create_meme.check_text_is_correct(data['text'])
    post_create_meme.check_url_is_correct(data['url'])
    post_create_meme.check_tags_is_correct(data['tags'])
    post_create_meme.check_info_is_correct(data['info'])
    post_create_meme.check_status_code_is_correct(status_code=200)


@allure.feature('Post')
@pytest.mark.regression
@allure.title('Создать новый мем - отрицательные тесты')
@pytest.mark.parametrize('data', invalid_data_create)
def test_add_meme_with_negative_data(post_create_meme, data, token):
    post_create_meme.new_meme(data, token)
    post_create_meme.check_status_code_400_is_bad_request_error()


@allure.feature('Put')
@pytest.mark.regression
@allure.title('Обновить мем')
def test_update_meme(new_meme_id, put_update_meme, token):
    data = valid_data_update
    data["id"] = new_meme_id
    put_update_meme.make_changes_in_meme(new_meme_id, data, token)
    put_update_meme.check_text_is_correct(data['text'])
    put_update_meme.check_url_is_correct(data['url'])
    put_update_meme.check_tags_is_correct(data['tags'])
    put_update_meme.check_info_is_correct(data['info'])
    put_update_meme.check_status_code_is_correct(status_code=200)


@allure.feature('Put')
@pytest.mark.regression
@allure.title('Обновление мема - негативный тест')
@pytest.mark.parametrize('data', invalid_data_update)
def test_update_meme_with_negative_data(put_update_meme, new_meme_id, data, token):
    put_update_meme.make_changes_in_meme(new_meme_id, data, token)
    put_update_meme.check_status_code_400_is_bad_request()


@allure.feature('Post')
@pytest.mark.regression
@allure.title('Создать новый мем - неавторизованный пользователь')
def test_add_meme_unauthorized(post_create_meme):
    post_create_meme.new_meme(valid_data_create[0], invalid_token)
    post_create_meme.check_status_code_401_is_unauthorized()


@allure.feature('Delete')
@pytest.mark.regression
@allure.title('Удаление мема')
def test_delete_meme(new_meme_id, delete_meme, token):
    delete_meme.delete_meme_by_id(new_meme_id, token)
    delete_meme.check_status_code_is_correct(status_code=200)
    delete_meme.delete_meme_by_id(new_meme_id, token)
    delete_meme.check_status_code_404()
