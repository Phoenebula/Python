#-*-coding:utf-8-*-
import sqlite3
import xlrd

book = xlrd.open_workbook("机房告警设备明细_处理_顾鑫.xlsx")
sheet = book.sheet_by_name("报修汇总")
conn = sqlite3.connect('maintain.db')
cursor = conn.cursor()

sqlinsert = "insert into maintain (AssetNumber,Brand,IDC,Cabinet,ErrorCode,IP,SerialNumber,ErrorClass,FaultDiscoveryTime,IDCContactor,FaultSpecificInformation,MaintenanceProgress,MaintState,RepairTime,Application,Product,Department,Role,Function,Model,ManagementIP,Operators,CreationTime,RepairChange,Remarks) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"       #注意导入sqlite不能包含单引号‘。
# sqlinsert = "insert into maintain (AssetNumber,Brand,SerialNumber,IDC,Cabinet,IP,ErrorCode,FaultDiscoveryTime,IDCContactor,FaultSpecificInformation,OperatorDockers) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

for r in range(1,sheet.nrows):
    AssetNumber = sheet.cell(r,0).value
    Brand = sheet.cell(r,1).value
    IDC = sheet.cell(r,2).value
    Cabinet = sheet.cell(r,3).value
    ErrorCode = sheet.cell(r,4).value
    IP = sheet.cell(r,5).value
    SerialNumber = sheet.cell(r,6).value
    ErrorClass = sheet.cell(r,7).value
    FaultDiscoveryTime = sheet.cell(r,8).value
    IDCContactor = sheet.cell(r,9).value
    FaultSpecificInformation = sheet.cell(r,10).value
    MaintenanceProgress = sheet.cell(r,11).value
    MaintState = sheet.cell(r,12).value
    RepairTime = sheet.cell(r,13).value
    Application = sheet.cell(r,14).value
    Product = sheet.cell(r,15).value
    Department = sheet.cell(r,16).value
    Role = sheet.cell(r,17).value
    Function = sheet.cell(r,18).value
    Model = sheet.cell(r,19).value
    ManagementIP = sheet.cell(r,20).value
    Operators = sheet.cell(r,21).value
    CreationTime = sheet.cell(r,22).value
    RepairChange = sheet.cell(r,23).value
    Remarks = sheet.cell(r,24).value

    # print(type(FaultSpecificInformation))   #这个添加不进sqlite，多行
    values = (AssetNumber,Brand,IDC,Cabinet,ErrorCode,IP,SerialNumber,ErrorClass,FaultDiscoveryTime,IDCContactor,FaultSpecificInformation,MaintenanceProgress,MaintState,RepairTime,Application,Product,Department,Role,Function,Model,ManagementIP,Operators,CreationTime,RepairChange,Remarks)
    # values = (AssetNumber,Brand,SerialNumber,IDC,Cabinet,IP,ErrorCode,FaultDiscoveryTime,IDCContactor,FaultSpecificInformation,OperatorDockers)
    cursor.execute(sqlinsert % values)
cursor.close()
conn.commit()
conn.close()

columns = str(sheet.ncols)
rows = str(sheet.nrows)
print ("导入 " +columns + " 列 " + rows + " 行数据到SQL数据库!")