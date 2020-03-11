import unittest
import logging

import app
from api.login import LoginApi
import utils
import json
from parameterized import parameterized


# 构造测试数据，读取JSON文件
# [(), (), ()]
def build_data():
    test_data = []
    with open(app.BASE_DIR + "/data/login.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            mobile = case_data.get("mobile")
            pwd = case_data.get("pwd")
            status_code = case_data.get("status_code")
            success = case_data.get("success")
            code = case_data.get("code")
            message = case_data.get("message")
            test_data.append((mobile, pwd, status_code, success, code, message))
        logging.info("test_data={}".format(test_data))
    return test_data
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
    # 登录
    @parameterized.expand(build_data)
    def test_login(self, mobile, pwd, status_code, success, code, message):
        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))
        # 断言
        utils.common_assert(self, response, status_code, success, code, message)
        # 保存token数据
        if success:
            token = json_data.get("data")
            app.header_data["Authorization"] = "Bearer " + token
            print("app.header_data==", app.header_data)
            # app.a = 2

    # 登录成功
    @unittest.skip
    def test_login_success(self):
        # 测试数据
        mobile = "13800000002"
        pwd = "123456"

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, True, 10000, "操作成功")
        # utils.common_assert(self, response)
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, json_data.get("success"))
        # self.assertEqual(10000, json_data.get("code"))
        # self.assertIn("操作成功", json_data.get("message"))

        # 保存token数据
        token = json_data.get("data")
        app.header_data["Authorization"] = "Bearer " + token
        print("app.header_data==", app.header_data)
        # app.a = 2

    # 用户名不存在
    @unittest.skip
    def test_username_is_not_exist(self):
        # 测试数据
        mobile = "13888889919"
        pwd = "123456"

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

        # self.assertEqual(200, response.status_code)
        # self.assertEqual(False, json_data.get("success"))
        # self.assertFalse(json_data.get("success"))
        # self.assertEqual(20001, json_data.get("code"))
        # self.assertIn("用户名或密码错误", json_data.get("message"))

    # 密码错误
    @unittest.skip
    def test_pwd_is_error(self):
        # 测试数据
        mobile = "13800000002"
        pwd = "error"

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 20001, "用户名或密码错误")

    # 请求参数为空
    @unittest.skip
    def test_req_param_is_null(self):
        # 测试数据
        mobile = None
        pwd = None

        # 登录
        response = self.login_api.login(mobile, pwd)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, False, 99999, "系统繁忙")
