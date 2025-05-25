def printTable(tableData):
    # Number of columns is the number of inner lists
    num_cols = len(tableData)
    # Number of rows is the length of each inner list
    num_rows = len(tableData[0])

    # Find the maximum width of each column 
    colWidths = [0] * num_cols
    for col in range(num_cols):
        max_len = 0
        for item in tableData[col]:
            if len(item) > max_len:
                max_len = len(item)
        colWidths[col] = max_len

    # Print the table row by row
    for row in range(num_rows):
        for col in range(num_cols):
            # Right-justify everything by column width
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print("\n") 

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
