import numpy as np

class Grid:
    def __init__(self, grid_size, box_size):
        self._grid_size = grid_size
        self._box_size = box_size
        self._data = np.zeros((grid_size, grid_size), dtype=int)

    # 获得第row行数据
    def getRow(self, row):
        if row >= self._grid_size or row < 0: 
            return np.array()

        return self._data[row, :]

    # 获得第column列数据
    def getColumn(self, column):
        if column >= self._grid_size or column < 0:
            return np.array()
        
        return self._data[:, column]
    
    # 获取第row行第column列所在box的数据
    def getBox(self, row, column):
        if row >= self._grid_size or row < 0 or         \
            column >= self._grid_size or column < 0:
            return np.array()

        box_begin_index = row // self._box_size
        box_end_index = column // self._box_size
        return self._data[box_begin_index : box_begin_index + self._box_size,
                          box_end_index   : box_end_index + self._box_size].flatten()

    # 获取第row行第column列数字
    def at(self, row, column):
        if row >= self._grid_size or row < 0 or         \
            column >= self._grid_size or column < 0:
            return 0

        return self._data[row][column]

    # 返回网格size
    def gridSize(self):
        return self._grid_size

    # 重置网格数据
    def _resetData(self):
        self._data = np.zeros((self._grid_size, self._grid_size), dtype=int)