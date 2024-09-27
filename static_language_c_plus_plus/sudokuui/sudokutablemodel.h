#ifndef _SUDOKU_TABLE_MODEL_H_
#define _SUDOKU_TABLE_MODEL_H_

#include <QAbstractTableModel>
#include <QtQml/qqml.h>
#include "sudoku.h"

// 网格表格数据
class SudokuTableModel : public QAbstractTableModel
{
    Q_OBJECT
    Q_PROPERTY(bool show_hint READ showHint WRITE setShowHint)
    Q_PROPERTY(QString message READ message NOTIFY messageChanged)

public:
    SudokuTableModel(QObject* parent = nullptr);

    bool showHint() const;
    void setShowHint(bool show_hint);

    QString message() const;

    int rowCount(const QModelIndex &parent = QModelIndex()) const override;
    int columnCount(const QModelIndex &parent = QModelIndex()) const override;

    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;

signals:
    void messageChanged();

public slots:
    // 解析输入字符串
    bool parse(QString str);

private:
    //网格数据
    Sudoku _sudoku;
    //显示提示数字
    bool _show_hint = false;
    //提示文字
    QString _msg;
};

inline bool SudokuTableModel::showHint() const
{
    return _show_hint;
}
inline void SudokuTableModel::setShowHint(bool show_hint)
{
    _show_hint = show_hint;
    _msg = _show_hint ? "Hints have been showed" : "Hints have been hidden";
    
    beginResetModel();
    endResetModel();
}
inline QString SudokuTableModel::message() const
{
    return _msg;
}

#endif //_SUDOKU_TABLE_MODEL_H_