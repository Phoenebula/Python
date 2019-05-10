#-*-coding:utf-8-*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import analysis


plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

#所有故障数量
def error_all_pie_draw():
    """
    draw pie
    return:
    """
    #指定切片大小比例
    sclice = [analysis.error_dell_hardware,analysis.error_amax_hardware,analysis.error_anqing_hardware,analysis.error_liantai_hardware,analysis.error_shuguang_hardware,analysis.error_langchao_hardware]
    #指定标签
    activite = ["dell","amax","安擎","联泰","曙光","浪潮"]
    #颜色
    color = ['b','m','r','g','y','c']

    plt.pie(sclice,labels=activite,
            colors=color,
            startangle=0,
            shadow=True,
            explode=(0.1,0.1,0.1,0.1,0.1,0.1),
            autopct='%1.2f%%')
    plt.title("硬件故障数量")
    plt.savefig("硬件故障数量.png")
    plt.show()

error_all_pie_draw()

#硬件维修故障数量
def maintain_all_pie_draw():
    """
    draw pie
    return:
    """
    #指定切片大小比例
    sclice = [analysis.maintain_dell[0],analysis.maintain_amax[0],analysis.maintain_anqing[0],analysis.maintain_liantai[0],analysis.maintain_shuguang[0],analysis.maintain_langchao[0]]
    #指定标签
    activite = ["dell","amax","安擎","联泰","曙光","浪潮"]
    #颜色
    color = ['b','m','r','g','y','c']

    plt.pie(sclice,labels=activite,
            colors=color,
            startangle=0,
            shadow=True,
            explode=(0.1,0.1,0.1,0.1,0.1,0.1),
            autopct='%1.2f%%')
    plt.title("硬件维修故障数量")
    plt.savefig("硬件维修故障数量.png")
    plt.show()

maintain_all_pie_draw()


def print_hist_draw():
    """
    画直方图
    """
    error_list = ['Raid', 'IPMI', 'GPU', 'Dmesg', 'IB', 'Dump', 'Other']
    num_list = [analysis.error_dell_Raid, analysis.error_dell_Ipmi, analysis.error_dell_GPU,analysis.error_dell_Dmesg, analysis.error_dell_IB, analysis.error_dell_Dump,analysis.error_dell_Other[0]]
    rects = plt.bar(range(len(num_list)), num_list, color='bmrgyck')
    # X轴标题
    index = [0, 1, 2, 3, 4, 5, 6]
    index = [float(c) + 0.4 for c in index]
    plt.ylim(top=10, bottom=0)
    plt.xticks(index, error_list)
    plt.ylabel("数量")  # X轴标签
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha='center', va='bottom')
    plt.title("故障明细")
    plt.savefig("故障明细.png")
    plt.show()

# print_hist_draw()

#对比图
def errolist_hist_draw():
    """
    画对比直方图
    """

    name_list = ('Dell','AMAX','安擎','联泰','曙光', '浪潮')  # 姓名
    error_list = ['Raid', 'IPMI', 'GPU', 'Dmesg', 'IB', 'Dump', 'Other']         #对应subjects
    num_list = ((analysis.error_dell_Raid, analysis.error_dell_Ipmi, analysis.error_dell_GPU, analysis.error_dell_Dmesg,analysis.error_dell_IB, analysis.error_dell_Dump, analysis.error_dell_Other[0]),(analysis.error_amax_Raid, analysis.error_amax_Ipmi, analysis.error_amax_GPU, analysis.error_amax_Dmesg,analysis.error_amax_IB, analysis.error_amax_Dump, analysis.error_amax_Other[0]),(analysis.error_anqing_Raid, analysis.error_anqing_Ipmi, analysis.error_anqing_GPU, analysis.error_anqing_Dmesg,analysis.error_anqing_IB, analysis.error_anqing_Dump, analysis.error_anqing_Other[0]),(analysis.error_liantai_Raid, analysis.error_liantai_Ipmi, analysis.error_liantai_GPU, analysis.error_liantai_Dmesg,analysis.error_liantai_IB, analysis.error_liantai_Dump, analysis.error_liantai_Other[0]),(analysis.error_shuguang_Raid, analysis.error_shuguang_Ipmi, analysis.error_shuguang_GPU, analysis.error_shuguang_Dmesg,analysis.error_shuguang_IB, analysis.error_shuguang_Dump, analysis.error_shuguang_Other[0]),(analysis.error_langchao_Raid, analysis.error_langchao_Ipmi, analysis.error_langchao_GPU, analysis.error_langchao_Dmesg,analysis.error_langchao_IB, analysis.error_langchao_Dump, analysis.error_langchao_Other[0]))        #对应scores


    # num_list = ((1, 2, 7),(3, 4, 8),(5, 6, 9))
    bar_width = 0.12
    index = np.arange(len(num_list[0]))
    rects_dell = plt.bar(index, num_list[0], bar_width, color='b', label=name_list[0])
    rects_amax = plt.bar(index + bar_width, num_list[1], bar_width, color='m', label=name_list[1])
    rects_anqing = plt.bar(index + bar_width*2, num_list[2], bar_width, color='r', label=name_list[2])
    rects_liantai = plt.bar(index + bar_width*3, num_list[3], bar_width, color='g', label=name_list[3])
    rects_shuguang = plt.bar(index + bar_width*4, num_list[4], bar_width, color='y', label=name_list[4])
    rects_langchao = plt.bar(index + bar_width*5, num_list[5], bar_width, color='c', label=name_list[5])
    # X轴标题
    plt.xticks(index + bar_width, error_list)
    # Y轴范围
    plt.ylim(top=20, bottom=0)
    #图例
    plt.legend(loc='best')
    # 添加数据标签
    def add_labels(rects):
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2, height, height, ha='center', va='bottom')
            # 柱形图边缘用白色填充，纯粹为了美观
            rect.set_edgecolor('white')

    add_labels(rects_dell)
    add_labels(rects_amax)
    add_labels(rects_anqing)
    add_labels(rects_liantai)
    add_labels(rects_shuguang)
    add_labels(rects_langchao)

    plt.title("故障明细对比")
    plt.savefig('故障明细对比.png')
    plt.show()

errolist_hist_draw()