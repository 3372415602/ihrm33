import unittest
import app
from script.test_emp import TestEmp
from script.test_login import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestLogin))
# suite.addTest(unittest.makeSuite(TestEmp))

# unittest.TextTestRunner().run(suite)
print("111")

report_file = app.BASE_DIR + "/report/report.html"
with open(report_file, "wb") as f:
    runner = HTMLTestRunner(f, title="ihrm接口测试报告", description="xxx")
    runner.run(suite)
