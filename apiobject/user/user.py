import re

class HTTP:
    def __init__(self, host) -> None:
        from requests import Session
        import urllib3

        self.host = host
        self.session = Session()
        self.session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def request(self, method, uri, prefix='/dcTrackApp/api/v2', *args, **kwargs):
        url = f'https://{self.host}{prefix}{uri}'
        resp = self.session.request(method, url, *args, **kwargs)
        if resp.ok:
            return resp
        else:
            raise RuntimeError(resp.content.decode('utf-8'))


class User:

    def __init__(self, host: str, username: str, password: str) -> None:
        super().__init__()
        self.username = username
        self.password = password
        self.http = HTTP(host)

    def login(self):
        self.http.session.auth = (self.username, self.password)
        res_login_form = self.http.request('GET', uri='/login', prefix='/login')
        login_authenticity_token = re.search(
            r'name="authenticity_token" value="(\S+)"',
            res_login_form.text
        ).group(1)
        self.http.request(
            method='POST',
            uri='/login',
            prefix='/login',
            data={
                'authenticity_token': login_authenticity_token,
                'login': self.username,
                'password': self.password
            },
            cookies=res_login_form.cookies
        )
        

class Administrator(User):
    def __init__(self, host, username, password):
        super().__init__(host, username, password)
