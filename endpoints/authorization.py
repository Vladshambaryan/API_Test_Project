import requests
from endpoints.endpoint import Endpoint


class Authorization(Endpoint):

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
