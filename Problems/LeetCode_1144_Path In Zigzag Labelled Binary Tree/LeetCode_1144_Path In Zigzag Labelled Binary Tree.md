# 【LeetCode】 1144. Path In Zigzag Labelled Binary Tree

## Description
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

![](https://assets.leetcode.com/uploads/2019/06/24/tree.png)

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

Constraints:

+ 1 <= label <= 10^6

## Example 1:
```
Input: label = 14
Output: [1,3,4,14]
```

## Example 2:
```
Input: label = 26
Output: [1,2,6,10,26]
```

## Solution1
* 將找尋 parent node 包為 function , 若 label 不為 1 , 由下搜尋往上搜尋。
* 效果還行 runtime 95%, memory use 100% , 但過多 if else。

### Code1
```python
import math
class Solution:
    def __init__(self):
        self.result = [1]

    def pathInZigZagTree(self, label: "int") -> "List[int]":

        node = label
        while node != 1:
            self.result.append(node)
            parent = self.findParent(node)
            if parent == 1:
                break
            node = parent
        return sorted(self.result)

    def findParent(self, nodeNum: "int") -> "int":
        step = 1
        column = 1
        parentNum = 1
        while 2 ** step - 1 < nodeNum:
            step += 1
        if step % 2 == 0:
            column = 2 ** step - nodeNum
        else:
            column = nodeNum - (2 ** (step - 1) - 1)

        if step != 1 and (step - 1) % 2 == 0:
            parentNum = 2 ** (step - 1) - math.ceil(column / 2)

        elif step != 1 and (step - 1) % 2 == 1:
            parentNum = 2 ** (step - 2) + math.ceil(column / 2) - 1

        return parentNum
```
## Solution2
* 重構一下 , 減少 if else 判斷
* 效果一樣 runtime 95%, memory use 100% 。

### Code2
```python
import math
class Solution:
    def pathInZigZagTree(self, label: "int") -> "List[int]":
        depth = int(math.log(label, 2)) + 1
        nodeIndex = 0
        nodeList = []

        if depth % 2 == 0:
            nodeIndex = (2 ** depth) - 1 - label
        else:
            nodeIndex = label - (2 ** (depth - 1))

        nodeList.insert(0, label)

        for step in range(depth - 1, 0, -1):
            nodeIndex = int(nodeIndex/2)
            if step % 2 == 0:
                nodeList.insert(0, 2 ** step - 1 - nodeIndex)
            else:
                nodeList.insert(0, 2 ** (step - 1) + nodeIndex)

        return nodeList
```

## Solution3
* Solution2 方法改用 golang 
* 效果變成 runtime 100%, memory use 100% , 不明所以。

### Code3
```golang
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
```

###### tags: `LeetCode` `python` `golang` `Path In Zigzag Labelled Binary Tree` 
