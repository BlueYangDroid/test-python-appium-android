class Result(dict):

    def __init__(self):
        super(Result, self).__init__()

    # def __eq__(self, other):
    #     return True

    def match(self, other):
        return self == other


if __name__ == "__main__":
    result1 = Result()
    result1["key1"] = "value1"

    result2 = Result()
    result2["key2"] = "value2"

    print(result1)
    print(result1 == result2)