import random
import uuid
from faker import Faker


class TestDate:
    def get_ranusername(self):
        ranusername = uuid.uuid1()
        return ranusername

    def get_ranmobile(self):
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三位数字
        third = {3: random.randint(0, 9),
                 4: [5, 7, 9][random.randint(0, 2)],
                 5: [i for i in range(10) if i != 4][random.randint(0, 8)],
                 7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
                 8: random.randint(0, 9), }[second]
        # 后面8位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        return f"1{second}{third}{suffix}"

    def testdata(self):
        print(self.get_ranmobile(),self.get_ranusername())
        return (self.get_ranmobile(),self.get_ranusername())


def get_testdata():
    # 用户名， 姓名， 手机号
    faker = Faker(locale='zh_CN')
    return [faker.user_name(), faker.name(), str(faker.phone_number())]