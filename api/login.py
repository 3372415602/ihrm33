import requests
import app


class LoginApi:

    def __init__(self):
        # 登录URL
        self.login_url = app.BASE_URL + "/api/sys/login"

    # 登录
    def login(self, mobile, pwd):
        # data = {"mobile": mobile, "password": pwd}
        data = None
        if mobile is not None:
            if data is None:
                data = {}
            data["mobile"] = mobile
        if pwd is not None:
            if data is None:
                data = {}
            data["password"] = pwd
        return requests.post(self.login_url, json=data, headers={"Content-Type": "application/json"})
