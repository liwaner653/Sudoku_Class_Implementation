#ifndef _SUDOKU_H_
#define _SUDOKU_H_

#include <string_view>
#include "grid.h"

class Sudoku : public Grid
{
public:
    Sudoku();

    // 解析输入字符串
    bool parse(std::string_view str);
    // cell提示值
    std::vector<int> getInference(int row, int column) const;
    // 是否合法数独
    bool isAValidSudoku() const;
};

#endif //_SUDOKU_H_