#include <iostream>

#include "sudoku.h"

using std::cout;
using std::cin;
using std::endl;

int main(int argc, char *argv[])
{
    std::string input_string;// = "017903600000080000900000507072010430000402070064370250701000065000030000005601720";

    cout << "Please input string(Ctrl+C ends it):\n";
    while(cin >> input_string)
    {
        // Parse input string
        Sudoku sudoku;
        if (!sudoku.parse(input_string))
        {
            cout << "The input string is invalid. Try another\n";
            cout << "\nPlease input string: ";
            continue;
        }

        // Print sudoku if parsing successfully
        sudoku.print();

        // Serialize sudoku to string
        std::string sudoku_string = sudoku.serialization();
        cout << "serialization: " << sudoku_string << endl;

        // Check parsing result
        cout << "sudoku serialization equals to input string: " 
                << (input_string.compare(sudoku_string) == 0 ? "True" : "False")
                << endl;

        cout << "\nPlease input string: ";
    }

    return 0;
}