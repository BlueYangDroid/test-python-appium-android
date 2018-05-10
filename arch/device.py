from arch import adb
from utils.pylog import Log as L

TAG = 'Device'


class Device(object):

    def __init__(self, params={}):
        super(Device, self).__init__()
        self._os_name = params.get("os_name", "Android")
        self._os_version = params.get("os_version", "4.4")
        self._ip = params.get("ip", "192.168.1.53")
        self._port = params.get("port", 5555)
        self._name = self._ip + ":" + str(self._port)
        L.d("device ip=%s, port=%s" % (self._ip, self._port), tag=TAG)

    def connect(self):
        print("connect to device (ip=%s port=%d)" % (self._ip, self._port))
        return adb.connect(self._name)

    def disconnect(self):
        print("connect to device (ip=%s port=%d)" % (self._ip, self._port))
        return adb.disconnect(self._ip)

    def info(self):
        print("get device info (ip=%s port=%d)" % (self._ip, self._port))
        return adb.get_state()

    def logcat(self):
        print("get logcat of device (ip=%s port=%d)" % (self._ip, self._port))
        # TODO: adb获取日志
        pass


if __name__ == "__main__":
    dev = Device({"ip": "192.168.1.55", "port": 5555})
    dev.connect()
    dev.info()
