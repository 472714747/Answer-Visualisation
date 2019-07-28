#include "visualise.h"
#include "ui_visualise.h"

visualise::visualise(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::visualise)
{
    ui->setupUi(this);
}

visualise::~visualise()
{
    delete ui;
}
