#include "grid.h"

Grid::Grid(int grid_size, int box_size)
    :   _grid_size(grid_size),
        _box_size(box_size)
{
    // Initialize grid
    _data.resize(grid_size, std::vector<int>(grid_size, 0));
}

std::vector<int> Grid::getColumn(int column) const
{
    std::vector<int> column_data(_grid_size, 0);

    // 1. Check if row is valid
    if ((unsigned int)column >= _grid_size)
    {
        return column_data;
    }

    // 2. Construct return vector
    for (int row = 0; row < _grid_size; ++row)
    {
        column_data[row] = _data[row][column];
    }
    return column_data;
}

std::vector<int> Grid::getBox(int row, int column) const
{
    std::vector<int> box_data(_box_size * _box_size, 0);

    // 1. Check if row and column are valid
    if ((unsigned int)row >= _grid_size || (unsigned int)column >= _grid_size)
    {
        return box_data;
    }

    // 2. Construct box data
    int box_begin_row = row / _box_size * _box_size,
        box_begin_column = column / _box_size * _box_size;
    for (int r = 0; r < _box_size; ++r)
    {
        for (int c = 0; c < _box_size; ++c)
        {
            box_data[r * _box_size + c] = _data[r + box_begin_row][c + box_begin_column];
        }
    }
    return box_data;
}

void Grid::resetData()
{
    _data.clear();
    _data.resize(_grid_size, std::vector<int>(_grid_size, 0));
}