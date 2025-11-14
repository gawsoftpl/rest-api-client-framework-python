from gawsoft.api_client import Request, Response


class Client(Request):
    def __init__(
        self,
        api_key: str,
        api_host: str = 'http://httpbin.org',
        user_agent: str = 'Example Api Python client'
     ):
        super().__init__(api_key, api_host, user_agent)

    def info(self, url: str, params: dict = {}) -> Response:
        return self.request(url, 'POST', params)


c = Client("abc")
response = c.info("delay/1")
print(response.status_code)
print(response.data())