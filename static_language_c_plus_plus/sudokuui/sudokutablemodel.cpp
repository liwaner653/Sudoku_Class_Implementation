#include "sudokutablemodel.h"

SudokuTableModel::SudokuTableModel(QObject* parent /*= nullptr*/)
    : QAbstractTableModel(parent)
{

}

int SudokuTableModel::rowCount(const QModelIndex &parent /*= QModelIndex()*/) const
{
    return parent.isValid() ? 0 : _sudoku.gridSize();
}

int SudokuTableModel::columnCount(const QModelIndex &parent /*= QModelIndex()*/) const
{
    return parent.isValid() ? 0 : _sudoku.gridSize();
}

QVariant SudokuTableModel::data(const QModelIndex &index, int role /*= Qt::DisplayRole*/) const
{
    if (!index.isValid() || role != Qt::DisplayRole)
    {
        return QVariant();
    }

    // 固定值
    auto isFixedNumber = [this, &index](int row, int column){
        return _sudoku.at(row, column) > 0;
    };

    switch (role)
    {
    case Qt::DisplayRole: 
    {
        // Show hint numbers
        if (_show_hint && !isFixedNumber(index.row(), index.column()))
        {
            std::vector<int> cell_hint_numbers = _sudoku.getInference(index.row(), index.column());
            QString hint_numbers_string;
            for(int hint_number : cell_hint_numbers)
                hint_numbers_string += QString::number(hint_number) + " ";
            return hint_numbers_string.mid(0, hint_numbers_string.size() - 1);
        }

        // Show fixed numbers
        int cell_number = _sudoku.at(index.row(), index.column());
        return cell_number == 0 ? QString("") : QString::number(cell_number); 
    }
    }

    return QVariant();
}

bool SudokuTableModel::parse(QString str)
{
    // 1. Parse input string
    bool result = _sudoku.parse(str.toStdString());
    _msg = result ? "Parsing successfully" : "ERROR: Fail to parse!\nPlease check the input string";

    // 2. Refresh table numbers if success
    beginResetModel();
    endResetModel();
    
    return result;
}