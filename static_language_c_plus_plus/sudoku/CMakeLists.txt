cmake_minimum_required(VERSION 3.14)

project(Sudoku VERSION 1.0 LANGUAGES CXX)

set(SudokuIncludeDir ${CMAKE_CURRENT_SOURCE_DIR})

add_library(${PROJECT_NAME} STATIC
    grid.cpp 
    grid.h
    sudoku.cpp 
    sudoku.h
)
target_include_directories(${PROJECT_NAME} PUBLIC ${SudokuIncludeDir})