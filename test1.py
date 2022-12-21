# from AppKit import NSWorkspace
# import time
#
# activeWindowTime = ""
#
# while True:
#     new_window_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
#
#     if active_window_lane != new_window_name:
#         active_window_name = new_window_name
#         print(active_window_name)
#
#     time.sleep(10)

# test = {}
# current_app = 'Gopal'
#
# if current_app not in test.keys():
#     test.update({current_app: '45'})
#
# print('Done...')

# import csv
# import atexit
# import ast
#
# csv_columns = ['AppName', 'Time Spend']
# csv_file = "log.csv"
# all_apps = {'pycharm64': '66', 'vpnui': '15', 'OUTLOOK.EXE': '6', 'Teams': '1', 'msedge': '1'}
#
#
#
# def exit_handler(all_apps):
#     with open(csv_file,  encoding="utf-8-sig") as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         writer.writerow(all_apps)
#
#
# atexit.register(exit_handler(all_apps))


# import json
#
# # Data to be written
# dictionary = {
# 'pycharm64': 66,
#     'vpnui': 1,
#     'OUTLOOK.EXE': 6,
#     'Teams': 1,
#     'msedge': 25
# }
#
# # Serializing json
# with open("sample.json", "w") as outfile:
#     json.dump(dictionary, outfile)
# import os
# import getpass
# path = os.path.join('..','Documents and Settings',os.getlogin(),'Desktop')
# path2 = os.path.join('..','Documents and Settings',getpass.getuser(),'Desktop')
# path3 = os.getlogin()
# print(path)
# print(path2)
# print(path3)

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql://gokul:Sunnyday01!@gokulproject.database.windows.net/azure-log-backup")

print("Connection Successfull...")
