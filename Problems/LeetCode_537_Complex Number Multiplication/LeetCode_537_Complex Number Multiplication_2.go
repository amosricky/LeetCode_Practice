package main

import (
	"fmt"
	"regexp"
	"strconv"
)

func complexNumberMultiply(a string, b string) string {
	regRule := regexp.MustCompile(`-?[0-9]+`)
	strIntA := regRule.FindAllString(a, -1)
	strIntB := regRule.FindAllString(b, -1)
	aR1 , _ := strconv.Atoi(strIntA[0])
	aR2 , _ := strconv.Atoi(strIntA[1])
	bR1 , _ := strconv.Atoi(strIntB[0])
	bR2 , _ := strconv.Atoi(strIntB[1])
	R1 := aR1 * bR1 - aR2 * bR2
	R2 := aR1 * bR2 + aR2 * bR1

	return fmt.Sprintf("%v+%vi", R1, R2)
}

func main()  {
	fmt.Println(complexNumberMultiply("2+5i", "2+3i"))
}