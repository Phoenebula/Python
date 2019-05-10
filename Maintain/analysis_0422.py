#-*-coding:utf-8-*-
import sqlite3
import numpy as np
import matplotlib.pyplot as plt


conn = sqlite3.connect('maintain.db')
cursor = conn.cursor()

#各服务器总数量
total_dell = 406
total_amax = 632
total_anqing = 199
total_liantai = 531
total_shuguang = 345
total_langchao = 911
total_all = total_dell + total_amax + total_anqing + total_liantai + total_shuguang + total_langchao

#查询各服务器总故障数量
sql_error_total = "select count(*) from maintain"
sql_error_dell = "select count(*) from maintain where Brand = 'DELL'"
sql_error_amax = "select count(*) from maintain where Brand = 'AMAX'"
sql_error_anqing = "select count(*) from maintain where Brand = '安擎'"
sql_error_liantai = "select count(*) from maintain where Brand like '%联泰%'"
sql_error_shuguang = "select count(*) from maintain where Brand = '曙光'"
sql_error_langchao = "select count(*) from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%'"

#查询各服务器发生硬件维修的故障数量
sql_maintain_total = "select count(*) from maintain where RepairChange = 'Y'"
sql_maintain_dell = "select count(*) from (select * from maintain where Brand = 'DELL') where RepairChange = 'Y'"
sql_maintain_amax = "select count(*) from (select * from maintain where Brand = 'AMAX') where RepairChange = 'Y'"
sql_maintain_anqing = "select count(*) from (select * from maintain where Brand = '安擎') where RepairChange = 'Y'"
sql_maintain_liantai = "select count(*) from (select * from maintain where Brand like '联泰') where RepairChange = 'Y'"
sql_maintain_shuguang = "select count(*) from (select * from maintain where Brand = '曙光') where RepairChange = 'Y'"
sql_maintain_langchao = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where RepairChange = 'Y'"

#各服务器总故障数量
cursor.execute(sql_error_total)
error_total = cursor.fetchone()
# print(number_total)
print("所有故障数量：",error_total[0])
# print(type(number_total[0]))
#Dell故障数量
cursor.execute(sql_error_dell)
error_dell = cursor.fetchone()
print("Dell故障数量：",error_dell[0])
#amax故障数量
cursor.execute(sql_error_amax)
error_amax = cursor.fetchone()
print("AMAX故障数量：",error_amax[0])
#安擎故障数量
cursor.execute(sql_error_anqing)
error_anqing = cursor.fetchone()
print("安擎故障数量：",error_anqing[0])
#联泰故障数量
cursor.execute(sql_error_liantai)
error_liantai = cursor.fetchone()
print("联泰故障数量：",error_liantai[0])
#曙光故障数量
cursor.execute(sql_error_shuguang)
error_shuguang = cursor.fetchone()
print("曙光故障数量：",error_shuguang[0])
#浪潮故障数量
cursor.execute(sql_error_langchao)
error_langchao = cursor.fetchone()
print("浪潮故障数量：",error_langchao[0])


#各服务器发生硬件维修的故障数量
cursor.execute(sql_maintain_total)
maintain_total = cursor.fetchone()
# print(number_total)
print("所有硬件维修故障数量：",maintain_total[0])
# print(type(number_total[0]))
#Dell故障数量
cursor.execute(sql_maintain_dell)
maintain_dell = cursor.fetchone()
print("Dell硬件维修故障数量：",maintain_dell[0])
#amax故障数量
cursor.execute(sql_maintain_amax)
maintain_amax = cursor.fetchone()
print("AMAX硬件维修故障数量：",maintain_amax[0])
#安擎故障数量
cursor.execute(sql_maintain_anqing)
maintain_anqing = cursor.fetchone()
print("安擎硬件维修故障数量：",maintain_anqing[0])
#联泰故障数量
cursor.execute(sql_maintain_liantai)
maintain_liantai = cursor.fetchone()
print("联泰硬件维修故障数量：",maintain_liantai[0])
#曙光故障数量
cursor.execute(sql_maintain_shuguang)
maintain_shuguang = cursor.fetchone()
print("曙光硬件维修故障数量：",maintain_shuguang[0])
#浪潮故障数量
cursor.execute(sql_maintain_langchao)
maintain_langchao = cursor.fetchone()
print("浪潮硬件维修故障数量：",maintain_langchao[0])

#硬件维修故障数量占服务器数量百分比
#Dell硬件维修故障数量占Dell服务器数量百分比
maintain_percent_dell = ('{:.2f}%'.format(maintain_dell[0]/total_dell*100))   #输出为百分比
print("Dell硬件维修故障数量占Dell服务器数量百分比：",maintain_percent_dell)
#amax硬件维修故障数量占amax服务器数量百分比
maintain_percent_amax = ('{:.2f}%'.format(maintain_amax[0]/total_amax*100))   #输出为百分比
print("amax硬件维修故障数量占amax服务器数量百分比：",maintain_percent_amax)
#安擎硬件维修故障数量占安擎服务器数量百分比
maintain_percent_anqing = ('{:.2f}%'.format(maintain_anqing[0]/total_anqing*100))   #输出为百分比
print("安擎硬件维修故障数量占安擎服务器数量百分比：",maintain_percent_anqing)
#联泰硬件维修故障数量占联泰服务器数量百分比
maintain_percent_liantai = ('{:.2f}%'.format(maintain_liantai[0]/total_liantai*100))   #输出为百分比
print("联泰硬件维修故障数量占联泰服务器数量百分比：",maintain_percent_liantai)
#曙光硬件维修故障数量占曙光服务器数量百分比
maintain_percent_shuguang = ('{:.2f}%'.format(maintain_shuguang[0]/total_shuguang*100))   #输出为百分比
print("曙光硬件维修故障数量占曙光服务器数量百分比：",maintain_percent_shuguang)
#浪潮硬件维修故障数量占浪潮服务器数量百分比
maintain_percent_langchao = ('{:.2f}%'.format(maintain_langchao[0]/total_langchao*100))   #输出为百分比
print("浪潮硬件维修故障数量占浪潮服务器数量百分比：",maintain_percent_langchao)
#所有服务器硬件维修故障数量占服务器数量百分比
maintain_percent_total = ('{:.2f}%'.format(maintain_total[0]/total_all*100))   #输出为百分比
print("所有服务器硬件维修故障数量占服务器数量百分比：",maintain_percent_total)


#分类故障数量
#Dell
#Raid
#Raid卡
sql_error_dell_Raid_Raidsas = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = 'Raid卡'"
#硬盘故障
sql_error_dell_Raid_Disk = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '硬盘故障'"

#IPMI
#电源报错
sql_error_dell_Ipmi_PsError = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '电源报错'"
#电源松动
sql_error_dell_Ipmi_PsLoose = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '电源松动'"
#风扇故障
sql_error_dell_Ipmi_FanError = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '风扇故障'"
#风扇降速
sql_error_dell_Ipmi_FanLow = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '风扇降速'"
#PCIE中断
sql_error_dell_Ipmi_PCIE = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = 'PCIE中断'"
#温度
sql_error_dell_Ipmi_Temp = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '温度'"
#机箱入侵
sql_error_dell_Ipmi_Chassis = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '机箱入侵'"

#GPU
#GPU掉卡
sql_error_dell_GPU_GpuLost = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = 'GPU掉卡'"
#GPUError
sql_error_dell_GPU_GpuError = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = 'GPUError'"
#烤机失败
sql_error_dell_GPU_GpuBurn = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '烤机失败'"

#Dmesg
#内存报错
sql_error_dell_Dmesg_Mem = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '内存报错'"
#OOM    #非硬件故障
sql_error_dell_Dmesg_Oom = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = 'OOM'"

#IB故障
#网线故障
sql_error_dell_IB_Cable = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '网线故障'"
#IB卡故障
sql_error_dell_IB_Card = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = 'IB卡故障'"

#ICMP
#宕机
sql_error_dell_ICMP_Dump = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = '宕机'"
#路由 #非硬件故障
sql_error_dell_ICMP_Route = "select count(*) from (select * from (select * from maintain where Brand = 'DELL') where ErrorClass = '路由') where RepairChange = 'Y'"
#测试维修   #非硬件故障
sql_error_dell_ICMP_TestMain = "select count(*) from (select * from (select * from maintain where Brand = 'DELL') where ErrorClass = '测试维修') where RepairChange = 'Y'"

#通用
#配置变更     #非硬件故障
sql_error_dell_Cfgchange = "select count(*) from (select * from (select * from maintain where Brand = 'DELL') where ErrorClass = '配置变更') where RepairChange = 'Y'"
#驱动   #非硬件故障
sql_error_dell_Drive = "select count(*) from (select * from (select * from maintain where Brand = 'DELL') where ErrorClass = '驱动') where RepairChange = 'Y'"
#Other
sql_error_dell_Other = "select count(*) from (select * from maintain where Brand = 'DELL') where ErrorClass = 'Other'"

#Dell分类故障数量
#Dell故障数量Raid卡
cursor.execute(sql_error_dell_Raid_Raidsas)
error_dell_Raid_Raidsas = cursor.fetchone()
print("Dell故障数量Raid卡：",error_dell_Raid_Raidsas[0])
#Dell故障数量硬盘故障
cursor.execute(sql_error_dell_Raid_Disk)
error_dell_Raid_Disk = cursor.fetchone()
print("Dell故障数量硬盘故障：",error_dell_Raid_Disk[0])
#Dell故障数量电源报错
cursor.execute(sql_error_dell_Ipmi_PsError)
error_dell_Ipmi_PsError = cursor.fetchone()
print("Dell故障数量电源报错：",error_dell_Ipmi_PsError[0])
#Dell故障数量电源松动
cursor.execute(sql_error_dell_Ipmi_PsLoose)
error_dell_Ipmi_PsLoose = cursor.fetchone()
print("Dell故障数量电源松动：",error_dell_Ipmi_PsLoose[0])
#Dell故障数量风扇故障
cursor.execute(sql_error_dell_Ipmi_FanError)
error_dell_Ipmi_FanError = cursor.fetchone()
print("Dell故障数量风扇故障：",error_dell_Ipmi_FanError[0])
#Dell故障数量风扇降速
cursor.execute(sql_error_dell_Ipmi_FanLow)
error_dell_Ipmi_FanLow = cursor.fetchone()
print("Dell故障数量风扇降速：",error_dell_Ipmi_FanLow[0])
#Dell故障数量PCIE中断
cursor.execute(sql_error_dell_Ipmi_PCIE)
error_dell_Ipmi_PCIE = cursor.fetchone()
print("Dell故障数量PCIE中断：",error_dell_Ipmi_PCIE[0])
#Dell故障数量温度
cursor.execute(sql_error_dell_Ipmi_Temp)
error_dell_Ipmi_Temp = cursor.fetchone()
print("Dell故障数量温度：",error_dell_Ipmi_Temp[0])
#Dell故障数量机箱入侵
cursor.execute(sql_error_dell_Ipmi_Chassis)
error_dell_Ipmi_Chassis = cursor.fetchone()
print("Dell故障数量机箱入侵：",error_dell_Ipmi_Chassis[0])
#Dell故障数量GPU掉卡
cursor.execute(sql_error_dell_GPU_GpuLost)
error_dell_GPU_GpuLost = cursor.fetchone()
print("Dell故障数量GPU掉卡：",error_dell_GPU_GpuLost[0])
#Dell故障数量GPUError
cursor.execute(sql_error_dell_GPU_GpuError)
error_dell_GPU_GpuError = cursor.fetchone()
print("Dell故障数量GPUError：",error_dell_GPU_GpuError[0])
#Dell故障数量烤机失败
cursor.execute(sql_error_dell_GPU_GpuBurn)
error_dell_GPU_GpuBurn = cursor.fetchone()
print("Dell故障数量烤机失败：",error_dell_GPU_GpuBurn[0])
#Dell故障数量内存报错
cursor.execute(sql_error_dell_Dmesg_Mem)
error_dell_Dmesg_Mem = cursor.fetchone()
print("Dell故障数量内存报错：",error_dell_Dmesg_Mem[0])
#Dell故障数量网线故障
cursor.execute(sql_error_dell_IB_Cable)
error_dell_IB_Cable = cursor.fetchone()
print("Dell故障数量网线故障：",error_dell_IB_Cable[0])
#Dell故障数量IB卡故障
cursor.execute(sql_error_dell_IB_Card)
error_dell_IB_Card = cursor.fetchone()
print("Dell故障数量IB卡故障：",error_dell_IB_Card[0])
#Dell故障数量宕机
cursor.execute(sql_error_dell_ICMP_Dump)
error_dell_ICMP_Dump = cursor.fetchone()
print("Dell故障数量宕机：",error_dell_ICMP_Dump[0])

#Dell故障数量_Other
cursor.execute(sql_error_dell_Other)
error_dell_Other = cursor.fetchone()
print("Dell故障数量_Other：",error_dell_Other[0])
#Dell 故障数量_Raid
error_dell_Raid = error_dell_Raid_Disk[0] + error_dell_Raid_Raidsas[0]
print("Dell故障数量_Raid：",error_dell_Raid)
#Dell 故障数量_IPMI
error_dell_Ipmi = error_dell_Ipmi_PsError[0] + error_dell_Ipmi_PsLoose[0] + error_dell_Ipmi_FanError[0] + error_dell_Ipmi_FanLow[0] + error_dell_Ipmi_PCIE[0] + error_dell_Ipmi_Temp[0] + error_dell_Ipmi_Chassis[0]
print("Dell故障数量_IPMI：",error_dell_Ipmi)
#Dell 故障数量_GPU
error_dell_GPU = error_dell_GPU_GpuLost[0] + error_dell_GPU_GpuError[0] + error_dell_GPU_GpuBurn[0]
print("Dell故障数量_GPU：",error_dell_GPU)
#Dell 故障数量_Dmesg
error_dell_Dmesg = error_dell_Dmesg_Mem[0]
print("Dell故障数量_Dmesg：",error_dell_Dmesg)
#Dell 故障数量_IB
error_dell_IB = error_dell_IB_Cable[0] + error_dell_IB_Card[0]
print("Dell故障数量_IB：",error_dell_IB)
#Dell 故障数量_宕机
error_dell_Dump = error_dell_ICMP_Dump[0]
print("Dell故障数量_宕机：",error_dell_Dump)
#Dell 硬件故障数量
error_dell_hardware = error_dell_Raid + error_dell_Ipmi + error_dell_GPU + error_dell_Dmesg + error_dell_IB + error_dell_Dump + error_dell_Other[0]
print("Dell硬件故障数量：",error_dell_hardware)

#分类故障数量
#amax
#Raid
#Raid卡
sql_error_amax_Raid_Raidsas = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = 'Raid卡'"
#硬盘故障
sql_error_amax_Raid_Disk = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '硬盘故障'"

#IPMI
#电源报错
sql_error_amax_Ipmi_PsError = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '电源报错'"
#电源松动
sql_error_amax_Ipmi_PsLoose = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '电源松动'"
#风扇故障
sql_error_amax_Ipmi_FanError = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '风扇故障'"
#风扇降速
sql_error_amax_Ipmi_FanLow = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '风扇降速'"
#PCIE中断
sql_error_amax_Ipmi_PCIE = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = 'PCIE中断'"
#温度
sql_error_amax_Ipmi_Temp = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '温度'"
#机箱入侵
sql_error_amax_Ipmi_Chassis = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '机箱入侵'"

#GPU
#GPU掉卡
sql_error_amax_GPU_GpuLost = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = 'GPU掉卡'"
#GPUError
sql_error_amax_GPU_GpuError = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = 'GPUError'"
#烤机失败
sql_error_amax_GPU_GpuBurn = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '烤机失败'"

#Dmesg
#内存报错
sql_error_amax_Dmesg_Mem = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '内存报错'"
#OOM    #非硬件故障
sql_error_amax_Dmesg_Oom = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = 'OOM'"

#IB故障
#网线故障
sql_error_amax_IB_Cable = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '网线故障'"
#IB卡故障
sql_error_amax_IB_Card = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = 'IB卡故障'"

#ICMP
#宕机
sql_error_amax_ICMP_Dump = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = '宕机'"
#路由 #非硬件故障
sql_error_amax_ICMP_Route = "select count(*) from (select * from (select * from maintain where Brand = 'AMAX') where ErrorClass = '路由') where RepairChange = 'Y'"
#测试维修   #非硬件故障
sql_error_amax_ICMP_TestMain = "select count(*) from (select * from (select * from maintain where Brand = 'AMAX') where ErrorClass = '测试维修') where RepairChange = 'Y'"

#通用
#配置变更     #非硬件故障
sql_error_amax_Cfgchange = "select count(*) from (select * from (select * from maintain where Brand = 'AMAX') where ErrorClass = '配置变更') where RepairChange = 'Y'"
#驱动   #非硬件故障
sql_error_amax_Drive = "select count(*) from (select * from (select * from maintain where Brand = 'AMAX') where ErrorClass = '驱动') where RepairChange = 'Y'"
#Other
sql_error_amax_Other = "select count(*) from (select * from maintain where Brand = 'AMAX') where ErrorClass = 'Other'"

#amax分类故障数量
#amax故障数量Raid卡
cursor.execute(sql_error_amax_Raid_Raidsas)
error_amax_Raid_Raidsas = cursor.fetchone()
print("amax故障数量Raid卡：",error_amax_Raid_Raidsas[0])
#amax故障数量硬盘故障
cursor.execute(sql_error_amax_Raid_Disk)
error_amax_Raid_Disk = cursor.fetchone()
print("amax故障数量硬盘故障：",error_amax_Raid_Disk[0])
#amax故障数量电源报错
cursor.execute(sql_error_amax_Ipmi_PsError)
error_amax_Ipmi_PsError = cursor.fetchone()
print("amax故障数量电源报错：",error_amax_Ipmi_PsError[0])
#amax故障数量电源松动
cursor.execute(sql_error_amax_Ipmi_PsLoose)
error_amax_Ipmi_PsLoose = cursor.fetchone()
print("amax故障数量电源松动：",error_amax_Ipmi_PsLoose[0])
#amax故障数量风扇故障
cursor.execute(sql_error_amax_Ipmi_FanError)
error_amax_Ipmi_FanError = cursor.fetchone()
print("amax故障数量风扇故障：",error_amax_Ipmi_FanError[0])
#amax故障数量风扇降速
cursor.execute(sql_error_amax_Ipmi_FanLow)
error_amax_Ipmi_FanLow = cursor.fetchone()
print("amax故障数量风扇降速：",error_amax_Ipmi_FanLow[0])
#amax故障数量PCIE中断
cursor.execute(sql_error_amax_Ipmi_PCIE)
error_amax_Ipmi_PCIE = cursor.fetchone()
print("amax故障数量PCIE中断：",error_amax_Ipmi_PCIE[0])
#amax故障数量温度
cursor.execute(sql_error_amax_Ipmi_Temp)
error_amax_Ipmi_Temp = cursor.fetchone()
print("amax故障数量温度：",error_amax_Ipmi_Temp[0])
#amax故障数量机箱入侵
cursor.execute(sql_error_amax_Ipmi_Chassis)
error_amax_Ipmi_Chassis = cursor.fetchone()
print("amax故障数量机箱入侵：",error_amax_Ipmi_Chassis[0])
#amax故障数量GPU掉卡
cursor.execute(sql_error_amax_GPU_GpuLost)
error_amax_GPU_GpuLost = cursor.fetchone()
print("amax故障数量GPU掉卡：",error_amax_GPU_GpuLost[0])
#amax故障数量GPUError
cursor.execute(sql_error_amax_GPU_GpuError)
error_amax_GPU_GpuError = cursor.fetchone()
print("amax故障数量GPUError：",error_amax_GPU_GpuError[0])
#amax故障数量烤机失败
cursor.execute(sql_error_amax_GPU_GpuBurn)
error_amax_GPU_GpuBurn = cursor.fetchone()
print("amax故障数量烤机失败：",error_amax_GPU_GpuBurn[0])
#amax故障数量内存报错
cursor.execute(sql_error_amax_Dmesg_Mem)
error_amax_Dmesg_Mem = cursor.fetchone()
print("amax故障数量内存报错：",error_amax_Dmesg_Mem[0])
#amax故障数量网线故障
cursor.execute(sql_error_amax_IB_Cable)
error_amax_IB_Cable = cursor.fetchone()
print("amax故障数量网线故障：",error_amax_IB_Cable[0])
#amax故障数量IB卡故障
cursor.execute(sql_error_amax_IB_Card)
error_amax_IB_Card = cursor.fetchone()
print("amax故障数量IB卡故障：",error_amax_IB_Card[0])
#amax故障数量宕机
cursor.execute(sql_error_amax_ICMP_Dump)
error_amax_ICMP_Dump = cursor.fetchone()
print("amax故障数量宕机：",error_amax_ICMP_Dump[0])

#amax故障数量_Other
cursor.execute(sql_error_amax_Other)
error_amax_Other = cursor.fetchone()
print("amax故障数量_Other：",error_amax_Other[0])
#amax 故障数量_Raid
error_amax_Raid = error_amax_Raid_Disk[0] + error_amax_Raid_Raidsas[0]
print("amax故障数量_Raid：",error_amax_Raid)
#amax 故障数量_IPMI
error_amax_Ipmi = error_amax_Ipmi_PsError[0] + error_amax_Ipmi_PsLoose[0] + error_amax_Ipmi_FanError[0] + error_amax_Ipmi_FanLow[0] + error_amax_Ipmi_PCIE[0] + error_amax_Ipmi_Temp[0] + error_amax_Ipmi_Chassis[0]
print("amax故障数量_IPMI：",error_amax_Ipmi)
#amax 故障数量_GPU
error_amax_GPU = error_amax_GPU_GpuLost[0] + error_amax_GPU_GpuError[0] + error_amax_GPU_GpuBurn[0]
print("amax故障数量_GPU：",error_amax_GPU)
#amax 故障数量_Dmesg
error_amax_Dmesg = error_amax_Dmesg_Mem[0]
print("amax故障数量_Dmesg：",error_amax_Dmesg)
#amax 故障数量_IB
error_amax_IB = error_amax_IB_Cable[0] + error_amax_IB_Card[0]
print("amax故障数量_IB：",error_amax_IB)
#amax 故障数量_宕机
error_amax_Dump = error_amax_ICMP_Dump[0]
print("amax故障数量_宕机：",error_amax_Dump)
#amax 硬件故障数量
error_amax_hardware = error_amax_Raid + error_amax_Ipmi + error_amax_GPU + error_amax_Dmesg + error_amax_IB + error_amax_Dump + error_amax_Other[0]
print("amax硬件故障数量：",error_amax_hardware)

#分类故障数量
#anqing
#Raid
#Raid卡
sql_error_anqing_Raid_Raidsas = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = 'Raid卡'"
#硬盘故障
sql_error_anqing_Raid_Disk = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '硬盘故障'"

#IPMI
#电源报错
sql_error_anqing_Ipmi_PsError = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '电源报错'"
#电源松动
sql_error_anqing_Ipmi_PsLoose = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '电源松动'"
#风扇故障
sql_error_anqing_Ipmi_FanError = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '风扇故障'"
#风扇降速
sql_error_anqing_Ipmi_FanLow = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '风扇降速'"
#PCIE中断
sql_error_anqing_Ipmi_PCIE = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = 'PCIE中断'"
#温度
sql_error_anqing_Ipmi_Temp = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '温度'"
#机箱入侵
sql_error_anqing_Ipmi_Chassis = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '机箱入侵'"

#GPU
#GPU掉卡
sql_error_anqing_GPU_GpuLost = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = 'GPU掉卡'"
#GPUError
sql_error_anqing_GPU_GpuError = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = 'GPUError'"
#烤机失败
sql_error_anqing_GPU_GpuBurn = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '烤机失败'"

#Dmesg
#内存报错
sql_error_anqing_Dmesg_Mem = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '内存报错'"
#OOM    #非硬件故障
sql_error_anqing_Dmesg_Oom = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = 'OOM'"

#IB故障
#网线故障
sql_error_anqing_IB_Cable = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '网线故障'"
#IB卡故障
sql_error_anqing_IB_Card = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = 'IB卡故障'"

#ICMP
#宕机
sql_error_anqing_ICMP_Dump = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = '宕机'"
#路由 #非硬件故障
sql_error_anqing_ICMP_Route = "select count(*) from (select * from (select * from maintain where Brand = '安擎') where ErrorClass = '路由') where RepairChange = 'Y'"
#测试维修   #非硬件故障
sql_error_anqing_ICMP_TestMain = "select count(*) from (select * from (select * from maintain where Brand = '安擎') where ErrorClass = '测试维修') where RepairChange = 'Y'"

#通用
#配置变更     #非硬件故障
sql_error_anqing_Cfgchange = "select count(*) from (select * from (select * from maintain where Brand = '安擎') where ErrorClass = '配置变更') where RepairChange = 'Y'"
#驱动   #非硬件故障
sql_error_anqing_Drive = "select count(*) from (select * from (select * from maintain where Brand = '安擎') where ErrorClass = '驱动') where RepairChange = 'Y'"
#Other
sql_error_anqing_Other = "select count(*) from (select * from maintain where Brand = '安擎') where ErrorClass = 'Other'"

#anqing分类故障数量
#anqing故障数量Raid卡
cursor.execute(sql_error_anqing_Raid_Raidsas)
error_anqing_Raid_Raidsas = cursor.fetchone()
print("anqing故障数量Raid卡：",error_anqing_Raid_Raidsas[0])
#anqing故障数量硬盘故障
cursor.execute(sql_error_anqing_Raid_Disk)
error_anqing_Raid_Disk = cursor.fetchone()
print("anqing故障数量硬盘故障：",error_anqing_Raid_Disk[0])
#anqing故障数量电源报错
cursor.execute(sql_error_anqing_Ipmi_PsError)
error_anqing_Ipmi_PsError = cursor.fetchone()
print("anqing故障数量电源报错：",error_anqing_Ipmi_PsError[0])
#anqing故障数量电源松动
cursor.execute(sql_error_anqing_Ipmi_PsLoose)
error_anqing_Ipmi_PsLoose = cursor.fetchone()
print("anqing故障数量电源松动：",error_anqing_Ipmi_PsLoose[0])
#anqing故障数量风扇故障
cursor.execute(sql_error_anqing_Ipmi_FanError)
error_anqing_Ipmi_FanError = cursor.fetchone()
print("anqing故障数量风扇故障：",error_anqing_Ipmi_FanError[0])
#anqing故障数量风扇降速
cursor.execute(sql_error_anqing_Ipmi_FanLow)
error_anqing_Ipmi_FanLow = cursor.fetchone()
print("anqing故障数量风扇降速：",error_anqing_Ipmi_FanLow[0])
#anqing故障数量PCIE中断
cursor.execute(sql_error_anqing_Ipmi_PCIE)
error_anqing_Ipmi_PCIE = cursor.fetchone()
print("anqing故障数量PCIE中断：",error_anqing_Ipmi_PCIE[0])
#anqing故障数量温度
cursor.execute(sql_error_anqing_Ipmi_Temp)
error_anqing_Ipmi_Temp = cursor.fetchone()
print("anqing故障数量温度：",error_anqing_Ipmi_Temp[0])
#anqing故障数量机箱入侵
cursor.execute(sql_error_anqing_Ipmi_Chassis)
error_anqing_Ipmi_Chassis = cursor.fetchone()
print("anqing故障数量机箱入侵：",error_anqing_Ipmi_Chassis[0])
#anqing故障数量GPU掉卡
cursor.execute(sql_error_anqing_GPU_GpuLost)
error_anqing_GPU_GpuLost = cursor.fetchone()
print("anqing故障数量GPU掉卡：",error_anqing_GPU_GpuLost[0])
#anqing故障数量GPUError
cursor.execute(sql_error_anqing_GPU_GpuError)
error_anqing_GPU_GpuError = cursor.fetchone()
print("anqing故障数量GPUError：",error_anqing_GPU_GpuError[0])
#anqing故障数量烤机失败
cursor.execute(sql_error_anqing_GPU_GpuBurn)
error_anqing_GPU_GpuBurn = cursor.fetchone()
print("anqing故障数量烤机失败：",error_anqing_GPU_GpuBurn[0])
#anqing故障数量内存报错
cursor.execute(sql_error_anqing_Dmesg_Mem)
error_anqing_Dmesg_Mem = cursor.fetchone()
print("anqing故障数量内存报错：",error_anqing_Dmesg_Mem[0])
#anqing故障数量网线故障
cursor.execute(sql_error_anqing_IB_Cable)
error_anqing_IB_Cable = cursor.fetchone()
print("anqing故障数量网线故障：",error_anqing_IB_Cable[0])
#anqing故障数量IB卡故障
cursor.execute(sql_error_anqing_IB_Card)
error_anqing_IB_Card = cursor.fetchone()
print("anqing故障数量IB卡故障：",error_anqing_IB_Card[0])
#anqing故障数量宕机
cursor.execute(sql_error_anqing_ICMP_Dump)
error_anqing_ICMP_Dump = cursor.fetchone()
print("anqing故障数量宕机：",error_anqing_ICMP_Dump[0])

#anqing故障数量_Other
cursor.execute(sql_error_anqing_Other)
error_anqing_Other = cursor.fetchone()
print("anqing故障数量_Other：",error_anqing_Other[0])
#anqing 故障数量_Raid
error_anqing_Raid = error_anqing_Raid_Disk[0] + error_anqing_Raid_Raidsas[0]
print("anqing故障数量_Raid：",error_anqing_Raid)
#anqing 故障数量_IPMI
error_anqing_Ipmi = error_anqing_Ipmi_PsError[0] + error_anqing_Ipmi_PsLoose[0] + error_anqing_Ipmi_FanError[0] + error_anqing_Ipmi_FanLow[0] + error_anqing_Ipmi_PCIE[0] + error_anqing_Ipmi_Temp[0] + error_anqing_Ipmi_Chassis[0]
print("anqing故障数量_IPMI：",error_anqing_Ipmi)
#anqing 故障数量_GPU
error_anqing_GPU = error_anqing_GPU_GpuLost[0] + error_anqing_GPU_GpuError[0] + error_anqing_GPU_GpuBurn[0]
print("anqing故障数量_GPU：",error_anqing_GPU)
#anqing 故障数量_Dmesg
error_anqing_Dmesg = error_anqing_Dmesg_Mem[0]
print("anqing故障数量_Dmesg：",error_anqing_Dmesg)
#anqing 故障数量_IB
error_anqing_IB = error_anqing_IB_Cable[0] + error_anqing_IB_Card[0]
print("anqing故障数量_IB：",error_anqing_IB)
#anqing 故障数量_宕机
error_anqing_Dump = error_anqing_ICMP_Dump[0]
print("anqing故障数量_宕机：",error_anqing_Dump)
#anqing 硬件故障数量
error_anqing_hardware = error_anqing_Raid + error_anqing_Ipmi + error_anqing_GPU + error_anqing_Dmesg + error_anqing_IB + error_anqing_Dump + error_anqing_Other[0]
print("anqing硬件故障数量：",error_anqing_hardware)


#分类故障数量
#liantai
#Raid
#Raid卡
sql_error_liantai_Raid_Raidsas = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = 'Raid卡'"
#硬盘故障
sql_error_liantai_Raid_Disk = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '硬盘故障'"

#IPMI
#电源报错
sql_error_liantai_Ipmi_PsError = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '电源报错'"
#电源松动
sql_error_liantai_Ipmi_PsLoose = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '电源松动'"
#风扇故障
sql_error_liantai_Ipmi_FanError = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '风扇故障'"
#风扇降速
sql_error_liantai_Ipmi_FanLow = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '风扇降速'"
#PCIE中断
sql_error_liantai_Ipmi_PCIE = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = 'PCIE中断'"
#温度
sql_error_liantai_Ipmi_Temp = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '温度'"
#机箱入侵
sql_error_liantai_Ipmi_Chassis = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '机箱入侵'"

#GPU
#GPU掉卡
sql_error_liantai_GPU_GpuLost = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = 'GPU掉卡'"
#GPUError
sql_error_liantai_GPU_GpuError = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = 'GPUError'"
#烤机失败
sql_error_liantai_GPU_GpuBurn = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '烤机失败'"

#Dmesg
#内存报错
sql_error_liantai_Dmesg_Mem = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '内存报错'"
#OOM    #非硬件故障
sql_error_liantai_Dmesg_Oom = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = 'OOM'"

#IB故障
#网线故障
sql_error_liantai_IB_Cable = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '网线故障'"
#IB卡故障
sql_error_liantai_IB_Card = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = 'IB卡故障'"

#ICMP
#宕机
sql_error_liantai_ICMP_Dump = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = '宕机'"
#路由 #非硬件故障
sql_error_liantai_ICMP_Route = "select count(*) from (select * from (select * from maintain where Brand like '%联泰%') where ErrorClass = '路由') where RepairChange = 'Y'"
#测试维修   #非硬件故障
sql_error_liantai_ICMP_TestMain = "select count(*) from (select * from (select * from maintain where Brand like '%联泰%') where ErrorClass = '测试维修') where RepairChange = 'Y'"

#通用
#配置变更     #非硬件故障
sql_error_liantai_Cfgchange = "select count(*) from (select * from (select * from maintain where Brand like '%联泰%') where ErrorClass = '配置变更') where RepairChange = 'Y'"
#驱动   #非硬件故障
sql_error_liantai_Drive = "select count(*) from (select * from (select * from maintain where Brand like '%联泰%') where ErrorClass = '驱动') where RepairChange = 'Y'"
#Other
sql_error_liantai_Other = "select count(*) from (select * from maintain where Brand like '%联泰%') where ErrorClass = 'Other'"

#liantai分类故障数量
#liantai故障数量Raid卡
cursor.execute(sql_error_liantai_Raid_Raidsas)
error_liantai_Raid_Raidsas = cursor.fetchone()
print("liantai故障数量Raid卡：",error_liantai_Raid_Raidsas[0])
#liantai故障数量硬盘故障
cursor.execute(sql_error_liantai_Raid_Disk)
error_liantai_Raid_Disk = cursor.fetchone()
print("liantai故障数量硬盘故障：",error_liantai_Raid_Disk[0])
#liantai故障数量电源报错
cursor.execute(sql_error_liantai_Ipmi_PsError)
error_liantai_Ipmi_PsError = cursor.fetchone()
print("liantai故障数量电源报错：",error_liantai_Ipmi_PsError[0])
#liantai故障数量电源松动
cursor.execute(sql_error_liantai_Ipmi_PsLoose)
error_liantai_Ipmi_PsLoose = cursor.fetchone()
print("liantai故障数量电源松动：",error_liantai_Ipmi_PsLoose[0])
#liantai故障数量风扇故障
cursor.execute(sql_error_liantai_Ipmi_FanError)
error_liantai_Ipmi_FanError = cursor.fetchone()
print("liantai故障数量风扇故障：",error_liantai_Ipmi_FanError[0])
#liantai故障数量风扇降速
cursor.execute(sql_error_liantai_Ipmi_FanLow)
error_liantai_Ipmi_FanLow = cursor.fetchone()
print("liantai故障数量风扇降速：",error_liantai_Ipmi_FanLow[0])
#liantai故障数量PCIE中断
cursor.execute(sql_error_liantai_Ipmi_PCIE)
error_liantai_Ipmi_PCIE = cursor.fetchone()
print("liantai故障数量PCIE中断：",error_liantai_Ipmi_PCIE[0])
#liantai故障数量温度
cursor.execute(sql_error_liantai_Ipmi_Temp)
error_liantai_Ipmi_Temp = cursor.fetchone()
print("liantai故障数量温度：",error_liantai_Ipmi_Temp[0])
#liantai故障数量机箱入侵
cursor.execute(sql_error_liantai_Ipmi_Chassis)
error_liantai_Ipmi_Chassis = cursor.fetchone()
print("liantai故障数量机箱入侵：",error_liantai_Ipmi_Chassis[0])
#liantai故障数量GPU掉卡
cursor.execute(sql_error_liantai_GPU_GpuLost)
error_liantai_GPU_GpuLost = cursor.fetchone()
print("liantai故障数量GPU掉卡：",error_liantai_GPU_GpuLost[0])
#liantai故障数量GPUError
cursor.execute(sql_error_liantai_GPU_GpuError)
error_liantai_GPU_GpuError = cursor.fetchone()
print("liantai故障数量GPUError：",error_liantai_GPU_GpuError[0])
#liantai故障数量烤机失败
cursor.execute(sql_error_liantai_GPU_GpuBurn)
error_liantai_GPU_GpuBurn = cursor.fetchone()
print("liantai故障数量烤机失败：",error_liantai_GPU_GpuBurn[0])
#liantai故障数量内存报错
cursor.execute(sql_error_liantai_Dmesg_Mem)
error_liantai_Dmesg_Mem = cursor.fetchone()
print("liantai故障数量内存报错：",error_liantai_Dmesg_Mem[0])
#liantai故障数量网线故障
cursor.execute(sql_error_liantai_IB_Cable)
error_liantai_IB_Cable = cursor.fetchone()
print("liantai故障数量网线故障：",error_liantai_IB_Cable[0])
#liantai故障数量IB卡故障
cursor.execute(sql_error_liantai_IB_Card)
error_liantai_IB_Card = cursor.fetchone()
print("liantai故障数量IB卡故障：",error_liantai_IB_Card[0])
#liantai故障数量宕机
cursor.execute(sql_error_liantai_ICMP_Dump)
error_liantai_ICMP_Dump = cursor.fetchone()
print("liantai故障数量宕机：",error_liantai_ICMP_Dump[0])

#liantai故障数量_Other
cursor.execute(sql_error_liantai_Other)
error_liantai_Other = cursor.fetchone()
print("liantai故障数量_Other：",error_liantai_Other[0])
#liantai 故障数量_Raid
error_liantai_Raid = error_liantai_Raid_Disk[0] + error_liantai_Raid_Raidsas[0]
print("liantai故障数量_Raid：",error_liantai_Raid)
#liantai 故障数量_IPMI
error_liantai_Ipmi = error_liantai_Ipmi_PsError[0] + error_liantai_Ipmi_PsLoose[0] + error_liantai_Ipmi_FanError[0] + error_liantai_Ipmi_FanLow[0] + error_liantai_Ipmi_PCIE[0] + error_liantai_Ipmi_Temp[0] + error_liantai_Ipmi_Chassis[0]
print("liantai故障数量_IPMI：",error_liantai_Ipmi)
#liantai 故障数量_GPU
error_liantai_GPU = error_liantai_GPU_GpuLost[0] + error_liantai_GPU_GpuError[0] + error_liantai_GPU_GpuBurn[0]
print("liantai故障数量_GPU：",error_liantai_GPU)
#liantai 故障数量_Dmesg
error_liantai_Dmesg = error_liantai_Dmesg_Mem[0]
print("liantai故障数量_Dmesg：",error_liantai_Dmesg)
#liantai 故障数量_IB
error_liantai_IB = error_liantai_IB_Cable[0] + error_liantai_IB_Card[0]
print("liantai故障数量_IB：",error_liantai_IB)
#liantai 故障数量_宕机
error_liantai_Dump = error_liantai_ICMP_Dump[0]
print("liantai故障数量_宕机：",error_liantai_Dump)
#liantai 硬件故障数量
error_liantai_hardware = error_liantai_Raid + error_liantai_Ipmi + error_liantai_GPU + error_liantai_Dmesg + error_liantai_IB + error_liantai_Dump + error_liantai_Other[0]
print("liantai硬件故障数量：",error_liantai_hardware)


#分类故障数量
#shuguang
#Raid
#Raid卡
sql_error_shuguang_Raid_Raidsas = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = 'Raid卡'"
#硬盘故障
sql_error_shuguang_Raid_Disk = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '硬盘故障'"

#IPMI
#电源报错
sql_error_shuguang_Ipmi_PsError = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '电源报错'"
#电源松动
sql_error_shuguang_Ipmi_PsLoose = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '电源松动'"
#风扇故障
sql_error_shuguang_Ipmi_FanError = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '风扇故障'"
#风扇降速
sql_error_shuguang_Ipmi_FanLow = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '风扇降速'"
#PCIE中断
sql_error_shuguang_Ipmi_PCIE = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = 'PCIE中断'"
#温度
sql_error_shuguang_Ipmi_Temp = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '温度'"
#机箱入侵
sql_error_shuguang_Ipmi_Chassis = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '机箱入侵'"

#GPU
#GPU掉卡
sql_error_shuguang_GPU_GpuLost = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = 'GPU掉卡'"
#GPUError
sql_error_shuguang_GPU_GpuError = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = 'GPUError'"
#烤机失败
sql_error_shuguang_GPU_GpuBurn = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '烤机失败'"

#Dmesg
#内存报错
sql_error_shuguang_Dmesg_Mem = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '内存报错'"
#OOM    #非硬件故障
sql_error_shuguang_Dmesg_Oom = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = 'OOM'"

#IB故障
#网线故障
sql_error_shuguang_IB_Cable = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '网线故障'"
#IB卡故障
sql_error_shuguang_IB_Card = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = 'IB卡故障'"

#ICMP
#宕机
sql_error_shuguang_ICMP_Dump = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = '宕机'"
#路由 #非硬件故障
sql_error_shuguang_ICMP_Route = "select count(*) from (select * from (select * from maintain where Brand = '曙光') where ErrorClass = '路由') where RepairChange = 'Y'"
#测试维修   #非硬件故障
sql_error_shuguang_ICMP_TestMain = "select count(*) from (select * from (select * from maintain where Brand = '曙光') where ErrorClass = '测试维修') where RepairChange = 'Y'"

#通用
#配置变更     #非硬件故障
sql_error_shuguang_Cfgchange = "select count(*) from (select * from (select * from maintain where Brand = '曙光') where ErrorClass = '配置变更') where RepairChange = 'Y'"
#驱动   #非硬件故障
sql_error_shuguang_Drive = "select count(*) from (select * from (select * from maintain where Brand = '曙光') where ErrorClass = '驱动') where RepairChange = 'Y'"
#Other
sql_error_shuguang_Other = "select count(*) from (select * from maintain where Brand = '曙光') where ErrorClass = 'Other'"

#shuguang分类故障数量
#shuguang故障数量Raid卡
cursor.execute(sql_error_shuguang_Raid_Raidsas)
error_shuguang_Raid_Raidsas = cursor.fetchone()
print("shuguang故障数量Raid卡：",error_shuguang_Raid_Raidsas[0])
#shuguang故障数量硬盘故障
cursor.execute(sql_error_shuguang_Raid_Disk)
error_shuguang_Raid_Disk = cursor.fetchone()
print("shuguang故障数量硬盘故障：",error_shuguang_Raid_Disk[0])
#shuguang故障数量电源报错
cursor.execute(sql_error_shuguang_Ipmi_PsError)
error_shuguang_Ipmi_PsError = cursor.fetchone()
print("shuguang故障数量电源报错：",error_shuguang_Ipmi_PsError[0])
#shuguang故障数量电源松动
cursor.execute(sql_error_shuguang_Ipmi_PsLoose)
error_shuguang_Ipmi_PsLoose = cursor.fetchone()
print("shuguang故障数量电源松动：",error_shuguang_Ipmi_PsLoose[0])
#shuguang故障数量风扇故障
cursor.execute(sql_error_shuguang_Ipmi_FanError)
error_shuguang_Ipmi_FanError = cursor.fetchone()
print("shuguang故障数量风扇故障：",error_shuguang_Ipmi_FanError[0])
#shuguang故障数量风扇降速
cursor.execute(sql_error_shuguang_Ipmi_FanLow)
error_shuguang_Ipmi_FanLow = cursor.fetchone()
print("shuguang故障数量风扇降速：",error_shuguang_Ipmi_FanLow[0])
#shuguang故障数量PCIE中断
cursor.execute(sql_error_shuguang_Ipmi_PCIE)
error_shuguang_Ipmi_PCIE = cursor.fetchone()
print("shuguang故障数量PCIE中断：",error_shuguang_Ipmi_PCIE[0])
#shuguang故障数量温度
cursor.execute(sql_error_shuguang_Ipmi_Temp)
error_shuguang_Ipmi_Temp = cursor.fetchone()
print("shuguang故障数量温度：",error_shuguang_Ipmi_Temp[0])
#shuguang故障数量机箱入侵
cursor.execute(sql_error_shuguang_Ipmi_Chassis)
error_shuguang_Ipmi_Chassis = cursor.fetchone()
print("shuguang故障数量机箱入侵：",error_shuguang_Ipmi_Chassis[0])
#shuguang故障数量GPU掉卡
cursor.execute(sql_error_shuguang_GPU_GpuLost)
error_shuguang_GPU_GpuLost = cursor.fetchone()
print("shuguang故障数量GPU掉卡：",error_shuguang_GPU_GpuLost[0])
#shuguang故障数量GPUError
cursor.execute(sql_error_shuguang_GPU_GpuError)
error_shuguang_GPU_GpuError = cursor.fetchone()
print("shuguang故障数量GPUError：",error_shuguang_GPU_GpuError[0])
#shuguang故障数量烤机失败
cursor.execute(sql_error_shuguang_GPU_GpuBurn)
error_shuguang_GPU_GpuBurn = cursor.fetchone()
print("shuguang故障数量烤机失败：",error_shuguang_GPU_GpuBurn[0])
#shuguang故障数量内存报错
cursor.execute(sql_error_shuguang_Dmesg_Mem)
error_shuguang_Dmesg_Mem = cursor.fetchone()
print("shuguang故障数量内存报错：",error_shuguang_Dmesg_Mem[0])
#shuguang故障数量网线故障
cursor.execute(sql_error_shuguang_IB_Cable)
error_shuguang_IB_Cable = cursor.fetchone()
print("shuguang故障数量网线故障：",error_shuguang_IB_Cable[0])
#shuguang故障数量IB卡故障
cursor.execute(sql_error_shuguang_IB_Card)
error_shuguang_IB_Card = cursor.fetchone()
print("shuguang故障数量IB卡故障：",error_shuguang_IB_Card[0])
#shuguang故障数量宕机
cursor.execute(sql_error_shuguang_ICMP_Dump)
error_shuguang_ICMP_Dump = cursor.fetchone()
print("shuguang故障数量宕机：",error_shuguang_ICMP_Dump[0])

#shuguang故障数量_Other
cursor.execute(sql_error_shuguang_Other)
error_shuguang_Other = cursor.fetchone()
print("shuguang故障数量_Other：",error_shuguang_Other[0])
#shuguang 故障数量_Raid
error_shuguang_Raid = error_shuguang_Raid_Disk[0] + error_shuguang_Raid_Raidsas[0]
print("shuguang故障数量_Raid：",error_shuguang_Raid)
#shuguang 故障数量_IPMI
error_shuguang_Ipmi = error_shuguang_Ipmi_PsError[0] + error_shuguang_Ipmi_PsLoose[0] + error_shuguang_Ipmi_FanError[0] + error_shuguang_Ipmi_FanLow[0] + error_shuguang_Ipmi_PCIE[0] + error_shuguang_Ipmi_Temp[0] + error_shuguang_Ipmi_Chassis[0]
print("shuguang故障数量_IPMI：",error_shuguang_Ipmi)
#shuguang 故障数量_GPU
error_shuguang_GPU = error_shuguang_GPU_GpuLost[0] + error_shuguang_GPU_GpuError[0] + error_shuguang_GPU_GpuBurn[0]
print("shuguang故障数量_GPU：",error_shuguang_GPU)
#shuguang 故障数量_Dmesg
error_shuguang_Dmesg = error_shuguang_Dmesg_Mem[0]
print("shuguang故障数量_Dmesg：",error_shuguang_Dmesg)
#shuguang 故障数量_IB
error_shuguang_IB = error_shuguang_IB_Cable[0] + error_shuguang_IB_Card[0]
print("shuguang故障数量_IB：",error_shuguang_IB)
#shuguang 故障数量_宕机
error_shuguang_Dump = error_shuguang_ICMP_Dump[0]
print("shuguang故障数量_宕机：",error_shuguang_Dump)
#shuguang 硬件故障数量
error_shuguang_hardware = error_shuguang_Raid + error_shuguang_Ipmi + error_shuguang_GPU + error_shuguang_Dmesg + error_shuguang_IB + error_shuguang_Dump + error_shuguang_Other[0]
print("shuguang硬件故障数量：",error_shuguang_hardware)


#分类故障数量
#langchao
#Raid
#Raid卡
sql_error_langchao_Raid_Raidsas = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = 'Raid卡'"
#硬盘故障
sql_error_langchao_Raid_Disk = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '硬盘故障'"

#IPMI
#电源报错
sql_error_langchao_Ipmi_PsError = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '电源报错'"
#电源松动
sql_error_langchao_Ipmi_PsLoose = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '电源松动'"
#风扇故障
sql_error_langchao_Ipmi_FanError = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '风扇故障'"
#风扇降速
sql_error_langchao_Ipmi_FanLow = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '风扇降速'"
#PCIE中断
sql_error_langchao_Ipmi_PCIE = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = 'PCIE中断'"
#温度
sql_error_langchao_Ipmi_Temp = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '温度'"
#机箱入侵
sql_error_langchao_Ipmi_Chassis = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '机箱入侵'"

#GPU
#GPU掉卡
sql_error_langchao_GPU_GpuLost = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = 'GPU掉卡'"
#GPUError
sql_error_langchao_GPU_GpuError = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = 'GPUError'"
#烤机失败
sql_error_langchao_GPU_GpuBurn = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '烤机失败'"

#Dmesg
#内存报错
sql_error_langchao_Dmesg_Mem = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '内存报错'"
#OOM    #非硬件故障
sql_error_langchao_Dmesg_Oom = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = 'OOM'"

#IB故障
#网线故障
sql_error_langchao_IB_Cable = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '网线故障'"
#IB卡故障
sql_error_langchao_IB_Card = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = 'IB卡故障'"

#ICMP
#宕机
sql_error_langchao_ICMP_Dump = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '宕机'"
#路由 #非硬件故障
sql_error_langchao_ICMP_Route = "select count(*) from (select * from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '路由') where RepairChange = 'Y'"
#测试维修   #非硬件故障
sql_error_langchao_ICMP_TestMain = "select count(*) from (select * from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '测试维修') where RepairChange = 'Y'"

#通用
#配置变更     #非硬件故障
sql_error_langchao_Cfgchange = "select count(*) from (select * from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '配置变更') where RepairChange = 'Y'"
#驱动   #非硬件故障
sql_error_langchao_Drive = "select count(*) from (select * from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = '驱动') where RepairChange = 'Y'"
#Other
sql_error_langchao_Other = "select count(*) from (select * from maintain where Brand like '%浪潮%' or Brand like '%阿里巴巴%') where ErrorClass = 'Other'"

#langchao分类故障数量
#langchao故障数量Raid卡
cursor.execute(sql_error_langchao_Raid_Raidsas)
error_langchao_Raid_Raidsas = cursor.fetchone()
print("langchao故障数量Raid卡：",error_langchao_Raid_Raidsas[0])
#langchao故障数量硬盘故障
cursor.execute(sql_error_langchao_Raid_Disk)
error_langchao_Raid_Disk = cursor.fetchone()
print("langchao故障数量硬盘故障：",error_langchao_Raid_Disk[0])
#langchao故障数量电源报错
cursor.execute(sql_error_langchao_Ipmi_PsError)
error_langchao_Ipmi_PsError = cursor.fetchone()
print("langchao故障数量电源报错：",error_langchao_Ipmi_PsError[0])
#langchao故障数量电源松动
cursor.execute(sql_error_langchao_Ipmi_PsLoose)
error_langchao_Ipmi_PsLoose = cursor.fetchone()
print("langchao故障数量电源松动：",error_langchao_Ipmi_PsLoose[0])
#langchao故障数量风扇故障
cursor.execute(sql_error_langchao_Ipmi_FanError)
error_langchao_Ipmi_FanError = cursor.fetchone()
print("langchao故障数量风扇故障：",error_langchao_Ipmi_FanError[0])
#langchao故障数量风扇降速
cursor.execute(sql_error_langchao_Ipmi_FanLow)
error_langchao_Ipmi_FanLow = cursor.fetchone()
print("langchao故障数量风扇降速：",error_langchao_Ipmi_FanLow[0])
#langchao故障数量PCIE中断
cursor.execute(sql_error_langchao_Ipmi_PCIE)
error_langchao_Ipmi_PCIE = cursor.fetchone()
print("langchao故障数量PCIE中断：",error_langchao_Ipmi_PCIE[0])
#langchao故障数量温度
cursor.execute(sql_error_langchao_Ipmi_Temp)
error_langchao_Ipmi_Temp = cursor.fetchone()
print("langchao故障数量温度：",error_langchao_Ipmi_Temp[0])
#langchao故障数量机箱入侵
cursor.execute(sql_error_langchao_Ipmi_Chassis)
error_langchao_Ipmi_Chassis = cursor.fetchone()
print("langchao故障数量机箱入侵：",error_langchao_Ipmi_Chassis[0])
#langchao故障数量GPU掉卡
cursor.execute(sql_error_langchao_GPU_GpuLost)
error_langchao_GPU_GpuLost = cursor.fetchone()
print("langchao故障数量GPU掉卡：",error_langchao_GPU_GpuLost[0])
#langchao故障数量GPUError
cursor.execute(sql_error_langchao_GPU_GpuError)
error_langchao_GPU_GpuError = cursor.fetchone()
print("langchao故障数量GPUError：",error_langchao_GPU_GpuError[0])
#langchao故障数量烤机失败
cursor.execute(sql_error_langchao_GPU_GpuBurn)
error_langchao_GPU_GpuBurn = cursor.fetchone()
print("langchao故障数量烤机失败：",error_langchao_GPU_GpuBurn[0])
#langchao故障数量内存报错
cursor.execute(sql_error_langchao_Dmesg_Mem)
error_langchao_Dmesg_Mem = cursor.fetchone()
print("langchao故障数量内存报错：",error_langchao_Dmesg_Mem[0])
#langchao故障数量网线故障
cursor.execute(sql_error_langchao_IB_Cable)
error_langchao_IB_Cable = cursor.fetchone()
print("langchao故障数量网线故障：",error_langchao_IB_Cable[0])
#langchao故障数量IB卡故障
cursor.execute(sql_error_langchao_IB_Card)
error_langchao_IB_Card = cursor.fetchone()
print("langchao故障数量IB卡故障：",error_langchao_IB_Card[0])
#langchao故障数量宕机
cursor.execute(sql_error_langchao_ICMP_Dump)
error_langchao_ICMP_Dump = cursor.fetchone()
print("langchao故障数量宕机：",error_langchao_ICMP_Dump[0])

#langchao故障数量_Other
cursor.execute(sql_error_langchao_Other)
error_langchao_Other = cursor.fetchone()
print("langchao故障数量_Other：",error_langchao_Other[0])
#langchao 故障数量_Raid
error_langchao_Raid = error_langchao_Raid_Disk[0] + error_langchao_Raid_Raidsas[0]
print("langchao故障数量_Raid：",error_langchao_Raid)
#langchao 故障数量_IPMI
error_langchao_Ipmi = error_langchao_Ipmi_PsError[0] + error_langchao_Ipmi_PsLoose[0] + error_langchao_Ipmi_FanError[0] + error_langchao_Ipmi_FanLow[0] + error_langchao_Ipmi_PCIE[0] + error_langchao_Ipmi_Temp[0] + error_langchao_Ipmi_Chassis[0]
print("langchao故障数量_IPMI：",error_langchao_Ipmi)
#langchao 故障数量_GPU
error_langchao_GPU = error_langchao_GPU_GpuLost[0] + error_langchao_GPU_GpuError[0] + error_langchao_GPU_GpuBurn[0]
print("langchao故障数量_GPU：",error_langchao_GPU)
#langchao 故障数量_Dmesg
error_langchao_Dmesg = error_langchao_Dmesg_Mem[0]
print("langchao故障数量_Dmesg：",error_langchao_Dmesg)
#langchao 故障数量_IB
error_langchao_IB = error_langchao_IB_Cable[0] + error_langchao_IB_Card[0]
print("langchao故障数量_IB：",error_langchao_IB)
#langchao 故障数量_宕机
error_langchao_Dump = error_langchao_ICMP_Dump[0]
print("langchao故障数量_宕机：",error_langchao_Dump)
#langchao 硬件故障数量
error_langchao_hardware = error_langchao_Raid + error_langchao_Ipmi + error_langchao_GPU + error_langchao_Dmesg + error_langchao_IB + error_langchao_Dump + error_langchao_Other[0]
print("langchao硬件故障数量：",error_langchao_hardware)



cursor.close()
# conn.commit()
conn.close()






def print_pie_draw():
    """
    draw pie
    return:
    """
    #指定切片大小比例
    sclice = [number_dell[0],number_amax[0],number_anqing[0],number_liantai[0],number_shuguang[0],number_langchao[0]]
    #指定标签
    activite = ["dell","amax","Engine","Liantai","Sugon","Inspur"]
    #颜色
    color = ['b','m','r','g','y','c']

    plt.pie(sclice,labels=activite,
            colors=color,
            startangle=0,
            shadow=True,
            explode=(0.1,0.1,0.1,0.1,0.1,0.1),
            autopct='%1.2f%%')
    plt.title("activite analys")
    plt.savefig("2.png")
    plt.show()

# print_pie_draw()