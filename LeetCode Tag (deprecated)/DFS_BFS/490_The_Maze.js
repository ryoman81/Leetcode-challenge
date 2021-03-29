/**
 * There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. 
 * When the ball stops, it could choose the next direction.
 * Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
 * 
 * The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. 
 * The start and destination coordinates are represented by row and column indexes.
 * 
 * Example 1
 * 
 * Input 1: a maze represented by a 2D array
 * 0 0 1 0 0
 * 0 0 0 0 0
 * 0 0 0 1 0
 * 1 1 0 1 1
 * 0 0 0 0 0
 * Input 2: start coordinate (rowStart, colStart) = (0, 4)
 * Input 3: destination coordinate (rowDest, colDest) = (4, 4)
 * 
 * Output: true
 * Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
 */

const hasPath = function(maze, start, dest) {
    const m = maze.length;
    const n = maze[0].length;
    return DFS(start[0],start[1]);

    // DFS function gets the inputs of current ball location i and j, and return a bool if hit destination
    function DFS (i, j) {
        // if hit the destination then return
        if (i === dest[0] && j === dest[1]) return true;
        let y = i; let x = j;
        // memo a visited place as -1
        maze[y][x] = -1;
        // keep current state as false
        let res = false;
        // rolling in four directions following down, left, up, right
        // rolling down 
        while (y >= 0 && y < m && maze[y][x] !== 1)
            y += 1;
        y -= 1;
        // if hit the wall then try next direction from current point
        if (maze[y][x] != -1) 
            res = res || DFS(y, x);
        // rolling left 
        while (x >= 0 && x < n && maze[y][x] !== 1)
            x -= 1;
        x += 1;
        // if hit the wall then try next direction from current point
        if (maze[y][x] != -1) 
            res = res || DFS(y, x);
        // rolling up 
        while (y >= 0 && y < m && maze[y][x] !== 1)
            y -= 1;
        y += 1;
        // if hit the wall then try next direction from current point
        if (maze[y][x] != -1) 
            res = res || DFS(y, x);
        // rolling right 
        while (x >= 0 && x < n && maze[y][x] !== 1)
            x += 1;
        x -= 1;
        // if hit the wall then try next direction from current point
        if (maze[y][x] != -1) 
            res = res || DFS(y, x);

        // return the last result
        return res;
    }
}

const result = hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], [0,4], [4,4]);
console.log(result);