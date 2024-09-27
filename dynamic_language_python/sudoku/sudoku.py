import numpy as np

from .grid import Grid

'''数独'''
class Sudoku(Grid):
    def __init__(self):
        super().__init__(9, 3)

    '''
    解析输入字符串
    '''
    def parse(self, input_string: str) -> bool:
        # 1. Check if input string size equals to the grid
        if len(input_string) != self._grid_size * self._grid_size:
            self._resetData()
            return False
        
        # 2. Check if the char is a number
        for i, number in enumerate(input_string):
            if int(number) < 0 or int(number) > self._grid_size:
                self._resetData()
                return False
            
            self._data[i // self._grid_size][i % self._grid_size] = int(number)
        
        # 3. Check if the sudoku is valid
        if not self.__isSudokuValid():
            self._resetData()
            return False
        
        return True

    '''
    推所有可能值
    '''
    def getInference(self, row, column) -> list:
        # 1. Find out all existed numbers in same row, column and box
        existed_numbers = set(self.getRow(row))
        existed_numbers.update(self.getColumn(column))
        existed_numbers.update(self.getBox(row, column))

        # 2. Inference not showed up numbers(diff of two sets)
        return list(set(range(1, self._grid_size + 1)) - existed_numbers)
    
    '''
    检查数组是否合法(同行，列，格中是否存在相同数字)
    '''
    def __isSudokuValid(self) -> bool:
        # arr里存在同样的数字
        def containSameNumber(arr: np.array):
            numbers_count = np.bincount(arr)
            return np.any(numbers_count[1:] > 1) # Remove number 0

        # 1. Check all rows
        for r in range(self._grid_size):
            if containSameNumber(self.getRow(r)):
                return False
    
        # 2. Check all columns
        for c in range(self._grid_size):
            if containSameNumber(self.getColumn(c)):
                return False
        
        # 3. Check all boxes
        for r in range(0, self._grid_size, self._box_size):
            for c in range(0, self._grid_size, self._box_size):
                if containSameNumber(self.getBox(r, c)):
                    return False
        
        return True
