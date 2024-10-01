FROM python
COPY requirements.txt .
COPY test_API .
COPY test_auth .
RUN mkdir allure-results
RUN pip install -r requirements.txt
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
CMD ["pytest", "test_API.py", "test_aut.py", "--alluredir=allure-results"]