from arch import adb


class Activity(object):

    def __init__(self, params={}):
        super(Activity, self).__init__()
        self._package = params.get("package", "com.jamdeo.tv.vod")
        self._class = params.get("class", "com.hisense.base.MainActivity")

    def launch(self):
        print("launch activity (%s/%s)" % (self._package, self._class))
        return adb.open_app(self._package, self._class)
