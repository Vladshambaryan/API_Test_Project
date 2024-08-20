import allure
from .test_data import invalid_token


@allure.title("Проверить авторизацию – получить действительный токен")
def test_get_token(auth):
    auth.authorization_token()
    auth.check_token_not_empty()
    auth.check_status_code(status_code=200)


@allure.title('Проверьте авторизацию - токен активен')
def test_is_token_alive(auth):
    auth.authorization_token()
    auth.check_token_is_alive()
    auth.check_status_code(status_code=200)


@allure.title('Проверить авторизацию – обновить токен')
def test_refresh_token(auth):
    auth.token = invalid_token
    auth.authorization_token()
    auth.check_token_not_empty()
    auth.check_token_is_alive()
    auth.check_status_code(status_code=200)
