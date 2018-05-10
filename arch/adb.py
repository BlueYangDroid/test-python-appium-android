import os
import sys
import time


# 运行命令，并同步等待数据返回
def run(command, append=True):
    print("run command: %s" % command)

    result = ("" if append else [])
    shell = os.popen(command, "r")

    while 1:
        line = shell.readline()
        if not line:
            break

        # print("read line: %s" % line)
        if append:
            result += line
        else:
            line = line.replace("\t", " ").replace("\n", "").replace("\r\n", "")
            if len(line):
                result.append(line)

    print("command result: \r\n%s" % result)

    shell.close()
    return result


def run2(command):
    pass


# 连接设备
def connect(device):
    result = run("adb connect %s" % device)
    return result.find("connected to %s" % device) >= 0


# 断开设备
def disconnect(device):
    result = run("adb disconnect %s" % device)
    return result.find("disconnected %s" % device) >= 0


# 检查设备
def devices():
    result = run("adb devices", False)

    devices = []
    for item in result:
        if item.endswith(" device"):
            devices.append(item[:-len(" device")])

    return devices


# 状态
def get_state():
    result = run("adb get-state")
    result = result.strip(' \t\n\r')
    return result or None


# 重启
def reboot(option):
    command = "adb shell reboot"
    if len(option) > 7 and option in ("bootloader", "recovery",):
        command = "%s %s" % (command, option.strip())
    run(command)


# 拷贝数据到设备
def push(local, remote):
    result = run("adb push %s %s" % (local, remote))
    return result


# 拷贝数据到电脑
def pull(remote, local):
    result = run("adb pull %s %s" % (remote, local))
    return result


# 数据同步
def sync(directory, **kwargs):
    command = "adb shell sync %s" % (directory if directory else "")
    if "list" in kwargs:
        command += " -l"
        result = run(command)
        return result


# 打开指定应用
def open_app(package, activity):
    result = run("adb shell am start -n %s/%s" % (package, activity))
    check = result.partition('\n')[2].replace('\n', '').split('\t ')

    if check[0].find("Error") >= 1:
        return False
    else:
        return True


# 根据包名获取进程id
def get_app_pid(package):
    # window使用findstr，linux和mac使用grep
    find = "findstr" if sys.platform.find("win") > 0 else "grep"

    result = run("adb shell ps | %s %s " % (find, package))
    if result == "":
        return "the process doesn't exist."

    result = result.split(" ")
    return result[4]


def logcat():
    file = os.getcwd() + os.sep + time.strftime("%Y%m%d_%H%M%S.log.txt")
    run("adb shell logcat -v threadtime > %s" % file)

def create_logcat(file_name = 'log'):
    file = os.getcwd() + os.sep + time.strftime("%Y%m%d_%H%M%S." + file_name + ".txt")
    os.popen("adb shell logcat -v time > %s" % file)

def stop_logcat():
    os.system(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "utils/kill5037.bat")))

if __name__ == '__main__':
    print("connect 192.168.1.53 result: ", connect("192.168.1.53"))
    print("connect 192.168.1.54 result: ", connect("192.168.1.54"))
    print("disconnect 192.168.1.54 result: ", disconnect("192.168.1.54"))

    print("find devices: ", devices())
    print("sync: ", sync(None))
    print("get state: ", get_state())
    print("start demo: ", open_app("com.hisense.vod", "com.hisense.base.MainActivity"))
    print("get demo pid: ", get_app_pid("com.hisense.vod"))

    logcat()
