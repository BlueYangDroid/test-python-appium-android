import unittest

from arch import activity
from arch import device
from arch import precondition
from arch import result
from arch import step


class Case(unittest.TestCase):

    def __init__(self):
        super(Case, self).__init__()
        self._precondition = precondition()     # 前置条件
        self._step = step()                     # 测试步骤
        self._expected = result()               # 期望结果
        self._actual = result()                 # 实际结果
        self._logcat = None                     # 日志文件

    def get(self, key):
        if key in ["precondition", "step", "expected", "actual", "logcat"]:
            return getattr(self, "_" + key, None)
        else:
            return None

    def precondition(self, func):
        self._precondition.append(func)

    def step(self, func):
        self._step.append(func)

    def expected(self, key, val):
        self._expected[key] = val

    def actual(self, key, val):
        self._actual[key] = val


if __name__ == "__main__":
    case = Case()
    case.expected("key", "value")
    print(case.get("expected"))
