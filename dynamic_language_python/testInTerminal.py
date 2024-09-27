from sudoku import Sudoku

if __name__ == '__main__':
    
    try:
        while 1:
            input_string = str(input('Please input string():\n'))

            # Construct an instance
            sudoku = Sudoku()

            # Fail to parse
            if not sudoku.parse(input_string):
                print('The input string is invalid. Try another\n')
                continue

            # Print sudoku
            sudoku.print()

            # Serialization
            sudoku_string = sudoku.serialization()
            print('serialization: ', sudoku_string)

            # Compare with input string
            print('sudoku serialization equals to input string: ', input_string == sudoku_string)
            print('\n')
    except KeyboardInterrupt:
        print('Program ends')