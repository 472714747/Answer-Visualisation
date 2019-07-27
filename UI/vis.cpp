#include "vis.h"
#include "ui_vis.h"

vis::vis(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::vis)
{
    ui->setupUi(this);
}

vis::~vis()
{
    delete ui;
}
