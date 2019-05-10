#-*-coding:utf-8-*-
import sqlite3

conn = sqlite3.connect('maintain.db')
cursor = conn.cursor()
# sql = "CREATE TABLE IF NOT EXISTS maintain(AssetNumber,Brand,SerialNumber,IDC,Cabinet,IP,ErrorCode,FaultDiscoveryTime,IDCContactor,FaultSpecificInformation,OperatorDockers,MaintenanceProgress,MaintState,RepairTime,Application,Product,Department,Role,Function,Model,ManagementIP,Operators,CreationTime,Source,Remarks)"
sql = "CREATE TABLE IF NOT EXISTS maintain(AssetNumber TEXT,Brand TEXT,IDC TEXT,Cabinet TEXT,ErrorCode TEXT,IP TEXT,SerialNumber TEXT,ErrorClass TEXT,FaultDiscoveryTime TEXT,IDCContactor TEXT,FaultSpecificInformation TEXT,MaintenanceProgress TEXT,MaintState TEXT,RepairTime TEXT,Application TEXT,Product TEXT,Department TEXT,Role TEXT,Function TEXT,Model TEXT,ManagementIP TEXT,Operators TEXT,CreationTime TEXT,RepairChange TEXT,Remarks TEXT)"

cursor.execute(sql)
conn.close()

