# 【LeetCode】 1222. Queens That Can Attack the King

## Description
On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.

Constraints:

+ 1 <= queens.length <= 63
+ queens[0].length == 2
+ 0 <= queens[i][j] < 8
+ king.length == 2
+ 0 <= king[0], king[1] < 8
+ At most one piece is allowed in a cell.

## Example 1:
![](https://assets.leetcode.com/uploads/2019/10/01/untitled-diagram.jpg)
```
Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:  
The queen at [0,1] can attack the king cause they're in the same row. 
The queen at [1,0] can attack the king cause they're in the same column. 
The queen at [3,3] can attack the king cause they're in the same diagnal. 
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.
```

## Example 2:
![](https://assets.leetcode.com/uploads/2019/10/01/untitled-diagram-1.jpg)
```
Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]
```

## Example 3:
![](https://assets.leetcode.com/uploads/2019/10/01/untitled-diagram-2.jpg)
```
Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
```

## Solution1
* 以 King 為起始位置，往上下左右及對角（共 8 個方向找尋）。
* 若發現 Queen 則加入 result list，停止搜尋往下個方向找。

### Code1
```python
class Solution:
    def queensAttacktheKing(self, queens: "List[List[int]]", king: "List[int]") -> "List[List[int]]":
        directionList = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        res = []

        for direction in directionList:
            newLocation = [sum(i) for i in zip(king, direction)]
            while 8 > newLocation[0] > -1 and 8 > newLocation[1] > -1:
                if newLocation in queens:
                    res.append(newLocation)
                    break
                newLocation = [sum(i) for i in zip(newLocation, direction)]
        return res
```
## Solution2
* 同樣方法 Golang version。

### Code2
```golang
package main

import "fmt"

func queensAttacktheKing(queens [][]int, king []int) [][]int {
	type direction = [2]int
	directionMap := [8]direction{{-1,-1},{-1,0},{-1,1},{0,1},{1,1},{1,0},{1,-1},{0,-1}}
	var result [][]int

	for _, direct := range directionMap{
		location := []int{king[0]+direct[0], king[1]+direct[1]}
		for{
			if check:=find(location, queens); check{
				result = append(result, location)
				break
			}

			location = []int{location[0]+direct[0], location[1]+direct[1]}

			if !(-1 < location[0] && location[0] < 8 && -1 < location[1] && location[1] < 8){
				break
			}
		}

	}

	return result
}

func find(location []int, queens [][]int) bool {
	res := false
	for _, queen := range queens{
		if queen[0] == location[0] && queen[1] == location[1]{
			res = true
			break
		}
	}
	return res
}
```

###### tags: `LeetCode` `python` `Golang` `Queens That Can Attack the King` 