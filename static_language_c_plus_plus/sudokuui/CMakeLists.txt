cmake_minimum_required(VERSION 3.14)

project(SudokuUi VERSION 1.0 LANGUAGES CXX)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

find_package(Qt6 COMPONENTS Quick Gui Core Qml REQUIRED)

qt_standard_project_setup(REQUIRES 6.7)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

qt_add_executable(${PROJECT_NAME}
    sudokutablemodel.cpp 
    sudokutablemodel.h
    qml/resource.qrc
    main.cpp
)

target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../sudoku)

qt_add_qml_module(${PROJECT_NAME}
    URI SudokuTableModel
    QML_FILES
        qml/main.qml
    NO_RESOURCE_TARGET_PATH
)

target_link_libraries(${PROJECT_NAME} PRIVATE Qt6::Gui Qt6::Quick Qt6::Core Qt6::Qml Sudoku)