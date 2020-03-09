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

func main()  {
	words := []string{"abc","deq","mee","aqq","dkd","ccc"}
	pattern := "abb"
	result := findAndReplacePattern(words, pattern)
	fmt.Print(result)
}
