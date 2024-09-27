cmake_minimum_required(VERSION 3.16)

project(hello VERSION 1.0 LANGUAGES CXX)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(Qt6 COMPONENTS Quick Gui Core Qml REQUIRED)

qt_standard_project_setup(REQUIRES 6.7)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

qt_add_executable(${PROJECT_NAME}
    src/sudoku/grid.cpp src/sudoku/grid.h
    src/sudoku/sudoku.cpp src/sudoku/sudoku.h
    src/sudokutablemodel.cpp src/sudokutablemodel.h
    qml/resource.qrc
    src/main.cpp
)

qt_add_qml_module(${PROJECT_NAME}
    URI SudokuTableModel
    QML_FILES
        qml/main.qml
    NO_RESOURCE_TARGET_PATH
)

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
target_link_libraries(${PROJECT_NAME} PRIVATE Qt6::Gui Qt6::Quick Qt6::Core Qt6::Qml)

install(TARGETS ${PROJECT_NAME}
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)