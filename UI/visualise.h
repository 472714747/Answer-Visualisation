#ifndef VISUALISE_H
#define VISUALISE_H

#include <QMainWindow>

namespace Ui {
class visualise;
}

class visualise : public QMainWindow
{
    Q_OBJECT

public:
    explicit visualise(QWidget *parent = nullptr);
    ~visualise();

private:
    Ui::visualise *ui;
};

#endif // VISUALISE_H
