# 主文件
# Queston.i.j
# < exam >
#     < courseCode >
#     < when >
#     < rubric >
#     < compositeq >
#             < questionText >
#             < compositeq >
#                 < questionText >
#                 < freeTextq >
#             < compositeq >
#                 < questionText >
#                 < freeTextq >
#             < graphq >

from bs4 import BeautifulSoup

import Text_Clear


def Open(filename):
    # 读取文件/Open file
    file = BeautifulSoup(open(filename, encoding="utf-8"), features="xml")
    '''
    # 获取文件总体属性/Get file's property
    exam_property = file.exam.attrs
    for key in exam_property:
        print(key + ":" + str(exam_property[key]))

    exam_CourseCode = file.exam.courseCode.contents[0]
    exam_CourseCode = Text_Clear.clear(exam_CourseCode)
    print("courseCode:" + exam_CourseCode)

    # 获取when/Get when
    exam_When = file.exam.when.contents[0]
    exam_When = Text_Clear.clear(exam_When)
    print("when" + exam_When)

    # 获取rubric
    exam_Rubric = file.exam.rubric.contents[0]
    exam_Rubric = Text_Clear.clear(exam_Rubric)
    print("rubric:" + exam_Rubric)

    # 获取compositeq(dict)属性
    compositeq_property = file.exam.compositeq.attrs
    for key in compositeq_property:
        print(key + ":" + str(compositeq_property[key]))
    '''

    Question_list = {}
    Questions = file.exam.compositeq.contents
    index1 = 1
    index2 = 1
    index3 = 0
    while str("\n") in Questions:
        Questions.remove(str("\n"))

    for Question in Questions:  # 一级题目-Index1
        while str("\n") in Question.contents:
            Question.contents.remove(str("\n"))

        if Question.name == "questionText":
            Question_list["Exam"] = Question.text
            continue

        for i in Question.contents:  # 二级题目-Index2
            if i.name == "questionText":
                Question_list["Question" + str(index1)] = i.text  # Question1

            if i.name == "freeTextq":
                while str("\n") in i.contents:
                    i.contents.remove(str("\n"))

                Question_list["Question" + str(index1) + "." +
                              str(index2)] = i.contents[0].text  # Question1.1
                index2 = index2 + 1

            if i.name == "compositeq":
                while str("\n") in i.contents:
                    i.contents.remove(str("\n"))

                for j in i.contents:  # 三级题目-Index3
                    if j.name == "questionText":
                        Question_list["Question" + str(index1) + "." +
                                      str(index2)] = j.text  # Question2.3

                    if j.name == "freeTextq":
                        while str("\n") in j.contents:
                            j.contents.remove(str("\n"))

                        Question_list[
                            "Question" + str(index1) + "." + str(index2) +
                            "." +
                            str(index3)] = j.contents[0].text  # Question2.3.1
                    index3 = index3 + 1
                index2 = index2 + 1

            if i.name == "graphq":
                Question_list[
                    "Question" + str(index1) + "." +
                    str(index2)] = "Need to use Oracle"  # Question1.1

                index2 = index2 + 1

            index3 = 0
        index1 = index1 + 1
        index2 = 1

    for element in Question_list:
        Question_list[element] = str(Text_Clear.clear(Question_list[element]))

    return Question_list
