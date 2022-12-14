from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import json
import atexit
import os

path = os.getlogin()
process_time = {}
timestamp = {}
all_apps = {'UserName': path}

while True:
    try:
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(
            ".exe", "")
        pid = win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]
        if pid < 0:
            pass
    except psutil.NoSuchProcess:
        pass
    else:
        timestamp[current_app] = int(time.time())
        time.sleep(1)
        if current_app not in process_time.keys():
            process_time[current_app] = 0

        process_time[current_app] = process_time[current_app] + int(time.time()) - timestamp[current_app]

        if current_app not in all_apps.keys():
            key_value = process_time[current_app]
            all_apps.update({current_app: key_value})
        else:
            new_key_value = all_apps[current_app] + process_time[current_app]
            all_apps.update({current_app: new_key_value})

        # print(process_time)
        # print(timestamp)
        # print(all_apps)


        def exit_handler():
            with open("log.json", "w") as outfile:
                json.dump(all_apps, outfile)

        atexit.register(exit_handler)