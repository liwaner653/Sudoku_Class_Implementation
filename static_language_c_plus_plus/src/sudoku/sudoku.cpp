#include <set>
#include "sudoku.h"

Sudoku::Sudoku()
    : Grid(9, 3)
{
}

bool Sudoku::parse(std::string_view str)
{
    // 1. Check if its size equals to the size of the grid
    if (str.size() != _grid_size * _grid_size)
    {
        resetData();
        return false;
    }

    // Limit number between 0 and _grid_size
    auto isCharAValidNumber = [this](char c){
        return c >= '0' && c <= '0' + _grid_size;
    };

    // 2. Parse input string
    for (int i = 0; i < str.size(); ++i)
    {
        if (!isCharAValidNumber(str[i])) // Between 0 and _grid_size
        {
            resetData();
            return false;
        }
        _data[i / _grid_size][i % _grid_size] = str[i] - '0';
    }

    // 3. Check if the sudoku is valid
    if (!isAValidSudoku())
    {
        resetData();
        return false;
    }

    return true;
}

std::vector<int> Sudoku::getInference(int row, int column) const
{
    // 1. Find out all numbers in the same row, column and box
    std::set<int> existed_numbers;
    // Add data to set
    auto addToSet = [&existed_numbers](const std::vector<int>& data) {
        existed_numbers.insert(data.begin(), data.end());
    };
    addToSet(getRow(row));          // Add same row numbers
    addToSet(getColumn(column));    // Add same column numbers
    addToSet(getBox(row, column));  // Add same box numbers
    
    // 2. Find out numbers not show yet
    std::vector<int> numbers_not_showed;
    for (int i = 1; i <= _grid_size; ++i)
    {
        if (existed_numbers.find(i) != existed_numbers.end())
            continue;

        numbers_not_showed.emplace_back(i);
    }
    return numbers_not_showed;
}

bool Sudoku::isAValidSudoku() const
{
    auto sameNumberExistsInOneArray = [this](const std::vector<int>& arr){
        std::set<int> unique_numbers;
        for(int i : arr)
        {
            // 1. Skip 0
            if (i == 0)
            {
                continue;
            }

            // 2. If same number exists in one array, exit
            if (unique_numbers.find(i) != unique_numbers.end())
            {
                return true;
            }

            unique_numbers.emplace(i);
        }
        // 3. This array is valid
        return false;
    };

    // 1. Check all the rows
    for (int r = 0; r < _grid_size; ++r)
    {
        if (sameNumberExistsInOneArray(getRow(r)))
            return false;
    }

    // 2. Check all the columns
    for (int c = 0; c < _grid_size; ++c)
    {
        if (sameNumberExistsInOneArray(getColumn(c)))
            return false;
    }

    // 3. Check all the boxes
    for (int r = 0; r < _box_size; ++r)
    {
        for (int c = 0; c < _box_size; ++c)
        {
            if (sameNumberExistsInOneArray(getBox(r * _box_size, c * _box_size)))
                return false;
        }
    }

    // 4. This is a valid sudoku
    return true;
}