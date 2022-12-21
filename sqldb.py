import json

import pyodbc as pyo
import pymysql

json_data = open("log.json").read()
json_obj = json.loads(json_data)


print("Opening Azure Sql database....")
cnn_azure = (
    r"Driver={SQL Server};Server=gokulproject"
    ".database.windows.net;Database=azure-log-backup;UID=gokul;PWD=rtgg%334!t"
)
cnn = pyo.connect(cnn_azure)
print("Successfully Connected")

cursor=cnn.cursor()

for item in json_obj:
    UserName = item.get("UserName")
    pycharm64 = item.get("pycharm64")
    vpnui = item.get("vpnui")
    msedge = item.get("msedge")
    OUTLOOK = item.get("OUTLOOK.EXE")
    explorer = item.get("explorer")
    cursor.execute("insert into azure-log-backup(UserName,pycharm64,vpnui,msedge,OUTLOOK,explorer)")
