#ifndef _GRID_H_
#define _GRID_H_

#include <vector>

// 网格
class Grid
{
public:
    Grid(int grid_size, int box_size);

    // 获取一行数据
    std::vector<int> getRow(int row) const;
    // 获取一列数据
    std::vector<int> getColumn(int column) const;
    // 获取box数据
    std::vector<int> getBox(int row, int column) const;

    // 第row行第columm列数字
    int at(int row, int column) const;
    // 网格数
    int gridSize() const;

    // 清空数据
    void resetData();

protected:
    //  方阵行列数   
    int _grid_size, _box_size;
    // 方阵数据
    std::vector<std::vector<int>> _data;
};

inline std::vector<int> Grid::getRow(int row) const
{
    return (unsigned int)row >= _grid_size ? 
        std::vector<int>(_grid_size, 0) :   // If row is invalid
        _data[row];
}
inline int Grid::at(int row, int column) const
{
    if ((unsigned int)row >= _grid_size || (unsigned int)column >= _grid_size)
        return 0;

    return _data[row][column];
}
inline int Grid::gridSize() const
{
    return _grid_size;
}

#endif //_GRID_H_