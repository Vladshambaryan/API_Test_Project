import requests
import allure


class Authorization:
    auth_url = 'http://167.172.172.115:52355/authorize'
    token = None
    response = None

    def is_token_alive(self, token):
        response = requests.get(f'{self.auth_url}/{token}')
        self.response = response
        return response.status_code == 200

    def authorization_token(self):
        if self.token is None or not self.is_token_alive(self.token):
            try:
                response = requests.post(self.auth_url, json={"name": "Vlad"})
                self.response = response
                self.token = response.json().get('token')
            except requests.exceptions.RequestException as exception:
                print(f"Авторизация не удалась: {exception}")
                self.token = None
        return self.token

    @allure.step('Проверить токен не пуст')
    def check_token_not_empty(self):
        assert self.token is not None

    @allure.step('Проверьте код состояния')
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Проверить токен жив')
    def check_token_is_alive(self):
        assert self.is_token_alive(self.token)
