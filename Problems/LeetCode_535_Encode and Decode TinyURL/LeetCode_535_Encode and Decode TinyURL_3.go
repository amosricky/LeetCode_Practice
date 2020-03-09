package main

import (
	"fmt"
	"math/rand"
	"strconv"
	"strings"
)

type tinyUrl struct {
	baseUrl string
	urlMap map[string]string
	letters []string
}

func (t *tinyUrl)letterInit()  {
	for i:=65;i<=90;i++{
		t.letters = append(t.letters, string(rune(i)))
	}
	for i:=97;i<=122;i++{
		t.letters = append(t.letters, string(rune(i)))
	}
	for i:=0;i<=9;i++{
		str := strconv.Itoa(i)
		t.letters = append(t.letters, str)
	}
}

func (t *tinyUrl)randomEncodeUrl() string {
	var encode string
	for i:=1; i<=6;i++{
		v := rand.Intn(61)
		encode = encode + t.letters[v]
	}
	return encode
}

func (t *tinyUrl)enCode(longUrl string) string {
	var encodeUrl string
	for{
		encodeUrl = t.randomEncodeUrl()
		if len(t.urlMap[encodeUrl]) == 0{
			t.urlMap[encodeUrl] = longUrl
			break
		}
	}

	return t.baseUrl + encodeUrl
}

func (t *tinyUrl)deCode(shortUrl string) string {
	urlList := strings.Split(shortUrl, "/")
	enCode := urlList[len(urlList)-1]

	return t.urlMap[enCode]
}

func main()  {
	longURL := "https://leetcode.com/problems/design-tinyurl"

	URL := tinyUrl{baseUrl:"http://tinyurl.com/", urlMap:make(map[string]string)}
	URL.letterInit()

	shortURL := URL.enCode(longURL)
	deCodeUrl := URL.deCode(shortURL)

	fmt.Println(shortURL)
	fmt.Println(deCodeUrl)
}
