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

func main()  {
	queen := [][]int{{0, 1}, {1, 0}, {4, 0}, {0, 4}, {3, 3}, {2, 4}}
	king := []int{0, 0}
	result := queensAttacktheKing(queen, king)
	fmt.Println(result)
}
