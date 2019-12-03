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


myClass = Codec()
enCodeUrl = myClass.encode("https://leetcode.com/problems/design-tinyurl")
print(enCodeUrl)
deCodeUrl = myClass.decode(enCodeUrl)
print(deCodeUrl)
