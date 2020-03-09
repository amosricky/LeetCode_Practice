# 【LeetCode】 535. Encode and Decode TinyURL

## Description
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Note:

+ This is a companion problem to the [System Design](https://leetcode.com/discuss/interview-question/system-design/?currentPage=1&orderBy=hot&query=)
 problem: [Design TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/).


## Solution1
* 透過 md5 產生 hash ，再塞入 Map。
* 優點是不易碰撞，但結果較長。

### Code1
```python
import hashlib
class Codec:

    def __init__(self):
        self.baseUrl = "http://tinyurl.com/"
        self.urls = {}

    def encode(self, longUrl: 'str') -> 'str':
        """Encodes a URL to a shortened URL.
        """
        m = hashlib.md5()
        m.update(longUrl.encode("utf8"))
        enCode = m.hexdigest()
        self.urls[enCode] = longUrl
        return self.baseUrl + enCode

    def decode(self, shortUrl: 'str') -> 'str':
        """Decodes a shortened URL to its original URL.
        """
        enCode = shortUrl.split("/")[-1]
        return self.urls[enCode]
```
## Solution2
* 將 lowerletter + upplerletter + digit 塞入 List，再隨機從中取 6 個亂數當 hash。
* 但碰撞風險較高。

### Code2
```python
import string, random
class Codec:

    def __init__(self):
        self.baseUrl = "http://tinyurl.com/"
        self.urls = {}
        self.letters = string.ascii_letters + string.digits

    def randomStr(self) -> 'str':
        res = ""
        for i in range(6):
            res += self.letters[random.randint(0, 61)]
        return res

    def encode(self, longUrl: 'str') -> 'str':
        """Encodes a URL to a shortened URL.
        """
        encodeUrl = ''
        while True:
            encodeUrl = self.randomStr()
            if encodeUrl not in self.urls.keys():
                break
        self.urls[encodeUrl] = longUrl
        return self.baseUrl + encodeUrl

    def decode(self, shortUrl: 'str') -> 'str':
        """Decodes a shortened URL to its original URL.
        """
        encodeUrl = shortUrl.split('/')[-1]
        if encodeUrl in self.urls.keys():
            return self.urls[encodeUrl]
        else:
            return None
```

## Solution3
* Golang Version，解法與 2 相同。

### Code3
<pre><code>
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
</code></pre>

###### tags: `LeetCode` `python` `golang` `Encode and Decode TinyURL` 