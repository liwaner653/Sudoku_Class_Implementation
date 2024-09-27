import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuickControls2 import QQuickStyle

from ui.sudokuTableModel import SudokuTableModel

if __name__ == "__main__":

    app = QApplication()
    QQuickStyle.setStyle("Material")

    engine = QQmlApplicationEngine()

    sudoku_table_model = SudokuTableModel()
    engine.rootContext().setContextProperty("sudoku_table_model", sudoku_table_model)
    engine.load("qml/main.qml")
    if len(engine.rootObjects()) == 0:
        sys.exit(-1)

    engine.rootObjects()[0].parseSignal.connect(sudoku_table_model.parse)

    sys.exit(app.exec())