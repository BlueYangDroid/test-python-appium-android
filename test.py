from arch import activity
from arch import consts
from arch import device
from arch import hppium
from arch import tools


if __name__ == '__main__':
    device = device.Device({
        "os_name":      "Android",
        "os_version":   "4.4",
        "ip":           "192.168.1.53",
        "port":         5555
    })

    activity = activity.Activity({
        "package":      "com.jamdeo.tv.vod",
        "class":        "com.hisense.base.MainActivity"
    })

    device.connect()

    hppium = hppium.Hppium(device, activity)
    hppium.start_driver()

    try:
        tools.sleep(3)

        # widget = hppium.find_widget({
        #     "finder":   consts.Finder.ID,
        #     "value":    "com.jamdeo.tv.vod:id/test_list"
        # })
        #
        # if widget.find():
        #     print("find test item list.")
        # else:
        #     exit(0)
        #
        # # FIXME: 以下代码还无法正常工作
        # widget = widget.find_child({
        #     "finder": consts.Finder.XPATH,
        #     "value": "//android.widget.TextView",
        #     # "index": 0
        # })

        widget = hppium.find_widget({
            "finder":   consts.Finder.XPATH_2,
            # "value":    "//android.widget.ListView/android.widget.TextView[contains(@text, '自动化测试')]",
            "value":    "//android.widget.ListView/android.widget.TextView",
            "index": 1
        })

        if widget.find():
            print("widget element parent type: %s" % widget._element._parent)
            print("TextView text: %s" % widget.text())
            # widget.send_keys("abcdefg")
            widget.click()
        else:
            exit(0)

        tools.sleep(3)

        hppium.send_key(20)
        tools.sleep(1)
        hppium.send_key(20)
        tools.sleep(1)
        hppium.send_key(20)
        tools.sleep(1)
        hppium.send_key(19)

        tools.sleep(3)

    # except Exception:
    #     print("exception, fix it.")
    finally:
        hppium.stop_driver()
        device.disconnect()
