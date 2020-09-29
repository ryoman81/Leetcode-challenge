
/*var rotate = function(matrix) {
    const n = matrix.length;    // dimension of matrix
    // loop over the circle
    for (let i = 0; i < Math.ceil(n/2); i++) {
        // starting point at current circle: [i, i] loop over the numbers
        for (let j = i; j < n-1-i; j++) {
            // point at [i, j] do four switches
            let row = i, col = j;
            let val = matrix[i][j];
            let val_next;
            for (let k = 0; k < 4; k++) {
                let row_next = col;
                let col_next = n-1 - row;
                val_next = matrix[row_next][col_next];
                matrix[row_next][col_next] = val;
                val = val_next;
                row = row_next;
                col = col_next;
            }
        }
    }

    return matrix;
};
*/

// Method two: we reverse matrix up-side-down, then transpose matrix
var rotate = function(matrix) {
    matrix.reverse();
    for (let i = 0; i < matrix.length; i++) {
        for (let j = i+1; j < matrix.length; j++) {
            const temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    return matrix;
};

console.log(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))