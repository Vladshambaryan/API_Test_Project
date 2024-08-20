import requests
import allure
from requests.exceptions import JSONDecodeError
from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    @allure.step('создать новый мем')
    def new_meme(self, payload, token, headers=None):
        headers = headers if headers else self.get_headers(token)
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        try:
            self.json = self.response.json()
        except JSONDecodeError:
            self.json = None
        return self.response
