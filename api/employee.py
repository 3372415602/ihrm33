import app
import requests


class EmpApi:
    def __init__(self):
        # 添加员工
        self.add_emp_url = app.BASE_URL + "/api/sys/user"
        # 查询员工URL
        self.get_emp_url = app.BASE_URL + "/api/sys/user/{}"
        # 修改员工URL
        self.update_emp_url = app.BASE_URL + "/api/sys/user/{}"
        # 删除员工URL
        self.del_emp_url = app.BASE_URL + "/api/sys/user/{}"

    # 添加员工
    def add_emp(self, username, mobile):
        data = {"username": username,
                "mobile": mobile,
                "timeOfEntry": "2019-07-01",
                "formOfEmployment": 1,
                "workNumber": "1322131",
                "departmentId": "1066240656856453120",
                "correctionTime": "2019-11-30"}
        return requests.post(self.add_emp_url, json=data, headers=app.header_data)

    # 查询员工
    def get_emp(self, emp_id):
        url = self.get_emp_url.format(emp_id)
        return requests.get(url, headers=app.header_data)

    # 修改员工
    def update_emp(self, emp_id, username):
        url = self.update_emp_url.format(emp_id)
        data = {"username": username}
        return requests.put(url, json=data, headers=app.header_data)

    # 删除员工
    def del_emp(self, emp_id):
        url = self.del_emp_url.format(emp_id)
        return requests.delete(url, headers=app.header_data)
