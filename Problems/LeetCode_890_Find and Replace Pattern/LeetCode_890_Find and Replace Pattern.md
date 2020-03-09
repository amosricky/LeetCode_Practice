# 【LeetCode】 890. Find and Replace Pattern

## Description
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

Note:
+ 1 <= words.length <= 50
+ 1 <= pattern.length = words[i].length <= 20

## Example:

```
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
```

## Solution1
* 利用 Map 儲存 Pattern mapping word 的 rule。

### Code1
```python
class Solution:
    def findAndReplacePattern(self, words: 'List[str]', pattern: 'str') -> 'List[str]':
        rule = {}
        res = []

        for word in words:
            check = True
            for index, alpha in enumerate(word):
                if (pattern[index] not in rule.keys()) and (alpha not in rule.values()):
                    rule[pattern[index]] = alpha

                elif (pattern[index] in rule.keys()) and (alpha == rule[pattern[index]]):
                    continue
                else:
                    check = False
                    break

            if check:
                res.append(word)
            rule = {}

        return res
```

## Solution2
* Golang 版本，作法差不多，但 Golang 無法直接取 map.value() ， 故多一變數 added 來紀錄。

### Code2
<pre><code>
package main

import "fmt"

func findAndReplacePattern(words []string, pattern string) []string {
	var res []string

	for _, word := range words {
		//ruleKeys := reflect.ValueOf(rule).MapKeys()
		rule := make(map[string]string)
		added := make(map[string]string)
		check := true
		for key, value := range word{
			if (len(rule[string(pattern[key])]) == 0) && (len(added[string(value)]) == 0) {
				rule[string(pattern[key])] = string(value)
				added[string(value)] = string(pattern[key])
			}else if rule[string(pattern[key])] == string(value){
				continue
			}else {
				check = false
				break
			}
		}
		if check{
			res = append(res, word)
		}
	}
	return res
}
</code></pre>
###### tags: `LeetCode` `python` `golang` `Find and Replace Pattern` 