package main

import (
	"fmt"
	"strconv"
)

type TreeNode struct {
 Val int
 Left *TreeNode
 Right *TreeNode
}


type FindElements struct {
	NewTree *TreeNode
}


func Constructor(root *TreeNode) FindElements {
	root.Val = 0
	nodeList := []*TreeNode{root}

	for{
		var tempList []*TreeNode
		for i:=0 ; i<len(nodeList) ; i++{
			if nodeList[i].Left!=nil{
				nodeList[i].Left.Val = nodeList[i].Val*2+1
				tempList = append(tempList, nodeList[i].Left)
			}
			if nodeList[i].Right!=nil{
				nodeList[i].Right.Val = nodeList[i].Val*2+2
				tempList = append(tempList, nodeList[i].Right)
			}
		}
		nodeList = tempList

		if len(nodeList) == 0{
			break
		}
	}

	return FindElements{root}
}


func (f *FindElements) Find(target int) bool {
	res := false
	targetBinStr := strconv.FormatInt(int64(target+1), 2)
	point := f.NewTree

	for i:=1 ; i<len(targetBinStr) ; i++{
		if point == nil{
			break
		}
		if string(targetBinStr[i]) == "0"{
			point = point.Left
		}else if string(targetBinStr[i]) == "1"{
			point = point.Right
		}
	}

	if point != nil && point.Val == target{
		res = true
	}
	return res
}

func main()  {
	rootNode := &TreeNode{Val:-1}
	rootNode.Left = &TreeNode{Val:-1}
	rootNode.Right = &TreeNode{Val:-1}
	rootNode.Right.Left = &TreeNode{Val:-1}
	rootNode.Right.Right = &TreeNode{Val:-1}
	rootNode.Right.Right.Right = &TreeNode{Val:-1}

	res := Constructor(rootNode)
	//fmt.Println(res.NewTree.Val)
	//fmt.Println(res.NewTree.Left.Val)
	//fmt.Println(res.NewTree.Right.Val)
	//fmt.Println(res.NewTree.Right.Left.Val)
	//fmt.Println(res.NewTree.Right.Right.Val)
	//fmt.Println(res.NewTree.Right.Right.Right.Val)

	fmt.Println(res.Find(2))
	fmt.Println(res.Find(3))
	fmt.Println(res.Find(4))
	fmt.Println(res.Find(5))
}


