class Option(object):
    INDEX = "index"
    FIND_TYPE = "find_type"
    ACTION = "action"
    ELEMENT_INFO = "element_info"
    TEST_INFO = "test_info"
    DEVICE = "device"
    IS_WEBVIEW = "is_webview"
    CHECK_TIME = "check_time"
    CODE = "code"
    MSG = "msg"
    ASSERT_VALUES = "assert_values"
    ASSERT_TYPE = "assert_type"
    LAUNCH_VALUES = 'launch_values'

class Action(object):
    FIND_ELEMENT_BY_ID = "id"
    FIND_ELEMENTS_BY_ID = "ids"
    FIND_ELEMENT_BY_XPATH = "xpath"
    FIND_ELEMENTS_BY_XPATH = "xpaths"
    FIND_ELEMENT_BY_UISELECT_TEXT = "text"
    FIND_ELEMENTS_BY_UISELECT_TEXT = "texts"
    FIND_ELEMENT_BY_CLASS_NAME = "class_name"
    FIND_ELEMENTS_BY_CLASS_NAME = "class_names"
    CLICK = "click"
    TAP = "tap"
    ACCESSIBILITY = "accessibility"

    ADB_TAP = "adb_tap"

    SWIPE_DOWN = "swipe_down"
    SWIPE_UP = "swipe_up"
    SWIPE_RIGHT = "swipe_right"
    SWIPE_LEFT = "swipe_left"
    SET_VALUE = "set_value"
    GET_VALUE = "get_value"
    WAIT_TIME = 20
    PRESS_KEY_CODE = "press_keycode"

    GET_CONTENT_DESC = "get_content_desc"

    RE_CONNECT = 1 # 是否打开失败后再次运行一次用例

    INFO_FILE = "info.pickle"
    SUM_FILE = "sum.pickle"
    DEVICES_FILE = "devices.pickle"
    REPORT_FILE = "Report.xlsx"

    LAUNCH = "launch"

    ASSERT = "assert"
    ASSERT_TEXT = "assert_text"
    ASSERT_ACTIVITY = "assert_activity"
