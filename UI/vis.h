#ifndef VIS_H
#define VIS_H

#include <QMainWindow>

namespace Ui {
class vis;
}

class vis : public QMainWindow
{
    Q_OBJECT

public:
    explicit vis(QWidget *parent = nullptr);
    ~vis();

private:
    Ui::vis *ui;
};

#endif // VIS_H
