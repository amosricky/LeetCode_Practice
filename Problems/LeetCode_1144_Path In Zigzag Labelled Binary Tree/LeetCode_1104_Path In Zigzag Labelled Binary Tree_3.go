package main

import (
	"fmt"
	"math"
)

func pathInZigZagTree(label int) []int {
	var result []int
	var nodeIndex int
	depth := int(math.Log2(float64(label))) + 1

	if depth %2 == 0{
		nodeIndex = int(math.Pow(2, float64(depth))) - 1 - label
	}else {
		nodeIndex = label - int(math.Pow(2, float64(depth - 1)))
	}

	result = append([]int{label}, result...)

	for step:=depth - 1; step>0; step--{
		nodeIndex = nodeIndex/2
		var nodeValue int
		if step %2 == 0{
			nodeValue = int(math.Pow(2, float64(step))) - 1 - nodeIndex
		}else {
			nodeValue = int(math.Pow(2, float64(step - 1))) + nodeIndex
		}
		result = append([]int{nodeValue}, result...)
	}
	return result
}

func main()  {
	fmt.Println(pathInZigZagTree(15))
}
