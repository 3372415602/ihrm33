import unittest
import logging

from api.employee import EmpApi
import utils
import pymysql


class TestEmp(unittest.TestCase):
    emp_id = "1217283469323096064"

    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = EmpApi()

    # 添加员工
    def test01_add_emp(self):
        """添加员工"""
        # 测试数据
        username = "tom11132313111111"
        mobile = "11012000005"

        # 调用接口
        response = self.emp_api.add_emp(username, mobile)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response)

        # 获取员工id
        TestEmp.emp_id = json_data.get("data").get("id")

    # 查询员工
    def test02_get_emp(self):
        # 测试数据
        emp_id = TestEmp.emp_id
        # 调用接口
        response = self.emp_api.get_emp(emp_id)
        json_data = response.json()
        logging.info("test_get_emp json_data={}".format(json_data))
        # 断言
        utils.common_assert(self, response)

    # 修改员工
    def test03_update_emp(self):
        # 测试数据
        emp_id = TestEmp.emp_id
        username = "tom-new22"

        # 调用接口
        response = self.emp_api.update_emp(emp_id, username)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response)

        # 校验数据库中的员工的用户名
        # 获取数据库连接
        conn = pymysql.connect("182.92.81.159", "readuser", "iHRM_user_2019", "ihrm")
        # 获取游标对象
        cursor = conn.cursor()
        # 执行查询操作
        sql = "SELECT t.id,t.username from bs_user t WHERE t.id={}".format(emp_id)
        cursor.execute(sql)
        db_data = cursor.fetchone()
        logging.info("db_data==={}".format(db_data))
        db_username = db_data[1]
        self.assertEqual(username, db_username)
        # 关闭游标对象
        cursor.close()
        # 关闭数据库连接
        conn.close()

    # 删除员工
    def test04_del_emp(self):
        # 测试数据
        emp_id = TestEmp.emp_id

        # 调用接口
        response = self.emp_api.del_emp(emp_id)
        json_data = response.json()
        logging.info("json_data={}".format(json_data))

        # 断言
        utils.common_assert(self, response)
