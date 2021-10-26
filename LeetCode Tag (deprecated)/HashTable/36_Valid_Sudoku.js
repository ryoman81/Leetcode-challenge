/**
 * Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
 * 
 * Each row must contain the digits 1-9 without repetition.
 * Each column must contain the digits 1-9 without repetition.
 * Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
 * The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
 */

var isValidSudoku = function(board) {
    const table_row = [{},{},{},{},{},{},{},{},{}];
    const table_col = [{},{},{},{},{},{},{},{},{}];
    const table_cel = [{},{},{},{},{},{},{},{},{}];
    
    for (let i = 0; i < 9; i++) {
        
        for (let j = 0; j < 9; j++) {
            if (board[i][j] === ".") continue;
            const crr = board[i][j];
            const indZone = parseInt(i/3)*3 + parseInt(j/3);

            if (table_row[i][crr]) return false;
            if (table_col[j][crr]) return false;
            if (table_cel[indZone][crr]) return false;
            
            table_row[i][crr] = [i,j];
            table_col[j][crr] = [i,j];
            table_cel[indZone][crr] = [i,j];
            
        }
    }

    return true;
};

const input = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
  ];

  const result = isValidSudoku(input);
  console.log(result);