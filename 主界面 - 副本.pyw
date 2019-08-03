import sys, re, pandas
from collections import Counter

from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5.QtWidgets import QApplication, QFileDialog, QTabWidget, QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QTableWidget, QFrame, QTableWidgetItem, QHeaderView

sys.path.append(
    r'L:\OneDrive - UOM\University of Manchester\PGT\Project\Tool\Spider')
sys.path.append(
    r'L:\OneDrive - UOM\University of Manchester\PGT\Project\Tool\UI')
sys.path.append(
    r'C:\Users\ang\OneDrive - UOM\University of Manchester\PGT\Project\Tool\Spider'
)
sys.path.append(
    r'C:\Users\ang\OneDrive - UOM\University of Manchester\PGT\Project\Tool\UI'
)

import Questions, Standard_Answers, Student_Answers, Word_Count, Visualise

Ui_MainWindow, Base1 = uic.loadUiType("UI/mainwindow.ui")
Vis_Window, Base2 = uic.loadUiType("UI/Visualise.ui")

Question_list = {}
Standard_list = {}
Answer_list = {}
filetype = ""
Status = ""
Student_number = ""
listWidget_Text = ""
Count = {}
Word_frenquency = Counter()
Word_frenquency2 = Counter()
Question_number = ""
list_same = []
list_different = []
Sub_list_same = []
Sub_list_different = []
sub = ""
Count = Counter("")
Count2 = Counter("")


class MainWindow(Base1, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # 禁用按钮
        self.menuView.setEnabled(False)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)
        self.tabWidget.setTabEnabled(3, False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)

        # 点击事件
        self.actionOpen.triggered.connect(self.Openfile)
        self.actionSave.triggered.connect(self.Save)
        self.actionExit.triggered.connect(self.Exit)
        self.actionStudent.triggered.connect(self.Student_View)
        self.actionQuestion.triggered.connect(self.Question_View)
        self.actionCompare.triggered.connect(self.Compare)

        self.listWidget.itemClicked.connect(self.listWidget_Clicked)
        self.listWidget_2.itemClicked.connect(self.listWidget_2_Clicked)

        self.pushButton.clicked.connect(self.detail)
        self.pushButton_3.clicked.connect(self.Subtract)
        self.pushButton_4.clicked.connect(self.vis_list)
        self.pushButton_5.clicked.connect(self.vis_sub_list)

        self.animation = None

        # 双击取词
        self.textEdit_2_Up.copyAvailable.connect(self.textCopy_Up)
        self.textEdit_2_Down.copyAvailable.connect(self.textCopy_Down)

        # Tab3搜索栏加图标
        myAction = QtWidgets.QAction(self.lineEdit)
        myAction.setIcon(QtGui.QIcon("./UI/Icons/search.png"))
        myAction.triggered.connect(self.search)

        self.lineEdit.addAction(myAction, QtWidgets.QLineEdit.TrailingPosition)
        self.lineEdit.returnPressed.connect(self.search)

        # 添加阴影
        # effect = QGraphicsDropShadowEffect(self)
        # effect.setBlurRadius(12)
        # effect.setOffset(0, 0)
        # effect.setColor(Qt.gray)
        # self.widget.setGraphicsEffect(effect)

    def setTable(self):
        self.tableStandard.setHorizontalHeaderLabels(['Words', 'Frequency'])
        self.tableStudent.setHorizontalHeaderLabels(['Words', 'Frequency'])
        self.tableCompare.setHorizontalHeaderLabels(['Same', 'Different'])

    def Openfile(self):  # 打开文件
        self.listWidget.clear()
        global filetype
        filename, filetype = QFileDialog.getOpenFileName(
            self, "Open File", "./",
            "Questions File (*.exam);;Standard Answers File (*.stan);;Student Answers File (*.aset)"
        )

        if filename != "":  # 成功选择文件
            self.listWidget.clear()
            global Question_list

            if filetype == "Questions File (*.exam)":  # 考试试题
                self.menuView.setEnabled(False)
                self.textEdit_Up.clear()
                self.textEdit_Down.clear()
                self.tabWidget.setTabEnabled(1, False)
                self.tabWidget.setTabText(0, "Question")

                Question_list = Questions.Open(filename)

                for i in Question_list:
                    self.listWidget.addItem(str(i))

            if filetype == "Standard Answers File (*.stan)":  # 标准答案
                self.menuView.setEnabled(False)
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
            pandas.DataFrame.from_dict(dict(Count),
                                       orient='index').T.to_csv(fname,
                                                                index=False)

        f = pandas.read_csv(fname)
        f_T = f.T
        f_T.to_csv(fname)

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
        global Count, Count2, Word_frenquency, Word_frenquency2

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

        if Status == "Detail":  # 查看词频
            pattern_Student = re.compile("Student+[0-9]*\.")
            text = ""
            i = item.text()
            Question = i.replace("Question", "")
            for j in Answer_list:
                QuestionOfStudent = pattern_Student.sub("", j)
                if Question == QuestionOfStudent:
                    text = text + Answer_list[j] + "     "

            Word_frenquency = Word_Count.Word_Count(text)
            Count = Word_frenquency.most_common(200)  # 保存用

            j = 0
            for i in Word_frenquency.most_common(20):
                word = i[0]
                frenquency = str(i[1])
                self.tableWidget.setItem(j, 0, QTableWidgetItem(word))
                self.tableWidget.setItem(j, 1, QTableWidgetItem(frenquency))
                j = j + 1

        if Status == "Compare":
            self.pushButton_3.setEnabled(True)
            self.pushButton_4.setEnabled(True)
            self.pushButton_5.setEnabled(True)
            self.tableStandard.clear()
            self.tableStudent.clear()
            self.tableCompare.clear()

            # 标准答案。
            i = item.text()
            Question = i.replace("Question", "Standard_Answer")
            text = Standard_list[Question]

            Word_frenquency = Word_Count.Word_Count(text)
            number = min(len(dict(Word_frenquency)), 200)
            self.tableStandard.setRowCount(number)
            Count = Word_frenquency.most_common(200)  # 保存用

            j = 0
            for i in Count:
                word = i[0]
                frenquency = str(i[1])
                self.tableStandard.setItem(j, 0, QTableWidgetItem(word))
                self.tableStandard.setItem(j, 1, QTableWidgetItem(frenquency))
                j = j + 1

            # 学生答案
            pattern_Student = re.compile("Student+[0-9]*\.")
            text2 = ""
            i = item.text()
            Question = i.replace("Question", "")
            for j in Answer_list:
                QuestionOfStudent = pattern_Student.sub("", j)
                if Question == QuestionOfStudent:
                    text2 = text2 + Answer_list[j] + "     "

            Word_frenquency2 = Word_Count.Word_Count(text2)
            number = min(len(dict(Word_frenquency2)), 20)
            self.tableStudent.setRowCount(number)
            Count2 = Word_frenquency2.most_common(20)  # 保存用

            j = 0
            for i in Count2:
                word = i[0]
                frenquency = str(i[1])
                self.tableStudent.setItem(j, 0, QTableWidgetItem(word))
                self.tableStudent.setItem(j, 1, QTableWidgetItem(frenquency))
                j = j + 1

            # 对比
            global list_same, list_different
            list_same = []
            list_different = []

            list1 = list(dict(Count).keys())
            list2 = list(dict(Count2).keys())

            for i in list1:
                if i in list2:
                    list_same.append(i)
                if i not in list2:
                    list_different.append(i)

            for i in list2:
                if i in list1:
                    list_same.append(i)
                if i not in list1:
                    list_different.append(i)

            list_same = list(set(list_same))
            list_different = list(set(list_different))

            length = max(len(list_same), len(list_different))
            self.tableCompare.setRowCount(length)
            i = 0
            j = 0
            for element in list_same:
                self.tableCompare.setItem(i, 0, QTableWidgetItem(element))
                i = i + 1

            for element in list_different:
                self.tableCompare.setItem(j, 1, QTableWidgetItem(element))
                j = j + 1

    def listWidget_2_Clicked(self, item):
        global Question_number

        if Status == "Student":
            Text = item.text()
            Text2 = Text.replace("Question", Student_number + ".")
            Question_number = Text

            try:
                self.textEdit_2_Up.setHtml(Question_list[Text[:-2]] +
                                           "<br><br>" + Question_list[Text])
            except:
                self.textEdit_2_Up.setHtml(Question_list[Text])

            self.textEdit_2_Down.setHtml(Answer_list[Text2])

        if Status == "Question":
            Text = listWidget_Text
            Text1 = item.text() + "." + Text.replace("Question", "")
            Question_number = Text1

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
            if "Question" in i and "." in i and i != "Question4.1":
                self.listWidget.addItem(i)

    def textCopy_Up(self, status):  # 取词查频
        if status is True:
            self.textEdit_2_Up.copy()
            command = QApplication.clipboard().text()
            original = Word_Count.Original(command)[0]

            pattern_Student = re.compile("Student+[0-9]*\.")
            text = ""
            i = Question_number
            Question = i.replace("Question", "")
            for j in Answer_list:
                QuestionOfStudent = pattern_Student.sub("", j)
                if Question == QuestionOfStudent:
                    text = text + Answer_list[j] + "     "

            Word_frenquency = Word_Count.Word_Count(text)
            word_list = dict(Word_frenquency.most_common(1000))

            if original in word_list.keys():
                self.lineEdit_2.setText("The word " + "\"" + command + "\"" +
                                        " appears " +
                                        str(word_list[original]) +
                                        " times in all students' answers")
            else:
                self.lineEdit_2.setText("The word " + "\"" + command + "\"" +
                                        " doesn't appear in students' answers")

    def textCopy_Down(self, status):  # 取词查频
        if status is True:
            self.textEdit_2_Down.copy()
            command = QApplication.clipboard().text()
            original = Word_Count.Original(command)[0]

            pattern_Student = re.compile("Student+[0-9]*\.")
            text = ""
            i = Question_number
            Question = i.replace("Question", "")
            for j in Answer_list:
                QuestionOfStudent = pattern_Student.sub("", j)
                if Question == QuestionOfStudent:
                    text = text + Answer_list[j] + "     "

            Word_frenquency = Word_Count.Word_Count(text)
            word_list = dict(Word_frenquency.most_common(1000))

            if original in word_list.keys():
                self.lineEdit_2.setText("The word " + "\"" + command + "\"" +
                                        " appears " +
                                        str(word_list[original]) +
                                        " times in all students' answers.")
            else:
                self.lineEdit_2.setText(
                    "The word " + "\"" + command + "\"" +
                    " doesn't appear in students' answers.")

    def search(self):
        self.tableWidget.clear()
        for i in Count:
            if i[0] == self.lineEdit.text():
                word = self.lineEdit.text()
                frenquency = str(i[1])
                self.tableWidget.setItem(0, 0, QTableWidgetItem(word))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(frenquency))

    def search2(self):
        self.tableWidget.clear()
        for i in Count:
            if i[0] == self.lineEdit.text():
                word = self.lineEdit.text()
                frenquency = str(i[1])
                self.tableWidget.setItem(0, 0, QTableWidgetItem(word))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(frenquency))

    def Compare(self):  # 对比界面
        self.listWidget.clear()
        self.tableStandard.clear()
        self.tableStudent.clear()
        self.tableCompare.clear()
        self.setTable()

        filename, haha = QFileDialog.getOpenFileName(
            self, "Open File", "./", "Standard Answers File (*.stan)")

        if filename != "":  # 成功选择文件
            global Question_list
            global Standard_list
            global Answer_list
            global Status
            Status = "Compare"

            self.tabWidget.setTabEnabled(0, False)
            self.tabWidget.setTabEnabled(1, False)
            self.tabWidget.setTabEnabled(2, False)
            self.tabWidget.setTabEnabled(3, True)
            self.tabWidget.setTabText(3, "Compare")

            Question_list = Questions.Open(filename.replace("stan", "exam"))
            Standard_list = Standard_Answers.Open(filename)
            Answer_list = Student_Answers.Open(filename.replace(
                "stan", "aset"))

            for i in Standard_list:
                self.listWidget.addItem(
                    i.replace("Standard_Answer", "Question"))

    def Subtract(self):  # 减去常用词
        self.tableStandard.clear()
        self.tableStudent.clear()
        self.tableCompare.clear()
        self.pushButton_3.setEnabled(False)
        self.setTable()
        global Word_frenquency, Word_frenquency2

        file = open("./Spider/Normal_Words.csv")
        a = file.read().split()
        file.close()

        Word_frenquency = dict(Word_frenquency.most_common(200))
        Word_frenquency2 = dict(Word_frenquency2.most_common(20))
        Sub_list1 = {}
        Sub_list2 = {}

        for element in Word_frenquency.keys():
            if element not in a:
                Sub_list1[element] = Word_frenquency[element]

        for element in Word_frenquency2.keys():
            if element not in a:
                Sub_list2[element] = Word_frenquency2[element]

        number1 = len(Sub_list1)
        number2 = len(Sub_list2)
        self.tableStandard.setRowCount(number1)
        self.tableStudent.setRowCount(number2)

        i = 0
        j = 0
        for element in Sub_list1:
            self.tableStandard.setItem(i, 0, QTableWidgetItem(element))
            self.tableStandard.setItem(
                i, 1, QTableWidgetItem(str(Sub_list1[element])))
            i = i + 1

        for element in Sub_list2:
            self.tableStudent.setItem(j, 0, QTableWidgetItem(element))
            self.tableStudent.setItem(
                j, 1, QTableWidgetItem(str(Sub_list2[element])))
            j = j + 1

        global Sub_list_same, Sub_list_different
        Sub_list_same = []
        Sub_list_different = []

        for i in Sub_list1.keys():
            if i in Sub_list2.keys():
                Sub_list_same.append(i)
            if i not in Sub_list2.keys():
                Sub_list_different.append(i)

        for i in Sub_list2.keys():
            if i in Sub_list1.keys():
                Sub_list_same.append(i)
            if i not in Sub_list1.keys():
                Sub_list_different.append(i)

        Sub_list_same = list(set(Sub_list_same))
        Sub_list_different = list(set(Sub_list_different))

        length = max(len(Sub_list_same), len(Sub_list_different))
        self.tableCompare.setRowCount(length)

        i = 0
        j = 0
        for element in Sub_list_same:
            self.tableCompare.setItem(i, 0, QTableWidgetItem(element))
            i = i + 1

        for element in Sub_list_different:
            self.tableCompare.setItem(j, 1, QTableWidgetItem(element))
            j = j + 1

    def vis_list(self):
        global sub
        sub = "no"

        self.main = Visualise_Window()
        self.main.show()
        self.close()

    def vis_sub_list(self):
        global sub
        sub = "yes"

        self.main = Visualise_Window()
        self.main.show()
        self.close()

    def closeEvent(self, event):  # 程序关闭动画
        if self.animation is None:
            self.animation = QPropertyAnimation(self, b'windowOpacity')
            self.animation.setDuration(470)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.close)
            self.animation.start()
            event.ignore()

    def Exit(self):  # 点击 Exit
        self.close()


class Visualise_Window(Base2, Vis_Window):
    def __init__(self):
        super(Base2, self).__init__()
        self.setupUi(self)
        self.showMaximized()

        # 初始化界面
        if sub == "yes":
            Visualise.init(self, Sub_list_same, Sub_list_different, Count,
                           Count2)

        if sub == "no":
            Visualise.init(self, list_same, list_different, Count, Count2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
