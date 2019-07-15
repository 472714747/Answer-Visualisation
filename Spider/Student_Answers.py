# 主文件
# Queston.i.j

from bs4 import BeautifulSoup
import Text_Clear


def Open(filename):
    # 读取文件/Open file
    file = BeautifulSoup(open(filename, encoding="utf-8"), features="xml")
    '''
    # 获取文件总体属性/Get file's property
    setOfAnswerPapers_property = file.setOfAnswerPapers.attrs
    for key in setOfAnswerPapers_property:
        print(key + ":" + str(setOfAnswerPapers_property[key]))

    # 获取comment/Get comment
    comment = file.setOfAnswerPapers.comment.text
    '''
    # 获取answerPaper(dict)属性
    index1 = 1
    index2 = 1
    index3 = 1
    Answer_List = {}

    for answerPaper in file.setOfAnswerPapers.contents:
        if answerPaper.name == "answerPaper":
            StudentID = answerPaper.attrs["studentId"]
            Paper = answerPaper.compositea

            while str("\n") in Paper.contents:
                Paper.contents.remove(str("\n"))

            for Answers in Paper:
                while str("\n") in Answers.contents:
                    Answers.contents.remove(str("\n"))

                for Sub_Answers in Answers.contents:
                    if Sub_Answers.name == "unanswered":
                        Answer_List["Student" + str(StudentID) + "." +
                                    str(index1) + "." +
                                    str(index2)] = "unanswered"
                        index2 = index2 + 1

                    if Sub_Answers.name == "compositea":
                        while str("\n") in Sub_Answers.contents:
                            Sub_Answers.contents.remove(str("\n"))

                        for i in Sub_Answers.contents:
                            while str("\n") in i.contents:
                                i.contents.remove(str("\n"))

                            if i.name == "unanswered":
                                Answer_List["Student" + str(StudentID) + "." +
                                            str(index1) + "." + str(index2) +
                                            "." + str(index3)] = "unanswered"
                                index3 = index3 + 1

                            if i.name == "freeTextAnswer":
                                Answer_List["Student" + str(StudentID) + "." +
                                            str(index1) + "." + str(index2) +
                                            "." +
                                            str(index3)] = i.contents[0].text
                                index3 = index3 + 1
                        index2 = index2 + 1

                    if Sub_Answers.name == "freeTextAnswer":
                        while str("\n") in Sub_Answers.contents:
                            Sub_Answers.contents.remove(str("\n"))

                        Answer_List["Student" + str(StudentID) + "." +
                                    str(index1) + "." +
                                    str(index2)] = Sub_Answers.contents[0].text
                        index2 = index2 + 1

                    index3 = 1
                index2 = 1
                index1 = index1 + 1
            index1 = 1

    for element in Answer_List:
        Answer_List[element] = str(Text_Clear.clear(Answer_List[element]))

    return Answer_List
    '''
    # 导出到csv/output to .csv
    xixi = []
    for element11 in Answer_List:
        xixi.append([element11, Answer_List[element11]])

    shuju = ["Index", "Content"]
    Student_Answers = pd.DataFrame(columns=shuju, data=xixi)
    Student_Answers.to_csv('Spider/Student_Answers.csv', encoding='utf-8')
    '''
