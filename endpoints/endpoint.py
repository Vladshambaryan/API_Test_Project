import allure
from .authorization import Authorization


class Endpoint:
    url = 'http://167.172.172.115:52355/meme'
    response = None
    json = None
    errors = []
    auth = Authorization()

    def get_headers(self, token=None):
        if token is None:
            token = self.auth.authorization_token()
        return {
            'Content-Type': 'application/json',
            'Authorization': f'{token}'
        }

    def log_response(self):
        if self.response:
            allure.attach(str(self.response.status_code), 'Status Code')
            allure.attach(self.response.text, 'Response Body')

    @allure.step('Проверьте код состояния')
    def check_status_code_is_correct(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Убедитесь, что получена ошибка 400.')
    def check_status_code_is_bad_request(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Проверить текст')
    def check_text_is_correct(self, text):
        assert self.json is not None and self.json['text'] == text

    @allure.step('Проверить url')
    def check_url_is_correct(self, url):
        assert self.json is not None and self.json['url'] == url

    @allure.step('Проверить tags')
    def check_tags_is_correct(self, tags):
        assert self.json is not None and self.json['tags'] == tags

    @allure.step('Проверить info')
    def check_info_is_correct(self, info):
        assert self.json is not None and self.json['info'] == info

    @allure.step('Проверить id')
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

    @allure.step('Проверьте URL-адрес не пуст')
    def check_url_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        url = meme.get('url', '')
        if not url:
            self.errors.append(f"URL в меме поле пусто: {meme}")

    @allure.step('Проверьте теги не пусто')
    def check_tags_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        tags = meme.get('tags', '')
        if not tags:
            self.errors.append(f"Tags в меме поле пусто: {meme}")

    @allure.step('Информация о проверке не пуста')
    def check_info_not_empty(self, meme):
        assert self.json is not None and isinstance(meme, dict)
        info = meme.get('info', '')
        if not info:
            self.errors.append(f"Info в меме поле пусто: {meme}")

    @allure.step('Сообщить об ошибках')
    def report_errors(self):
        if self.errors:
            error_report = '\n'.join(self.errors)
            raise AssertionError(f"Test  со следующими ошибками:\n{error_report}")

    @allure.step('Проверить 401 error')
    def check_status_code_is_unauthorized(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Проверить 403 error')
    def check_status_code_is_forbidden(self, status_code):
        assert self.response.status_code == status_code
