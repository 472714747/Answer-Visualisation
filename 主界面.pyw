import sys
import re
import pandas

from PyQt5 import QtGui
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QFileDialog, QTabWidget, QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QTableWidget, QFrame, QTableWidgetItem

sys.path.append(
    r'L:\OneDrive - UOM\University of Manchester\PGT\Project\Tool\Spider')
sys.path.append(
    r'L:\OneDrive - UOM\University of Manchester\PGT\Project\Tool\UI')
sys.path.append(
    r'C:\Users\ang\OneDrive - UOM\University of Manchester\PGT\Project\Tool\Spider'
)

import Questions
import Standard_Answers
import Student_Answers
import Word_Count

qtCreatorFile = "UI/mainwindow.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

Question_list = {}
Standard_list = {}
Answer_list = {}
filetype = ""
Status = ""
Student_number = ""
listWidget_Text = ""
Count = {}


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.menuView.setEnabled(False)
        self.tabWidget.setTabEnabled(2, False)

        self.actionOpen.triggered.connect(self.Openfile)
        self.actionSave.triggered.connect(self.Save)
        self.actionExit.triggered.connect(self.Exit)
        self.actionStudent.triggered.connect(self.Student_View)
        self.actionQuestion.triggered.connect(self.Question_View)
        self.listWidget.itemClicked.connect(self.listWidget_Clicked)
        self.listWidget_2.itemClicked.connect(self.listWidget_2_Clicked)
        self.pushButton.clicked.connect(self.detail)
        self.animation = None
        self.tabWidget.setTabEnabled(1, False)

        # 搜索栏加图标
        myAction = QtWidgets.QAction(self.lineEdit)
        myAction.setIcon(QtGui.QIcon("./UI/Icons/search.png"))
        self.lineEdit.addAction(myAction, QtWidgets.QLineEdit.TrailingPosition)

        # 添加阴影
        # effect = QGraphicsDropShadowEffect(self)
        # effect.setBlurRadius(12)
        # effect.setOffset(0, 0)
        # effect.setColor(Qt.gray)
        # self.widget.setGraphicsEffect(effect)

    def Openfile(self):  # 打开文件
        self.listWidget.clear()
        global filetype
        filename, filetype = QFileDialog.getOpenFileName(
            self, "Open File", "./",
            "Questions File (*.exam);;Standard Answers File (*.stan);;Student Answers File (*.aset)"
        )

        if filename != "":  # 成功选择文件
            global Question_list

            if filetype == "Questions File (*.exam)":  # 考试试题
                self.textEdit_Up.clear()
                self.textEdit_Down.clear()
                self.tabWidget.setTabEnabled(1, False)
                self.tabWidget.setTabText(0, "Question")

                Question_list = Questions.Open(filename)

                for i in Question_list:
                    self.listWidget.addItem(str(i))

            if filetype == "Standard Answers File (*.stan)":  # 标准答案
                self.textEdit_Up.clear()
                self.textEdit_Down.clear()
                self.tabWidget.setTabEnabled(1, False)
                self.tabWidget.setTabText(0, "Standard_Answers")
                global Standard_list
                Question_list = Questions.Open(filename.replace(
                    "stan", "exam"))
                Standard_list = Standard_Answers.Open(filename)

                for i in Standard_list:
                    self.listWidget.addItem(str(i))

            if filetype == "Student Answers File (*.aset)":  # 考生答案
                self.textEdit_Up.clear()
                self.textEdit_Down.clear()
                self.menuView.setEnabled(True)  # 开启View
                self.tabWidget.setTabEnabled(0, True)
                self.tabWidget.setTabEnabled(1, False)
                self.tabWidget.setTabText(0, "Student_Answers")
                global Status, Answer_list
                Status = "None"
                Question_list = Questions.Open(filename.replace(
                    "aset", "exam"))
                Answer_list = Student_Answers.Open(filename)

                for i in Answer_list:
                    self.listWidget.addItem(str(i))

    def Save(self):
        fname, filetype = QFileDialog.getSaveFileName(
            self, "Save File", "./", "CSV (*.csv)")  # 写入文件首先获取文件路径
        if fname[0]:  # 如果获取的路径非空
            f = open(fname[0], "w")  # 以写入的方式打开文件
            pandas.DataFrame.from_dict(Count,
                                       orient='index').T.to_csv(fname,
                                                                index=False)
        f.close()

    def Student_View(self):  # 点击View-Student
        self.listWidget.clear()
        self.tabWidget.setTabEnabled(0, False)
        self.tabWidget.setTabEnabled(1, True)
        self.tabWidget.setTabText(1, "Student_View")
        global Status
        Status = "Student"
        length = int(
            sorted(Answer_list.keys())[-1].split(".")[0].replace(
                "Student", ""))
        for i in range(1, length):
            self.listWidget.addItem("Student" + str(i))

    def Question_View(self):  # 点击View-Question
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.tabWidget.setTabEnabled(0, False)
        self.tabWidget.setTabEnabled(1, True)
        self.tabWidget.setTabText(1, "Question_View")
        global Status
        Status = "Question"
        for i in Question_list:
            if "Question" in i and "." in i:
                self.listWidget.addItem(i)

    def listWidget_Clicked(self, item):  # 在左面选择一项
        if filetype == "Questions File (*.exam)":
            self.textEdit_Up.setHtml(Question_list[item.text()])

        if filetype == "Standard Answers File (*.stan)":
            Text = item.text().replace("Standard_Answer", "Question")
            try:
                self.textEdit_Up.setHtml(Question_list[Text[:-2]] +
                                         "<br><br>" + Question_list[Text])
            except:
                self.textEdit_Up.setHtml(Question_list[Text])

            self.textEdit_Down.setHtml(Standard_list[item.text()])

        if filetype == "Student Answers File (*.aset)":
            global Student_number
            Student_number = item.text()

            if Status == "None":  # 在普通视图下
                Text = item.text()
                Text_Split = item.text().split(".")
                Text_Change = str(Text_Split[0]) + "."
                Text = Text.replace(Text_Change, "Question")
                try:
                    self.textEdit_Up.setHtml(Question_list[Text[:-2]] +
                                             "<br><br>" + Question_list[Text])
                except:
                    self.textEdit_Up.setHtml(Question_list[Text])

                self.textEdit_Down.setHtml(Answer_list[item.text()])

            if Status == "Student":  # 在View-Student视图下
                self.listWidget_2.clear()

                for i in Answer_list:
                    if item.text() + "." in i:
                        i = i.replace(item.text() + ".", "Question")
                        self.listWidget_2.addItem(i)

            if Status == "Question":  # 在View-Question视图下
                self.listWidget_2.clear()
                global listWidget_Text
                listWidget_Text = item.text()
                length = int(
                    sorted(Answer_list.keys())[-1].split(".")[0].replace(
                        "Student", ""))  # Student94.4.1.2
                for i in range(1, length):
                    self.listWidget_2.addItem("Student" + str(i))

        if Status == "Detail":
            pattern_Student = re.compile("Student+[0-9]*\.")
            text = ""
            # for i in Question_list:
            #     # if "Question" in i:
            #     if i == "Question4.1.2":
            i = item.text()
            Question = i.replace("Question", "")
            for j in Answer_list:
                QuestionOfStudent = pattern_Student.sub("", j)
                if Question == QuestionOfStudent:
                    text = text + Answer_list[j] + "     "

            global Count
            Word_frenquency = Word_Count.Word_Count(text)
            Count = dict(Word_frenquency.most_common(100))

            j = 0
            for i in Word_frenquency.most_common(20):
                word = i[0]
                frenquency = str(i[1])
                self.tableWidget.setItem(j, 0, QTableWidgetItem(word))
                self.tableWidget.setItem(j, 1, QTableWidgetItem(frenquency))
                j = j + 1

    def listWidget_2_Clicked(self, item):
        if Status == "Student":
            Text = item.text()
            Text2 = Text.replace("Question", Student_number + ".")
            try:
                self.textEdit_2_Up.setHtml(Question_list[Text[:-2]] +
                                           "<br><br>" + Question_list[Text])
            except:
                self.textEdit_2_Up.setHtml(Question_list[Text])

            self.textEdit_2_Down.setHtml(Answer_list[Text2])

        if Status == "Question":
            Text = listWidget_Text
            Text1 = item.text() + "." + Text.replace("Question", "")
            try:
                self.textEdit_2_Up.setHtml(Question_list[Text[:-2]] +
                                           "<br><br>" + Question_list[Text])
            except:
                self.textEdit_2_Up.setHtml(Question_list[Text])

            self.textEdit_2_Down.setHtml(Answer_list[Text1])

    def detail(self):
        self.tabWidget.setTabEnabled(2, True)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabText(2, "Detail")
        global Status
        Status = "Detail"

        self.listWidget.clear()
        for i in Question_list:
            if "Question" in i and "." in i:
                self.listWidget.addItem(i)

    def Exit(self):  # 点击 Exit
        sys.exit(0)

    def closeEvent(self, event):  # 程序关闭动画
        if self.animation is None:
            self.animation = QPropertyAnimation(self, b'windowOpacity')
            self.animation.setDuration(470)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.close)
            self.animation.start()
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
