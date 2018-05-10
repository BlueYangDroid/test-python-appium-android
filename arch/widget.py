from arch import consts


class Widget(object):

    def __init__(self, _driver=None, _params={}, _element=None):
        super(Widget, self).__init__()
        self._driver = _driver
        self._params = _params
        self._element = _element

    def find(self):
        if self._element is not None:
            return True

        finder = self._params["finder"]
        if finder is None:
            print("no finder: %s" % self._params)
            return False

        method = self.__get_finder__()[finder]
        if method is None:
            print("no method: %s" % finder)
            return False

        value = self._params["value"]
        if value is None:
            print("no value: %s" % self._params)
            return False

        try:
            element = method(value)
        except Exception:
            print("can not find any element, exception.")
            return False

        if element is None:
            print("widget is not found: %s" % self._params)
            return False
        elif isinstance(element, list):
            print("widget list is found: %s" % element)
            element = element[self._params["index"]]
        else:
            print("widget is found: %s" % element)

        self._element = element
        return True

    def find_children(self, params={}):
        """
        TODO：该接口还不能使用
        :param params: {"finder": consts.Finder.ID, "value": "com.jamdeo.tv.vod:id/test_list"}
        :return: Widget list
        """
        print("find children params: %s" % params)

        if self._element is None:
            print("you need call find() first.")
            return None

        finder = params["finder"]
        if finder is None:
            print("no finder: %s" % params)
            return None

        if not isinstance(finder, consts.Finder):
            finder = consts.Finder(finder)

        value = params["value"]
        if value is None:
            print("no value: %s" % value)
            return None

        print("find children params: %s" % {"by": finder.to_by(), "value": value})
        widgets = map(lambda element: Widget(self._driver, {}, element), self._element.find_element({
            "by": finder.to_by(),
            "value": value
        }))
        return widgets

    def find_child(self, params={}):
        """
        TODO：该接口还不能使用
        :param params: {"finder": consts.Finder.ID, "value": "com.jamdeo.tv.vod:id/test_list", "index": 0}
        :return: Widget
        """

        print("find child params: %s" % params)

        if "index" not in params.keys():
            params["index"] = 0

        widgets = self.find_children(params)
        if widgets is None or widgets.size() == 0:
            return None
        else:
            return widgets[params["index"]]

    def click(self):
        if self._element is None:
            print("you need call find() first.")
        else:
            self._element.click()

    def send_keys(self, keys):
        print("widget send key: %s %s" % (self, keys))
        if self._element is None:
            print("you need call find() first.")
        else:
            self._element.send_keys(keys)

    def text(self):
        return self.__get_attr__("text")

    def width(self):
        """
        TODO：该接口还不能使用
        """
        return self.__get_attr__("width")

    def height(self):
        """
        TODO：该接口还不能使用
        """
        return self.__get_attr__("height")

    def __get_attr__(self, key):
        print("widget get attribute: %s %s" % (self, key))

        if self._element is None:
            print("you need call find() first.")
            return None
        else:
            return self._element.get_attribute(key)

    def __get_finder__(self):
        # TODO: 注意此处并未判断os，只支持android平台。
        return {
            consts.Finder.ID:               self._driver.find_element_by_id,
            consts.Finder.TAG:              self._driver.find_element_by_tag_name,
            consts.Finder.CLASS:            self._driver.find_elements_by_class_name,
            consts.Finder.XPATH:            self._driver.find_element_by_xpath,
            consts.Finder.UI_AUTOMATOR:     self._driver.find_element_by_android_uiautomator,

            consts.Finder.ID_2:             self._driver.find_elements_by_id,
            consts.Finder.TAG_2:            self._driver.find_elements_by_tag_name,
            consts.Finder.CLASS_2:          self._driver.find_elements_by_class_name,
            consts.Finder.XPATH_2:          self._driver.find_elements_by_xpath,
            consts.Finder.UI_AUTOMATOR_2:   self._driver.find_elements_by_android_uiautomator,
        }
