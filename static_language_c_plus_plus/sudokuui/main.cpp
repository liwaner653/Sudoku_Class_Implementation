#include <QQmlContext>
#include <QGuiApplication>
#include <QQmlApplicationEngine>

#include "sudoku.h"
#include "sudokutablemodel.h"

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);

    QQmlApplicationEngine engine;

    SudokuTableModel model;
    engine.rootContext()->setContextProperty("sudoku_table_model", &model);
    engine.load(":qml/main.qml");
    if (engine.rootObjects().isEmpty())
    {
        return -1;
    }

    auto objects = engine.rootObjects();
    QObject::connect(objects.front(), SIGNAL(parseSignal(QString)), &model, SLOT(parse(QString)));

    return app.exec();
}