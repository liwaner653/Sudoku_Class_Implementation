from PySide6.QtCore import QAbstractTableModel, QObject, Qt, Property, Signal

from sudoku.sudoku import Sudoku

class SudokuTableModel(QAbstractTableModel):

    messageChanged = Signal()

    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        # 数独
        self.__sudoku = Sudoku()
        # 显示提示
        self.__show_hint = False
        # 反馈信息
        self.__message = str()

    '''
    表格行数
    '''
    def rowCount(self, index):
        return 0 if index.isValid() else self.__sudoku.gridSize()

    '''
    表格列数
    '''
    def columnCount(self, index):
        return 0 if index.isValid() else self.__sudoku.gridSize()

    '''
    表格显示数据
    '''
    def data(self, index, role):
        if not index.isValid() or role != Qt.DisplayRole:
            return None

        # Show all hint numbers
        if self.__show_hint:
            inference_numbers = self.__sudoku.getInference(index.row(), index.column())
            return ' '.join(str(number) for number in inference_numbers)
        
        # Show fixed number
        fixed_number = self.__sudoku.at(index.row(), index.column())
        return "" if fixed_number == 0 else str(fixed_number)

    '''
    解析输入字符串
    '''
    def parse(self, input_string: str) -> bool:
        # 1. Try parsing
        parsing_result = self.__sudoku.parse(input_string)

        # 2. Make some feedback
        self.__message = "Parsing successfully" if parsing_result else "ERROR: Fail to parse"

        # 3. Refresh table
        self.beginResetModel()
        self.endResetModel()

        return parsing_result

    def message(self):
        return self.__message

    def showHint(self):
        return self.__show_hint

    def setShowHint(self, show_hint: bool):
        self.__show_hint = show_hint

        # Update feedback message
        self.__message = "Hints have been showed" if self.__show_hint else "Hints have been hidden"

        # Refresh UI table values
        self.beginResetModel()
        self.endResetModel()

    ''' Bind QML variables '''
    message = Property(str, message, notify=messageChanged)
    show_hint = Property(bool, showHint, setShowHint)