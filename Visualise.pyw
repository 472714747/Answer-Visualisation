import matplotlib
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets

matplotlib.use("Qt5Agg")  # 声明使用QT5


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=18, height=4.3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.axes = fig.add_subplot(111)

    def ShowSame(self, same, Count, Count2):
        myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

        a = []
        b = []
        for i in same:
            a.append(dict(Count)[i])
            b.append(dict(Count2)[i])

        width = 0.3

        length = len(same)
        position = np.arange(length) * 2

        self.axes.bar(position, a, width, label="Standard")
        self.axes.bar(position + width, b, width, label="Students")
        self.axes.set_xticks((position * 2 + width) / 2)
        self.axes.set_xticklabels(same, fontproperties=myfont)

        for i in range(length):
            self.axes.text(position[i],
                           a[i] + 0.05,
                           a[i],
                           ha='center',
                           va='bottom')
            self.axes.text(position[i] + width,
                           b[i] + 0.05,
                           b[i],
                           ha='center',
                           va='bottom')

        self.axes.legend()

    def ShowDifferent(self, different, Count, Count2):
        myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

        a = []
        b = []
        x_a = []
        x_b = []
        for i in different:
            if i in dict(Count):
                a.append(dict(Count)[i])
                x_a.append(i)
            else:
                b.append(dict(Count2)[i])
                x_b.append(i)

        width = 1
        length = len(different) * 3
        length_a = len(x_a)

        position = np.arange(0, length, 3)
        position_a = list(np.arange(length_a) * 3)
        position_b = list(set(position) - set(position_a))

        if a != []:
            self.axes.bar(position_a, a, width, label="Standard")
        if b != []:
            self.axes.bar(position_b, b, width, label="Students")
        self.axes.set_xticks(position_a + position_b)
        self.axes.set_xticklabels(x_a + x_b, fontproperties=myfont)

        if x_a != []:
            for i in range(len(x_a)):
                self.axes.text(position_a[i],
                               a[i] + 0.05,
                               a[i],
                               ha='center',
                               va='bottom')
        if x_b != []:
            for i in range(len(x_b)):
                self.axes.text(position_b[i],
                               b[i] + 0.05,
                               b[i],
                               ha='center',
                               va='bottom')

        self.axes.legend()


def init(self, same, different, Count, Count2):
    if same != []:
        FigSame = Figure_Canvas()
        FigSame.ShowSame(same, Count, Count2)

    if different != []:
        FigDiff = Figure_Canvas()
        FigDiff.ShowDifferent(different[0:21], Count, Count2)

    graphicscene = QtWidgets.QGraphicsScene()
    graphicscene_2 = QtWidgets.QGraphicsScene()

    graphicscene.addWidget(FigSame)
    graphicscene_2.addWidget(FigDiff)

    self.graphicsView.setScene(graphicscene)
    self.graphicsView.show()

    self.graphicsView_2.setScene(graphicscene_2)
    self.graphicsView_2.show()
