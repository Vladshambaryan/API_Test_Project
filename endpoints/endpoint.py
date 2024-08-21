import allure
import requests


class Endpoint:

    url = 'http://167.172.172.115:52355/meme'
    auth_url = 'http://167.172.172.115:52355/authorize'
    response = None
    json = None
    errors = []
    token = None

    def get_headers(self, token=None):
        if token is None:
            token = self.auth.authorization_token()
        return {
            'Content-Type': 'application/json',
            'Authorization': f'{token}'
        }

    @allure.step('Проверяет код состояния 200')
    def check_status_code_is_correct(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Проверяет код состояния 404')
    def check_status_code_404(self):
        assert self.response.status_code == 404

    @allure.step('Проверяет код состояния 400')
    def check_status_code_400_is_bad_request(self):
        assert self.response.status_code == 400

    @allure.step('Проверяет код состояния 401')
    def check_status_code_401_is_unauthorized(self):
        assert self.response.status_code == 401

    @allure.step('Проверяет текст')
    def check_text_is_correct(self, text):
        assert self.json is not None and self.json['text'] == text

    @allure.step('Проверяет url')
    def check_url_is_correct(self, url):
        assert self.json is not None and self.json['url'] == url

    @allure.step('Проверяет tags')
    def check_tags_is_correct(self, tags):
        assert self.json is not None and self.json['tags'] == tags

    @allure.step('Проверяет info')
    def check_info_is_correct(self, info):
        assert self.json is not None and self.json['info'] == info

    @allure.step('Проверяет id')
    def check_id_is_correct(self, meme_id):
        assert self.json is not None and self.json['id'] == meme_id

    @allure.step('Идентификатор чека не пуст')
    def check_id_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        id_meme = meme.get('id', '')
        if not id:
            self.errors.append(f"Id в меме поле пусто: {id_meme}")

    @allure.step('Текст проверки не пуст')
    def check_text_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        text = meme.get('text', '')
        if not text:
            self.errors.append(f"Text в меме поле пусто: {meme}")

    @allure.step('Проверяет URL-адрес не пуст')
    def check_url_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        url = meme.get('url', '')
        if not url:
            self.errors.append(f"URL в меме поле пусто: {meme}")

    @allure.step('Проверяет теги не пусто')
    def check_tags_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        tags = meme.get('tags', '')
        if not tags:
            self.errors.append(f"Tags в меме поле пусто: {meme}")

    @allure.step('Проверяет информация не пуста')
    def check_info_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        info = meme.get('info', '')
        if not info:
            self.errors.append(f"Info в меме поле пусто: {meme}")

    @allure.step('Проверить токен не пуст')
    def check_token_not_empty(self):
        assert self.token is not None

    @allure.step('Проверить токен жив')
    def check_token_is_alive(self):
        assert self.is_token_alive(self.token)

    def is_token_alive(self, token):
        response = requests.get(f'{self.auth_url}/{token}')
        self.response = response
        return response.status_code == 200
