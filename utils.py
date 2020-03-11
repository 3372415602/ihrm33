

# 通用断言方法
def common_assert(test_case, response, status_code=200, success=True, code=10000, message="操作成功"):
    test_case.assertEqual(status_code, response.status_code)
    test_case.assertEqual(success, response.json().get("success"))
    test_case.assertEqual(code, response.json().get("code"))
    test_case.assertIn(message, response.json().get("message"))



