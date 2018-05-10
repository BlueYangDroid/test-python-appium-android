import time


def sleep(second):
    print("begin sleep %d ....." % second)
    time.sleep(second)
    print("end sleep %d ....." % second)