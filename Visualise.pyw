import matplotlib
import matplotlib.font_manager as fm
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets

matplotlib.use("Qt5Agg")  # 声明使用QT5


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.axes = fig.add_subplot(111)

    def test(self, same):
        myfont = fm.FontProperties(fname='C:/Windows/Fonts/msyh.ttc')

        a = [23, 21, 32, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        b = [10, 15, 32, 12, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        width = 0.3

        length = len(same)
        position = np.arange(length) * 2

        self.axes.bar(position, a, width, label="Standard")
        self.axes.bar(position + width, b, width, label="Students")
        self.axes.set_xticks((position * 2 + width) / 2)
        self.axes.set_xticklabels(same, fontproperties=myfont)
        self.axes.legend()


def init(self, same, different):

    dr = Figure_Canvas()

    dr.test(same)
    graphicscene = QtWidgets.QGraphicsScene()
    graphicscene.addWidget(dr)

    self.graphicsView.setScene(graphicscene)
    self.graphicsView.show()
