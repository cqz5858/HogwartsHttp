from test_requests.wework.base import Base


class WeworkAddress(Base):
    def get_information(self, userid: str):
        """
        获取成员信息
        :param userid:
        :return:    r.json()
        """
        params = {"userid": userid}
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        r = self.send("GET", url, params=params)
        return r.json()

    def create_member(self, userid: str, name: str, mobile: str, department: list):
        """
        创建成员
        :param userid:
        :param name:
        :param mobile:
        :param department:
        :return:    r.json()
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send("POST", url, json=data)
        return r.json()

    def update(self, userid: str, name: str):
        """
        更新成员
        :param userid:
        :param name:
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name,
            # "mobile": mobile,
            # "department": department
        }
        r = self.send("POST", url, json=data)
        return r.json()

    def delete(self, userid: str):
        params = {"userid": userid}
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        r = self.send("GET", url, params=params)
        return r.json()
