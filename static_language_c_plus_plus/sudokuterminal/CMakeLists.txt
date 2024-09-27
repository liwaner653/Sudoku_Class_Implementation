cmake_minimum_required(VERSION 3.14)

project(SudokuTerminal VERSION 1.0 LANGUAGES CXX)

set(SudokuIncludeDir ${CMAKE_CURRENT_SOURCE_DIR})

add_executable(${PROJECT_NAME} main.cpp)

target_include_directories(${PROJECT_NAME} PUBLIC ${SudokuIncludeDir})
target_link_libraries(${PROJECT_NAME} PRIVATE Sudoku)