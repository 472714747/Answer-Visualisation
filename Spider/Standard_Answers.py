# 主文件
# Queston.i.j

from bs4 import BeautifulSoup

import Text_Clear


def Open(filename):
    # 读取文件/Open file
    file = BeautifulSoup(open(filename, encoding="utf-8"), features="xml")
    '''
    # 获取文件总体属性/Get file's property
    answerPaper_property = file.answerPaper.attrs
    for key in answerPaper_property:
        print(key + ":" + str(answerPaper_property[key]))

    # 获取compositea(dict)属性
    compositea_property = file.answerPaper.compositea.attrs
    for key in compositea_property:
        print(key + ":" + str(compositea_property[key]))
    '''

    Standard_list = {}
    Standard_Answers = file.answerPaper.compositea.contents
    index1 = 1
    index2 = 1
    index3 = 1
    while str("\n") in Standard_Answers:
        Standard_Answers.remove(str("\n"))

    for Standard_Answer in Standard_Answers:  # 一级题目-Index1
        while str("\n") in Standard_Answer.contents:
            Standard_Answer.contents.remove(str("\n"))

        for i in Standard_Answer.contents:  # 二级题目-Index2

            if i.name == "freeTextAnswer":
                while str("\n") in i.contents:
                    i.contents.remove(str("\n"))

                Standard_list[
                    "Standard_Answer" + str(index1) + "." +
                    str(index2)] = i.contents[0].text  # Standard_Answer1.1

            if i.name == "compositea":
                while str("\n") in i.contents:
                    i.contents.remove(str("\n"))

                for j in i.contents:  # 三级题目-Index3
                    while str("\n") in j.contents:
                        j.contents.remove(str("\n"))

                    if j.name == "freeTextAnswer":
                        Standard_list["Standard_Answer" + str(index1) + "." +
                                      str(index2) + "." +
                                      str(index3)] = j.contents[
                                          0].text  # Standard_Answer2.3

                    index3 = index3 + 1

            index2 = index2 + 1
            index3 = 1
        index1 = index1 + 1
        index2 = 1

    for element in Standard_list:
        Standard_list[element] = str(Text_Clear.clear(Standard_list[element]))

    return Standard_list
