# 【LeetCode】 1261. Find Elements in a Contaminated Binary Tree

## Description
Given a binary tree with the following rules:

    1.root.val == 0
    2.If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
    3.If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
    
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

You need to first recover the binary tree and then implement the FindElements class:

    * FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
    * bool find(int target) Return if the target value exists in the recovered binary tree.

Constraints:

+ TreeNode.val == -1
+ The height of the binary tree is less than or equal to 20
+ The total number of nodes is between [1, 10^4]
+ Total calls of find() is between [1, 10^4]
+ 0 <= target <= 10^6

## Example 1:
![](https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4-1.jpg)
```
Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
```

## Example 2:
![](https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4.jpg)
```
Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
```

## Example 3:
![](https://assets.leetcode.com/uploads/2019/11/07/untitled-diagram-4-1-1.jpg)
```
Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
```

## Solution1
* recursive 方式建 tree。
* 再依階層找尋 target。
* 速度過慢。

### Code1
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: 'TreeNode'):
        self.root = root
        self.root.val = 0
        self.recoveredTree(self.root)


    def recoveredTree(self, rootNode: 'TreeNode'):
        if rootNode and rootNode.left:
            rootNode.left.val = (rootNode.val * 2) + 1
            self.recoveredTree(rootNode.left)
        if rootNode and rootNode.right:
            rootNode.right.val = (rootNode.val * 2) + 2
            self.recoveredTree(rootNode.right)

    def find(self, target: 'int') -> 'bool':
        res = False
        nodeList = [self.root]

        while nodeList:
            tempList = []
            for node in nodeList:
                if node.val == target:
                    res = True
                    return res
                if node.left:
                    tempList.append(node.left)
                if node.right:
                    tempList.append(node.right)
            nodeList = tempList
        return res
```
## Solution2
* 一樣 recursive 方式建 tree。
* 將 val 存入 list。
* 速度一樣過慢。

### Code2
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: 'TreeNode'):
        self.root = root
        self.root.val = 0
        self.rootList = [0]
        self.recoveredTree(self.root)

    def recoveredTree(self, rootNode: 'TreeNode'):
        if rootNode and rootNode.left:
            rootNode.left.val = (rootNode.val * 2) + 1
            self.rootList.append(rootNode.left.val)
            self.recoveredTree(rootNode.left)
        if rootNode and rootNode.right:
            rootNode.right.val = (rootNode.val * 2) + 2
            self.rootList.append(rootNode.right.val)
            self.recoveredTree(rootNode.right)

    def find(self, target: 'int') -> 'bool':
        if target in self.rootList:
            return True
        return False
```
## Solution3
* 一樣 recursive 方式建 tree。
* 將 target + 1 後轉為 binary。
* 從 binary 中取 str , 為 0 往左 , 為 1 往右。
* 速度提昇。

### Code3
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: 'TreeNode'):
        self.root = root
        self.root.val = 0
        self.recoveredTree(self.root)

    def recoveredTree(self, rootNode: 'TreeNode'):
        if rootNode and rootNode.left:
            rootNode.left.val = (rootNode.val * 2) + 1
            self.recoveredTree(rootNode.left)
        if rootNode and rootNode.right:
            rootNode.right.val = (rootNode.val * 2) + 2
            self.recoveredTree(rootNode.right)

    def find(self, target: 'int') -> 'bool':

        targetBin = bin(target + 1)
        node = self.root
        res = False

        for val in targetBin[3:]:
            if not node:
                break
            if val == "0":
                node = node.left
            elif val == "1":
                node = node.right

        if node and node.val == target:
            res = True

        return res
```
## Solution4
* recursive 方式建 tree。
* 將 target + 1 後轉為 binary。
* 從 binary 中取 str , 為 0 往左 , 為 1 往右。
* 速度普通。

### Code4
<pre><code>
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
	return ConstructorRecursive(root,0)
}

func ConstructorRecursive(root *TreeNode, nodeVal int) FindElements {
	root.Val = nodeVal
	if root.Left != nil {
		root.Left.Val = nodeVal*2+1
		ConstructorRecursive(root.Left, nodeVal*2+1)
	}
	if root.Right != nil{
		root.Right.Val = nodeVal*2+2
		ConstructorRecursive(root.Right,nodeVal*2+2)
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
</code></pre>

## Solution5
* non-recursive 方式建 tree。
* 將 target + 1 後轉為 binary。
* 從 binary 中取 str , 為 0 往左 , 為 1 往右。
* 速度提昇。

### Code5
<pre><code>
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
</code></pre>

###### tags: `LeetCode` `python` `golang` `Find Elements in a Contaminated Binary Tree` 