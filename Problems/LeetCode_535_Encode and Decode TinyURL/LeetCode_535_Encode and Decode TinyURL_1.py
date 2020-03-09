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


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

myClass = Codec()
enCodeUrl = myClass.encode("https://leetcode.com/problems/design-tinyurl")
print(enCodeUrl)
deCodeUrl = myClass.decode(enCodeUrl)
print(deCodeUrl)
