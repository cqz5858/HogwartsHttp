import pytest
from test_requests.wework.wework_address import WeworkAddress
from test_requests.common.get_random import get_testdata


class TestAddress:
    # name = "cqz"
    # userid = "cqz"
    # mobile = 13800000001
    def setup_class(self):
        self.address = WeworkAddress()
        self.userid = get_testdata()[0]
        self.name = get_testdata()[1]
        self.mobile = get_testdata()[2]
        self.new_name = get_testdata()[1] + "(1)"
        self.department = [1]
        # print(get_testdata()[1:3])

    def setup(self):
        # 前置数据处理
        print("setup")
        self.address.delete(self.userid)
        # raise ValueError()

    def teardown(self):
        # 后置数据处理
        print("teardown")
        self.address.delete(self.userid)

    def test_get_information(self):
        # 数据处理
        self.address.create_member(self.userid, self.name, self.mobile, self.department)
        # 用户信息是不是正确
        r = self.address.get_information(self.userid)
        assert r.get('name') == self.name

    def test_create_member(self):
        r = self.address.create_member(self.userid, self.name, self.mobile, self.department)
        assert r["errmsg"] == "created"
        # 断言
        info = self.address.get_information(self.userid)
        assert info.get('name') == self.name

    # @pytest.mark.parametrize("newname, mobile", get_testdata()[1:3])
    # def test_update_member(self, newname, mobile):
    def test_update_member(self):
        self.address.create_member(self.userid, self.name, self.mobile, self.department)
        # r = self.address.update(self.userid, newname, mobile)
        r = self.address.update(self.userid, self.new_name)
        assert r.get("errmsg") == "updated"
        # 断言
        info = self.address.get_information(self.userid)
        assert info.get('name') == self.new_name

    def test_delete_member(self):
        self.address.create_member(self.userid, self.name, self.mobile, self.department)
        r = self.address.delete(self.userid)
        assert r.get('errmsg') == 'deleted'
        # 断言
        info = self.address.get_information(self.userid)
        assert info.get("errcode") == 60111
