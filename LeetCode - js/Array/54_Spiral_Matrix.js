/**
 * Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
 * 
 * Example 1:
 * 
 * Input:
 * [
 *  [ 1, 2, 3 ],
 *  [ 4, 5, 6 ],
 *  [ 7, 8, 9 ]
 * ]
 * Output: [1,2,3,6,9,8,7,4,5]
 */

var spiralOrder = function(matrix) {
    if (!matrix.length) return [];
    const result = [];
    const row = matrix.length;
    const col = matrix[0].length;
    
    let i = 0, j = 0, r = 0;
    result.push(matrix[i][j]);
    while (true) {
        j++;
        while (j < col - r) {
            result.push(matrix[i][j]);
            j++;
        }

        i++; j--;
        if (i >= row - r) break;
        while (i < row - r) {
            result.push(matrix[i][j]);
            i++;
        }

        j--; i--;
        if (j < r) break;
        while (j >= r) {
            result.push(matrix[i][j]);
            j--;
        }

        i--; j++;
        if (i <= r) break;
        while (i > r) {
            result.push(matrix[i][j]);
            i--;
        }
        if (j >= col - r) break;
        r++;
        i++;
        
    }
    return result;
};

console.log(
    spiralOrder(
        [
            [3,123,534,123,33],
            [2,78,56,38,95],
            [7,9,0,2,5],
            [84,22,65,32,1]
        ]
  )
)