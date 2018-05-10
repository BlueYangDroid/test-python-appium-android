from enum import Enum, unique
from selenium.webdriver.common.by import By


@unique
class Action(Enum):
    """
    界面操作
    """

    CLICK = "click"
    SEND_KEY = "send-key"


@unique
class Finder(Enum):
    """
    控件定位的几种方式
    """

    """
    定位单个控件
    """
    ID = "id"
    TAG = "tag"
    CLASS = "class"
    XPATH = "xpath"
    UI_AUTOMATOR = "ui_automator"

    """
    定位多个控件
    """
    ID_2 = "id_2"
    TAG_2 = "tag_2"
    CLASS_2 = "class_2"
    XPATH_2 = "xpath_2"
    UI_AUTOMATOR_2 = "ui_automator_2"

    def is_multi(self):
        return self._name_.endswith("_2")

    def to_by(self):
        if self in [Finder.ID, Finder.ID_2]:
            return By.ID
        elif self in [Finder.CLASS, Finder.CLASS_2]:
            return By.CLASS_NAME
        elif self in [Finder.XPATH, Finder.XPATH_2]:
            return By.XPATH
        elif self in [Finder.UI_AUTOMATOR, Finder.UI_AUTOMATOR_2]:
            return "no_support"
